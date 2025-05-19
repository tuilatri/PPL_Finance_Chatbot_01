from utils import read_finance_data, write_finance_data, check_funds, check_unallocated
from parser import FinanceParser

def run():
    finance_file = "finance_record.txt"
    # Initialize fresh data to reset finance_record.txt
    data = {"salary": 0, "not_used": 0, "categories": {}, "actions": []}
    write_finance_data(finance_file, data)
    
    print("Hello, User. I am your finance chatbot. What can I do for you today?")
    parser = FinanceParser()
    
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
                    salary = intent['amount']
                    data['salary'] = salary
                    data['not_used'] = salary
                    data['categories'] = {}
                    data['actions'].append({
                        'description': f"Set salary",
                        'amount': salary
                    })
                    write_finance_data(finance_file, data)
                    print(f"Chatbot: Salary set to {salary} VND. Please specify spending categories.")
                
                elif intent['type'] == 'category':
                    total_category_amount = sum(amount for _, amount in intent['categories'])
                    if check_unallocated(data['not_used'], total_category_amount):
                        for category, amount in intent['categories']:
                            # Update existing category or add new one
                            category = category.capitalize()
                            if category in data['categories']:
                                data['categories'][category] += amount
                            else:
                                data['categories'][category] = amount
                            data['not_used'] -= amount
                        data['actions'].append({
                            'description': f"Added categories",
                            'categories': [(cat.capitalize(), amt) for cat, amt in intent['categories']]
                        })
                        write_finance_data(finance_file, data)
                        print(f"Chatbot: Categories added. Unallocated money: {data['not_used']} VND")
                    else:
                        print("Chatbot: Not enough unallocated money to add these categories.")
                
                elif intent['type'] == 'spend':
                    amount = intent['amount']
                    item = intent['item']
                    category = intent['category'].capitalize()
                    if category in data['categories'] and check_funds(data['categories'][category], amount):
                        data['categories'][category] -= amount
                        data['actions'].append({
                            'description': f"Spent",
                            'amount': amount,
                            'item': item,
                            'category': category
                        })
                        write_finance_data(finance_file, data)
                        print(f"Chatbot: Enough money. Proceeding with {item} for {amount} VND.")
                    else:
                        print(f"Chatbot: Insufficient funds in {category} or category does not exist.")
                
                elif intent['type'] == 'modify_category':
                    category = intent['category'].capitalize()
                    new_amount = intent['amount']
                    if category in data['categories']:
                        old_amount = data['categories'][category]
                        data['not_used'] += old_amount
                        if check_unallocated(data['not_used'], new_amount):
                            data['categories'][category] = new_amount
                            data['not_used'] -= new_amount
                            data['actions'].append({
                                'description': f"Modified {category}",
                                'category': category,
                                'amount': new_amount
                            })
                            write_finance_data(finance_file, data)
                            print(f"Chatbot: Category {category} modified to {new_amount} VND.")
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
        
        except Exception as e:
            print(f"Chatbot: Error processing input: {str(e)}")