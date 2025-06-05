import os
import sys
import logging
import json
from antlr4 import *
from huggingface_hub import InferenceClient
from CompiledFiles.FinanceLexer import FinanceLexer
from CompiledFiles.FinanceParser import FinanceParser as ANTLRParser
from CompiledFiles.FinanceListener import FinanceListener

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class IntentListener(FinanceListener):
    def __init__(self):
        self.intents = []
    
    def exitSalaryStmt(self, ctx):
        amount, original_amount = self.parse_amount(ctx.amount())
        currency = ctx.CURRENCY().getText()
        self.intents.append({
            "type": "salary",
            "amount": amount,
            "original_amount": original_amount,
            "currency": currency
        })
    
    def exitCategoryStmt(self, ctx):
        categories = []
        for cat_item in ctx.categoryList().categoryItem():
            amount, original_amount = self.parse_amount(cat_item.amount())
            currency = cat_item.CURRENCY().getText()
            category = cat_item.category().getText()
            categories.append((category, amount, original_amount, currency))
        self.intents.append({"type": "category", "categories": categories})
    
    def exitSpendStmt(self, ctx):
        amount, original_amount = self.parse_amount(ctx.amount())
        currency = ctx.CURRENCY().getText()
        item = ' '.join([id.getText() for id in ctx.item().ID()])
        category = ctx.category().getText() if ctx.category() else self.infer_category(item)
        self.intents.append({
            "type": "spend",
            "amount": amount,
            "item": item,
            "category": category,
            "original_amount": original_amount,
            "currency": currency
        })
    
    def exitModifyCategoryStmt(self, ctx):
        category = ctx.category().getText()
        amount, original_amount = self.parse_amount(ctx.amount())
        currency = ctx.CURRENCY().getText()
        self.intents.append({
            "type": "modify_category",
            "category": category,
            "amount": amount,
            "original_amount": original_amount,
            "currency": currency
        })
    
    def exitDeleteCategoryStmt(self, ctx):
        category = ctx.category().getText()
        self.intents.append({"type": "delete_category", "category": category})
    
    def exitResetStmt(self, ctx):
        self.intents.append({"type": "reset"})
    
    def exitAnalyzeStmt(self, ctx):
        self.intents.append({"type": "analyze"})
    
    def exitGraphStmt(self, ctx):
        self.intents.append({"type": "graph"})
    
    def parse_amount(self, ctx):
        """Parse amount in Vietnamese number format or with multipliers (e.g., 10.000.000 or 5 million)."""
        numbers = [num.getText() for num in ctx.NUMBER()]
        multiplier = ctx.multiplier().getText() if ctx.multiplier() else None
        try:
            base_amount = int(''.join(numbers))
            if multiplier:
                multiplier = multiplier.lower()
                if multiplier in ['million', 'm']:
                    base_amount *= 1_000_000
                elif multiplier in ['thousand', 'k']:
                    base_amount *= 1_000
            return base_amount, base_amount
        except ValueError as e:
            logging.error(f"Error parsing amount: {numbers}, multiplier: {multiplier}")
            raise e
    
    def infer_category(self, item):
        food_items = ["pho", "tea", "coffee", "food", "drink", "noodle", "rice"]
        emergency_items = ["fix", "repair", "emergency"]
        hobby_items = ["gundam", "hobby"]
        
        item_lower = item.lower()
        if any(food in item_lower for food in food_items):
            return "Food"
        elif any(em in item_lower for em in emergency_items):
            return "Emergency"
        elif any(hobby in item_lower for hobby in hobby_items):
            return "Hobby"
        return "Other"

class FinanceParser:
    def __init__(self):
        self.hf_client = None
        hf_api_key = os.environ.get("HF_TOKEN")
        logging.debug(f"HF_TOKEN present: {bool(hf_api_key)}")
        if not hf_api_key:
            logging.warning("HF_TOKEN environment variable not set. Hugging Face API will be disabled.")
            return
        
        try:
            self.hf_client = InferenceClient(api_key=hf_api_key)
            logging.debug("Hugging Face InferenceClient initialized successfully")
        except Exception as e:
            logging.error(f"Failed to initialize Hugging Face client: {str(e)}")
            self.hf_client = None

    def parse_with_huggingface(self, text):
        """Use Hugging Face Conversational API to convert conversational input to structured command."""
        logging.debug(f"Attempting to parse with Hugging Face: {text}")
        if not self.hf_client:
            logging.error("Hugging Face client not initialized. Cannot parse with Hugging Face.")
            return []

        system_prompt = """
You are a financial assistant that converts natural language inputs into structured commands for a finance chatbot. The chatbot understands the following commands:
1. Set salary: "i have [amount] [currency] this month" (e.g., "i have 5000000 vnd this month")
2. Set categories: "i want [amount] [currency] for [category], [amount] [currency] for [category]" (e.g., "i want 2000000 vnd for food, 1000000 vnd for emergency")
3. Record spending: "i spent [amount] [currency] for [item] in [category]" (e.g., "i spent 50000 vnd for pho in food")
4. Modify category: "change the money for [category] to [amount] [currency]" (e.g., "change the money for food to 2500000 vnd")
5. Delete category: "delete [category]" (e.g., "delete food")
6. Reset data: "reset"
7. Analyze finances: "analyze" or "give advice"
8. Show graph: "graph" or "show graph"

Supported currencies: VND, USD, EUR, JPY, CNY.
Categories can be any single word (e.g., Food, Emergency, Hobby).
Items can be multiple words (e.g., "pho", "car repair").
Amounts can include shorthand like '5 million' (5000000) or '50k' (50000).

Convert the user input into one or more of the above commands. Return the command(s) as a JSON list of strings (e.g., ["i have 5000000 vnd this month"]). Do not include explanations or other fields. If the input is ambiguous or unclear, return an empty list.
"""
        try:
            response = self.hf_client.chat_completion(
                model="meta-llama/Meta-Llama-3-8B-Instruct",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Input: {text}\nOutput:"}
                ],
                max_tokens=200
            )
            logging.debug(f"Hugging Face response: {response.choices[0].message.content}")
            response_text = response.choices[0].message.content.strip()

            # Parse the response as JSON
            try:
                commands = json.loads(response_text)
                if not isinstance(commands, list):
                    commands = [commands]
                return [cmd.strip() for cmd in commands if isinstance(cmd, str) and cmd.strip()]
            except json.JSONDecodeError:
                logging.warning(f"Invalid JSON response: {response_text}")
                if response_text.strip():
                    return [response_text.strip()]
                return []
        except Exception as e:
            logging.error(f"Error with Hugging Face API: {str(e)}")
            return []

    def parse(self, text):
        """Parse user input, preferring Hugging Face for conversational inputs."""
        logging.debug(f"Parsing input: {text}")
        # Check if input contains textual amounts (e.g., 'million', 'thousand')
        if any(word in text.lower() for word in ['million', 'm', 'thousand', 'k']):
            commands = self.parse_with_huggingface(text)
            logging.debug(f"Hugging Face parsed commands: {commands}")
            intents = []
            for cmd in commands:
                try:
                    input_stream = InputStream(cmd)
                    lexer = FinanceLexer(input_stream)
                    stream = CommonTokenStream(lexer)
                    parser = ANTLRParser(stream)
                    tree = parser.start()
                    
                    listener = IntentListener()
                    walker = ParseTreeWalker()
                    walker.walk(listener, tree)
                    intents.extend(listener.intents)
                    logging.debug(f"Successfully parsed Hugging Face command '{cmd}' into intents: {listener.intents}")
                except Exception as e:
                    logging.error(f"Failed to parse Hugging Face command '{cmd}': {str(e)}")
            if intents:
                return intents
            return [{"type": "error", "message": "You entered an incorrect prompt structure. Try one of these suggestions:\ni have 5000000 vnd this month\ni want 2000000 vnd for food, 1000000 vnd for emergency\ni spent 50000 vnd for pho in food\nchange the money for food to 2500000 vnd\ndelete category food\nanalyze\ngraph\nreset"}]

        # Try ANTLR for structured inputs
        try:
            input_stream = InputStream(text)
            lexer = FinanceLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = ANTLRParser(stream)
            tree = parser.start()
            
            listener = IntentListener()
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
            
            if listener.intents:
                logging.debug(f"ANTLR parsed intents: {listener.intents}")
                return listener.intents
        except Exception as e:
            logging.warning(f"ANTLR parsing failed: {str(e)}")
        
        # Fallback to Hugging Face if ANTLR fails
        commands = self.parse_with_huggingface(text)
        logging.debug(f"Hugging Face parsed commands: {commands}")
        intents = []
        for cmd in commands:
            try:
                input_stream = InputStream(cmd)
                lexer = FinanceLexer(input_stream)
                stream = CommonTokenStream(lexer)
                parser = ANTLRParser(stream)
                tree = parser.start()
                
                listener = IntentListener()
                walker = ParseTreeWalker()
                walker.walk(listener, tree)
                intents.extend(listener.intents)
                logging.debug(f"Successfully parsed Hugging Face command '{cmd}' into intents: {listener.intents}")
            except Exception as e:
                logging.error(f"Failed to parse Hugging Face command '{cmd}': {str(e)}")
        if intents:
            return intents
        
        logging.debug("No valid intents parsed. Returning error intent.")
        return [{"type": "error", "message": "You entered an incorrect prompt structure. Try one of these suggestions:\ni have 5000000 vnd this month\ni want 2000000 vnd for food, 1000000 vnd for emergency\ni spent 50000 vnd for pho in food\nchange the money for food to 2500000 vnd\ndelete category food\nanalyze\ngraph\nreset"}]