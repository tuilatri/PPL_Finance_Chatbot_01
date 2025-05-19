import os
import sys
from antlr4 import *
sys.path.append(os.path.join(os.path.dirname(__file__), 'CompiledFiles'))
from CompiledFiles.FinanceLexer import FinanceLexer
from CompiledFiles.FinanceParser import FinanceParser as ANTLRParser
from CompiledFiles.FinanceListener import FinanceListener

class IntentListener(FinanceListener):
    def __init__(self):
        self.intents = []
    
    def exitSalaryStmt(self, ctx):
        amount = self.parse_amount(ctx.amount())
        self.intents.append({"type": "salary", "amount": amount})
    
    def exitCategoryStmt(self, ctx):
        categories = []
        for cat_item in ctx.categoryList().categoryItem():
            amount = self.parse_amount(cat_item.amount())
            category = cat_item.category().getText()
            categories.append((category, amount))
        self.intents.append({"type": "category", "categories": categories})
    
    def exitSpendStmt(self, ctx):
        amount = self.parse_amount(ctx.amount())
        item = ' '.join([id.getText() for id in ctx.item().ID()])
        category = ctx.category().getText() if ctx.category() else self.infer_category(item)
        self.intents.append({"type": "spend", "amount": amount, "item": item, "category": category})
    
    def exitModifyCategoryStmt(self, ctx):
        category = ctx.category().getText()
        amount = self.parse_amount(ctx.amount())
        self.intents.append({"type": "modify_category", "category": category, "amount": amount})
    
    def exitDeleteCategoryStmt(self, ctx):
        category = ctx.category().getText()
        self.intents.append({"type": "delete_category", "category": category})
    
    def exitResetStmt(self, ctx):
        self.intents.append({"type": "reset"})
    
    def parse_amount(self, ctx):
        """Parse amount in Vietnamese number format (e.g., 10.000.000 -> 10000000)."""
        numbers = [num.getText() for num in ctx.NUMBER()]
        try:
            return int(''.join(numbers))
        except ValueError as e:
            print(f"Error parsing amount: {numbers}")
            raise e
    
    def infer_category(self, item):
        # Simple heuristic for category inference
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
    def parse(self, text):
        """Parse user input and return list of intents."""
        input_stream = InputStream(text)
        lexer = FinanceLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ANTLRParser(stream)
        tree = parser.start()
        
        listener = IntentListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        
        return listener.intents