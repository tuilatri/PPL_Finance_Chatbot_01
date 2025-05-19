from utils import read_finance_data, write_finance_data, check_funds, check_unallocated, convert_to_vnd, get_spending_by_category
from parser import FinanceParser
from advisor import Advisor
from visualizer import generate_spending_graph

def run():
    finance_file = "finance_record.txt"
    # Initialize fresh data to reset finance_record.txt
    data = {"salary": 0, "not_used": 0, "categories": {}, "actions": []}
    write_finance_data(finance_file, data)
    
    print("Hello, User. I am your finance chatbot. What can I do for you today?")
    parser = FinanceParser()
    advisor = Advisor()
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['exit', 'quit']:
            break
        
        # Keep original input for case preservation, parse lowercase
        parse_input = user_input.lower()
        try:
            intents = parser.parse(parse_input)
            for intent in intents:
                if intent['type'] == 'salary':
                    original_amount = intent['amount']
                    currency = intent['currency']
                    salary = int(convert_to_vnd(original_amount, currency))
                    data['salary'] += salary
                    data['not_used'] += salary
                    data['actions'].append({
                        'description': f"Added salary",
                        'amount': salary,
                        'original_amount': original_amount,
                        'currency': currency
                    })
                    write_finance_data(finance_file, data)
                    print(f"Chatbot: Added {salary} VND ({original_amount} {currency.upper()}) to salary. Total salary: {data['salary']} VND. Please specify spending categories.")
                
                elif intent['type'] == 'category':
                    categories_vnd = []
                    total_category_amount = 0
                    for category, amount, orig_amount, currency in intent['categories']:
                        amount_vnd = int(convert_to_vnd(amount, currency))
                        categories_vnd.append((category, amount_vnd, orig_amount, currency))
                        total_category_amount += amount_vnd
                    if check_unallocated(data['not_used'], total_category_amount):
                        for category, amount_vnd, orig_amount, currency in categories_vnd:
                            category = category.capitalize()
                            if category in data['categories']:
                                data['categories'][category] += amount_vnd
                            else:
                                data['categories'][category] = amount_vnd
                            data['not_used'] -= amount_vnd
                        data['actions'].append({
                            'description': f"Added categories",
                            'categories': [(cat, amt, orig_amt, curr) for cat, amt, orig_amt, curr in categories_vnd]
                        })
                        write_finance_data(finance_file, data)
                        print(f"Chatbot: Categories added. Unallocated money: {data['not_used']} VND")
                    else:
                        print("Chatbot: Not enough unallocated money to add these categories.")
                
                elif intent['type'] == 'spend':
                    original_amount = intent['amount']
                    currency = intent['currency']
                    amount_vnd = int(convert_to_vnd(original_amount, currency))
                    item = intent['item']
                    category = intent['category'].capitalize()
                    if category in data['categories'] and check_funds(data['categories'][category], amount_vnd):
                        data['categories'][category] -= amount_vnd
                        data['actions'].append({
                            'description': f"Spent",
                            'amount': amount_vnd,
                            'original_amount': original_amount,
                            'currency': currency,
                            'item': item,
                            'category': category
                        })
                        write_finance_data(finance_file, data)
                        print(f"Chatbot: Enough money. Proceeding with {item} for {amount_vnd} VND ({original_amount} {currency.upper()}).")
                    else:
                        print(f"Chatbot: Insufficient funds in {category} or category does not exist.")
                
                elif intent['type'] == 'modify_category':
                    category = intent['category'].capitalize()
                    original_amount = intent['amount']
                    currency = intent['currency']
                    new_amount_vnd = int(convert_to_vnd(original_amount, currency))
                    if category in data['categories']:
                        old_amount = data['categories'][category]
                        data['not_used'] += old_amount
                        if check_unallocated(data['not_used'], new_amount_vnd):
                            data['categories'][category] = new_amount_vnd
                            data['not_used'] -= new_amount_vnd
                            data['actions'].append({
                                'description': f"Modified {category}",
                                'category': category,
                                'amount': new_amount_vnd,
                                'original_amount': original_amount,
                                'currency': currency
                            })
                            write_finance_data(finance_file, data)
                            print(f"Chatbot: Category {category} modified to {new_amount_vnd} VND ({original_amount} {currency.upper()}).")
                        else:
                            data['not_used'] -= old_amount
                            print("Chatbot: Not enough unallocated money to modify category.")
                    else:
                        print(f"Chatbot: Category {category} does not exist.")
                
                elif intent['type'] == 'delete_category':
                    category = intent['category'].capitalize()
                    if category in data['categories']:
                        amount = data['categories'][category]
                        data['not_used'] += amount
                        del data['categories'][category]
                        data['actions'].append({
                            'description': f"Deleted category {category}",
                            'category': category
                        })
                        write_finance_data(finance_file, data)
                        print(f"Chatbot: Category {category} deleted.")
                    else:
                        print(f"Chatbot: Category {category} does not exist.")
                
                elif intent['type'] == 'reset':
                    data = {"salary": 0, "not_used": 0, "categories": {}, "actions": []}
                    write_finance_data(finance_file, data)
                    print("Chatbot: All data reset.")
                
                elif intent['type'] == 'analyze':
                    advice = advisor.generate_advice(data)
                    data['actions'].append({
                        'description': f"Provided advice",
                        'advice': advice
                    })
                    write_finance_data(finance_file, data)
                    print(f"Chatbot: {advice}")
                
                elif intent['type'] == 'graph':
                    spending = get_spending_by_category(data)
                    if spending:
                        generate_spending_graph(spending)
                        data['actions'].append({
                            'description': f"Displayed spending graph"
                        })
                        write_finance_data(finance_file, data)
                        print(f"Chatbot: Displaying spending graph for your categories.")
                    else:
                        print(f"Chatbot: No spending data to graph yet.")
        
        except Exception as e:
            print(f"Chatbot: Error processing input: {str(e)}")