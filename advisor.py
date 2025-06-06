import spacy
from collections import Counter
import logging
from datetime import datetime, timedelta
from huggingface_hub import InferenceClient
import os
import sqlite3
from utils import format_vnd

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Advisor:
    def __init__(self):
        try:
            # Load small English model for local NLP
            self.nlp = spacy.load("en_core_web_sm")
            logging.debug("Spacy model loaded successfully")
            
            # Initialize Hugging Face client
            hf_api_key = os.environ.get("HF_TOKEN")
            if not hf_api_key:
                logging.warning("HF_TOKEN not set. Advanced NLP features disabled.")
                self.hf_client = None
            else:
                self.hf_client = InferenceClient(api_key=hf_api_key)
                logging.debug("Hugging Face InferenceClient initialized successfully")
        except Exception as e:
            logging.error(f"Initialization error: {str(e)}")
            raise

    def get_historical_spending(self, user_id, days=30):
        """Retrieve spending data for the past 'days' days."""
        try:
            # Create a new connection for this request
            conn = sqlite3.connect('finance_chatbot.db')
            cursor = conn.cursor()
            end_date = datetime.now()
            start_date = end_date - timedelta(days=days)
            cursor.execute('''
                SELECT category, SUM(amount), date FROM spending
                WHERE user_id = ? AND date >= ?
                GROUP BY category, date
            ''', (user_id, start_date.strftime('%Y-%m-%d %H:%M:%S')))
            data = cursor.fetchall()
            conn.close()
            return data
        except Exception as e:
            logging.error(f"Error fetching historical spending: {str(e)}")
            return []

    def analyze_spending_trends(self, historical_data):
        """Analyze spending trends over time."""
        trends = {}
        for category, amount, date in historical_data:
            try:
                week = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').isocalendar()[1]
                if category not in trends:
                    trends[category] = {}
                if week not in trends[category]:
                    trends[category][week] = 0
                trends[category][week] += amount
            except ValueError as e:
                logging.warning(f"Invalid date format in historical data: {date}, error: {str(e)}")
                continue
        return trends

    def infer_item_necessity(self, item):
        """Use Hugging Face to classify items as essential or non-essential."""
        if not self.hf_client:
            # Fallback to simple rule-based classification
            essential_items = ["pho", "food", "groceries", "utilities", "rent", "repair"]
            return "essential" if any(e in item.lower() for e in essential_items) else "non-essential"
        
        prompt = f"""
Classify the following item as 'essential' or 'non-essential' for financial budgeting:
Item: {item}
Return only the classification ('essential' or 'non-essential').
"""
        try:
            response = self.hf_client.chat_completion(
                model="meta-llama/Meta-Llama-3-70B-Instruct",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=20
            )
            return response.choices[0].message.content.strip().lower()
        except Exception as e:
            logging.error(f"Error classifying item '{item}': {str(e)}")
            # Fallback to rule-based classification
            essential_items = ["pho", "food", "groceries", "utilities", "rent", "repair"]
            return "essential" if any(e in item.lower() for e in essential_items) else "non-essential"

    def generate_advice(self, data, user_id="daily"):
        """Analyze spending data and generate financial advice."""
        logging.debug(f"Generating advice with data: {data}")
        if not data.get('actions'):
            logging.info("No actions to analyze")
            return "No financial activity to analyze yet. Try adding a salary or spending some money!"

        salary = data.get('salary', 0)
        not_used = data.get('not_used', 0)
        categories = data.get('categories', {})
        actions = data.get('actions', [])

        # Calculate spending by category
        category_spending = {cat: 0 for cat in categories}
        item_counts = Counter()
        non_essential_spending = 0
        for action in actions:
            try:
                if not isinstance(action, dict):
                    continue
                # Check for spending actions (must have amount, category, and optionally item)
                if 'amount' in action and 'category' in action:
                    category = action['category']
                    amount = action['amount']
                    if category in category_spending:
                        category_spending[category] += amount
                    if 'item' in action:
                        item = action['item'].lower()
                        item_counts[item] += 1
                        # Classify item necessity
                        necessity = self.infer_item_necessity(item)
                        if necessity == "non-essential":
                            non_essential_spending += amount
            except Exception as e:
                logging.warning(f"Error processing action: {action}, error: {str(e)}")
                continue

        # Analyze historical spending trends
        historical_data = self.get_historical_spending(user_id)
        trends = self.analyze_spending_trends(historical_data)

        # Generate advice
        advice = []

        # 1. High spending in any category (>40% of salary)
        for category, amount in category_spending.items():
            if salary > 0 and amount / salary > 0.4:
                advice.append(
                    f"You're spending {amount / salary * 100:.1f}% of your salary ({format_vnd(amount)} VND) on {category}. "
                    f"Consider reducing this to align with a balanced budget (e.g., 50/30/20 rule: 50% needs, 30% wants, 20% savings)."
                )

        # 2. High unallocated money (>60% of salary)
        if salary > 0 and not_used / salary > 0.6:
            advice.append(
                f"You have {not_used / salary * 100:.1f}% of your salary ({format_vnd(not_used)} VND) unallocated. "
                f"Consider allocating 20% to savings or investments to build wealth over time."
            )

        # 3. Non-essential spending warning
        if salary > 0 and non_essential_spending / salary > 0.3:
            advice.append(
                f"You're spending {non_essential_spending / salary * 100:.1f}% of your salary ({format_vnd(non_essential_spending)} VND) on non-essential items. "
                f"Try redirecting some of this to savings or essential categories."
            )

        # 4. Frequent spending items
        frequent_items = [item for item, count in item_counts.items() if count > 1]  # Lowered to >1 to catch repeated items in test data
        if frequent_items:
            advice.append(
                f"You frequently spend on {', '.join(frequent_items)}. "
                f"Review these purchases to see if they can be reduced or substituted with cheaper alternatives."
            )

        # 5. Spending trends analysis
        for category, weekly_spending in trends.items():
            if len(weekly_spending) > 1:
                weeks = sorted(weekly_spending.keys())
                amounts = [weekly_spending[week] for week in weeks]
                if all(amounts[i] < amounts[i + 1] for i in range(len(amounts) - 1)):
                    advice.append(
                        f"Your spending in {category} is increasing week-over-week. "
                        f"Monitor this category to avoid overspending."
                    )

        # 6. Apply 50/30/20 rule recommendation
        if salary > 0:
            needs = sum(category_spending.get(cat, 0) for cat in ['Food', 'Housing', 'Utilities', 'Transportation', 'Renting'])
            wants = sum(category_spending.get(cat, 0) for cat in ['Hobby', 'Entertainment', 'Shopping'])
            savings = salary - needs - wants - sum(category_spending.get(cat, 0) for cat in category_spending if cat not in ['Food', 'Housing', 'Utilities', 'Transportation', 'Renting', 'Hobby', 'Entertainment', 'Shopping'])
            if needs / salary > 0.5:
                advice.append(
                    f"Your spending on needs ({format_vnd(needs)} VND) exceeds 50% of your salary. "
                    f"Try to optimize essential expenses to align with the 50/30/20 budgeting rule."
                )
            if wants / salary > 0.3:
                advice.append(
                    f"Your spending on wants ({format_vnd(wants)} VND) exceeds 30% of your salary. "
                    f"Consider cutting back on non-essential spending to free up funds for savings."
                )
            if savings / salary < 0.2:
                advice.append(
                    f"Your savings ({format_vnd(savings)} VND) are below 20% of your salary. "
                    f"Aim to allocate at least 20% to savings or debt repayment for financial security."
                )

        # 7. NLP-based item analysis with spaCy
        spend_descriptions = [
            action.get('item', '') for action in actions
            if isinstance(action, dict) and 'item' in action
        ]
        if spend_descriptions:
            try:
                doc = self.nlp(" ".join(spend_descriptions))
                entities = [ent.text for ent in doc.ents if ent.label_ in ["PRODUCT", "MONEY", "ORG"]]
                if entities:
                    advice.append(
                        f"You've mentioned items like {', '.join(entities)}. "
                        f"Ensure these align with your financial priorities and long-term goals."
                    )
            except Exception as e:
                logging.error(f"Error processing spaCy descriptions: {str(e)}")

        # 8. General advice if no specific issues
        if not advice:
            total_spent = sum(category_spending.values())
            if salary > 0 and total_spent / salary < 0.3:
                advice.append(
                    "Your spending is conservative, which is excellent! "
                    f"Consider investing {format_vnd(not_used * 0.2)} VND of your unallocated funds in a low-risk investment or emergency fund."
                )
            else:
                advice.append(
                    "Your spending appears balanced. Continue tracking expenses and consider setting specific savings goals."
                )

        return " ".join(advice) if advice else "No specific advice at this time. Keep managing your finances wisely!"