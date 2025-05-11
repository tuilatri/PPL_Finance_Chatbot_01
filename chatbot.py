import os
import re
from antlr4 import *
from collections import defaultdict
from datetime import datetime
from CompiledFiles.FinanceLexer import FinanceLexer
from CompiledFiles.FinanceParser import FinanceParser

def format_vnd(amount):
    return f"{amount:,.0f}".replace(",", ".") + " VND"

def parse_command(command):
    input_stream = InputStream(command)
    lexer = FinanceLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FinanceParser(stream)
    tree = parser.command()
    return tree

def write_log(file_path, salary, categories, actions):
    total_allocated = sum(categories.values())
    not_used = salary - total_allocated

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"Salary: {format_vnd(salary)}\n")
        f.write(f"Not used (Salary - Total money for spending categories): {format_vnd(not_used)}\n")
        f.write("Spending categories:\n")
        for k, v in categories.items():
            f.write(f"- {k}: {format_vnd(v)}\n")
        f.write("\n--------------------Record Of Actions--------------------\n")
        for action in actions:
            f.write(action + "\n")

def reset_data():
    print("Resetting all data...")
    salary_input = input("Your new salary: ")
    salary = int(salary_input.replace(".", "").replace(",", "").replace("VND", "").strip())

    print("Your new spending categories:")
    raw_categories = input("Example: Renting (5.000.000 VND), Food (1.000.000 VND), ...\n> ")
    categories = defaultdict(float)

    for cat in re.findall(r'([A-Za-z]+)\s*\(([\d.]+)\s*VND\)', raw_categories):
        categories[cat[0]] = float(cat[1].replace(".", ""))

    actions = []
    write_log("finance_record.txt", salary, categories, actions)
    print("Reset complete and saved.")
    return salary, categories, actions

def main():
    print("Chatbot: Hello, User. I am here to help you on your finance.")
    salary_input = input("Your salary: ")
    salary = int(salary_input.replace(".", "").replace(",", "").replace("VND", "").strip())

    print("Your spending categories:")
    raw_categories = input("Example: Renting (5.000.000 VND), Food (1.000.000 VND), ...\n> ")
    categories = defaultdict(float)

    for cat in re.findall(r'([A-Za-z]+)\s*\(([\d.]+)\s*VND\)', raw_categories):
        categories[cat[0]] = float(cat[1].replace(".", ""))

    actions = []
    file_path = "finance_record.txt"
    write_log(file_path, salary, categories, actions)

    while True:
        cmd = input("Command: ")
        if cmd.lower() in ['exit', 'quit']:
            break

        try:
            tree = parse_command(cmd)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if hasattr(tree, 'addExpense') and tree.addExpense():  # Format: Food: Pizza (50.000 VND)
                cat = tree.addExpense().CATEGORY().getText()
                desc = tree.addExpense().DESCRIPTION().getText().strip()
                amt = float(tree.addExpense().AMOUNT().getText().replace(".", ""))

                if cat in categories and categories[cat] >= amt:
                    categories[cat] -= amt
                    action_msg = f"[{timestamp}] [{cat}] {desc} -{format_vnd(amt)} (Success)"
                    actions.append(action_msg)
                    print("Enough money. Proceeding.")
                else:
                    action_msg = f"[{timestamp}] [{cat}] {desc} -{format_vnd(amt)} (Insufficient)"
                    actions.append(action_msg)
                    print(f"Insufficient money in {cat}. Declining.")

            elif hasattr(tree, 'changeCategory') and tree.changeCategory():  # Format: Change Food (2.000.000 VND)
                change = tree.changeCategory().categoryChange()
                cat = change.CATEGORY().getText()
                new_amt = float(change.AMOUNT().getText().replace(".", ""))
                
                total_allocated = sum(categories.values())
                current_used = salary - total_allocated
                
                available_funds = current_used + categories.get(cat, 0)
                
                if new_amt <= available_funds:
                    old_amt = categories.get(cat, 0)
                    categories[cat] = new_amt
                    action_msg = f"[{timestamp}] [Change] {cat}: {format_vnd(old_amt)} → {format_vnd(new_amt)}"
                    actions.append(action_msg)
                    print("Proceeding!")
                else:
                    action_msg = f"[{timestamp}] [Change Failed] {cat} → {format_vnd(new_amt)} (Insufficient funds)"
                    actions.append(action_msg)
                    print("Declining! Not enough funds.")

            elif hasattr(tree, 'addCategory') and tree.addCategory():  # Format: Add Clothes (1.000.000 VND)
                change = tree.addCategory().categoryChange()
                cat = change.CATEGORY().getText()
                new_amt = float(change.AMOUNT().getText().replace(".", ""))
                
                total_allocated = sum(categories.values())
                current_used = salary - total_allocated
                
                if new_amt <= current_used and cat not in categories:
                    categories[cat] = new_amt
                    action_msg = f"[{timestamp}] [Add] {cat}: {format_vnd(new_amt)}"
                    actions.append(action_msg)
                    print("Proceeding!")
                else:
                    reason = "Category already exists" if cat in categories else "Insufficient funds"
                    action_msg = f"[{timestamp}] [Add Failed] {cat}: {format_vnd(new_amt)} ({reason})"
                    actions.append(action_msg)
                    print(f"Declining! {reason}.")

            elif hasattr(tree, 'deleteCategory') and tree.deleteCategory():  # Format: Delete Clothes
                cat = tree.deleteCategory().CATEGORY().getText()
                if cat in categories:
                    deleted_amt = categories[cat]
                    del categories[cat]
                    action_msg = f"[{timestamp}] [Delete] {cat} (Freed {format_vnd(deleted_amt)})"
                    actions.append(action_msg)
                    print(f"Deleted {cat} category. Freed {format_vnd(deleted_amt)}.")
                else:
                    action_msg = f"[{timestamp}] [Delete Failed] {cat} (Category not found)"
                    actions.append(action_msg)
                    print(f"Category {cat} not found.")

            elif hasattr(tree, 'resetCommand') and tree.resetCommand():  # Format: Reset
                salary, categories, actions = reset_data()

        except Exception as e:
            print("Invalid command. Please try again.")
            print(f"Error: {e}")

        write_log(file_path, salary, categories, actions)
        print("Update recorded.")

if __name__ == '__main__':
    main()