import os
import re
from antlr4 import *
from antlr4.error.Errors import RecognitionException
from collections import defaultdict
from datetime import datetime
from CompiledFiles.FinanceLexer import FinanceLexer
from CompiledFiles.FinanceParser import FinanceParser

def format_vnd(amount):
    return f"{amount:,.0f}".replace(",", ".") + " VND"

def parse_command(command):
    # Normalize spaces around VND and strip leading/trailing spaces
    command = re.sub(r'\s*VND\s*', 'VND', command.strip())
    input_stream = InputStream(command)
    lexer = FinanceLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FinanceParser(stream)
    parser.removeErrorListeners()  # Remove default console error listener
    parser.addErrorListener(DiagnosticErrorListener())  # Detailed error reporting
    try:
        tree = parser.command()
        return tree
    except RecognitionException as e:
        raise RecognitionException(f"Parsing failed: {str(e)}", None, input_stream, None)

def write_log(file_path, salary, initial_allocated, categories, display_names, actions):
    not_used = salary - initial_allocated
    if not_used < 0:
        print("Warning: Negative 'Not used' detected. Check category allocations.")
        not_used = 0
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"Salary: {format_vnd(salary)}\n")
        f.write(f"Not used (Salary - Total money for spending categories): {format_vnd(not_used)}\n")
        f.write("Spending categories:\n")
        if not categories:
            f.write("(None)\n")
        else:
            for k in sorted(categories.keys()):
                f.write(f"- {display_names.get(k, k)}: {format_vnd(categories[k])}\n")
        f.write("\n--------------------Record Of Actions--------------------\n")
        for action in actions:
            f.write(action + "\n")

def validate_vnd_format(value, field="amount"):
    if not re.match(r'^\d+(\.\d{3})*(\s*VND)?$', value.strip()):
        print(f"Invalid {field} format. Use e.g., 1.000.000 VND.")
        return False
    return True

def parse_vnd(value):
    return int(value.replace(".", "").replace("VND", "").strip())

def reset_data():
    print("Resetting all data...")
    while True:
        salary_input = input("Your new salary: ")
        if not validate_vnd_format(salary_input, "salary"):
            continue
        salary = parse_vnd(salary_input)
        if salary <= 0:
            print("Error: Salary must be positive.")
            continue
        break

    print("Your new spending categories (e.g., Renting (5.000.000 VND), Food (1.000.000 VND), ...):")
    categories = defaultdict(float)
    display_names = {}
    while True:
        raw_categories = input("> ")
        if not raw_categories.strip():
            print("Error: At least one category required.")
            continue
        valid = True
        categories.clear()
        display_names.clear()
        matches = re.findall(r'([A-Za-z][A-Za-z0-9_]*)\s*\(([\d.]+)\s*VND\)', raw_categories, re.IGNORECASE)
        if not matches:
            print("Error: No valid categories found. Use format: Renting (5.000.000 VND), Food (1.000.000 VND)")
            continue
        for cat, amt in matches:
            if cat.lower() in ['change', 'add', 'delete', 'reset']:
                print(f"Error: Category name '{cat}' is a reserved keyword.")
                valid = False
                break
            if not re.match(r'^\d+(\.\d{3})*$', amt):
                print(f"Invalid amount format for {cat}. Use e.g., 1.000.000.")
                valid = False
                break
            amount = parse_vnd(amt + "VND")
            if amount <= 0:
                print(f"Error: Amount for {cat} must be positive.")
                valid = False
                break
            categories[cat.lower()] = amount
            display_names[cat.lower()] = cat
        if not valid:
            continue
        total_allocated = sum(categories.values())
        if total_allocated > salary:
            print("Error: Total category allocation exceeds salary.")
            continue
        break

    actions = []
    initial_allocated = total_allocated
    print(f"DEBUG: Categories defined: {list(display_names.values())}")
    write_log("finance_record.txt", salary, initial_allocated, categories, display_names, actions)
    print("Reset complete and saved.")
    return salary, initial_allocated, categories, display_names, actions

def main():
    print("Chatbot: Hello, User. I am here to help you on your finance.")
    while True:
        salary_input = input("Your salary: ")
        if not validate_vnd_format(salary_input, "salary"):
            continue
        salary = parse_vnd(salary_input)
        if salary <= 0:
            print("Error: Salary must be positive.")
            continue
        break

    print("Your new spending categories (e.g., Renting (5.000.000 VND), Food (1.000.000 VND), ...):")
    categories = defaultdict(float)
    display_names = {}
    while True:
        raw_categories = input("> ")
        if not raw_categories.strip():
            print("Error: At least one category required.")
            continue
        valid = True
        categories.clear()
        display_names.clear()
        matches = re.findall(r'([A-Za-z][A-Za-z0-9_]*)\s*\(([\d.]+)\s*VND\)', raw_categories, re.IGNORECASE)
        if not matches:
            print("Error: No valid categories found. Use format: Renting (5.000.000 VND), Food (1.000.000 VND)")
            continue
        for cat, amt in matches:
            if cat.lower() in ['change', 'add', 'delete', 'reset']:
                print(f"Error: Category name '{cat}' is a reserved keyword.")
                valid = False
                break
            if not re.match(r'^\d+(\.\d{3})*$', amt):
                print(f"Invalid amount format for {cat}. Use e.g., 1.000.000.")
                valid = False
                break
            amount = parse_vnd(amt + "VND")
            if amount <= 0:
                print(f"Error: Amount for {cat} must be positive.")
                valid = False
                break
            categories[cat.lower()] = amount
            display_names[cat.lower()] = cat
        if not valid:
            continue
        total_allocated = sum(categories.values())
        if total_allocated > salary:
            print("Error: Total category allocation exceeds salary.")
            continue
        break

    actions = []
    initial_allocated = total_allocated
    file_path = "finance_record.txt"
    print(f"DEBUG: Categories defined: {list(display_names.values())}")
    write_log(file_path, salary, initial_allocated, categories, display_names, actions)

    while True:
        cmd = input("Command: ")
        if cmd.lower() in ['exit', 'quit']:
            break

        try:
            print(f"DEBUG: Processing command: {cmd}")
            print(f"DEBUG: Current categories: {list(display_names.values())}")
            tree = parse_command(cmd)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if hasattr(tree, 'addExpense') and tree.addExpense():
                cat = tree.addExpense().CATEGORY().getText().lower()
                desc = tree.addExpense().DESCRIPTION().getText().strip()
                amt_text = tree.addExpense().AMOUNT().getText()
                if not re.match(r'^\d+(\.\d{3})*$', amt_text):
                    print("Invalid amount format. Use e.g., 50.000.")
                    continue
                amt = float(amt_text.replace(".", ""))
                if amt <= 0:
                    print("Error: Expense amount must be positive.")
                    continue

                print(f"DEBUG: Checking category {cat} with balance {categories.get(cat, 0)}")
                if cat in categories and categories[cat] >= amt:
                    categories[cat] -= amt
                    action_msg = f"[{timestamp}] [{display_names.get(cat, cat)}] {desc} -{format_vnd(amt)} (Success)"
                    actions.append(action_msg)
                    print("Enough money. Proceeding.")
                else:
                    action_msg = f"[{timestamp}] [{display_names.get(cat, cat)}] {desc} -{format_vnd(amt)} (Insufficient)"
                    actions.append(action_msg)
                    print(f"Insufficient money in {display_names.get(cat, cat)}. Declining.")

            elif hasattr(tree, 'changeCategory') and tree.changeCategory():
                cat = tree.changeCategory().CATEGORY().getText().lower()
                amt_text = tree.changeCategory().AMOUNT().getText()
                if not re.match(r'^\d+(\.\d{3})*$', amt_text):
                    print("Invalid amount format. Use e.g., 1.000.000.")
                    continue
                new_amt = float(amt_text.replace(".", ""))
                if new_amt <= 0:
                    print("Error: Category amount must be positive.")
                    continue

                total_allocated = sum(categories.values())
                current_used = salary - total_allocated
                available_funds = current_used + categories.get(cat, 0)

                print(f"DEBUG: Changing {cat} to {new_amt}. Available funds: {available_funds}")
                if new_amt <= available_funds:
                    old_amt = categories.get(cat, 0)
                    categories[cat] = new_amt
                    initial_allocated += new_amt - old_amt
                    action_msg = f"[{timestamp}] [Change] {display_names.get(cat, cat)}: {format_vnd(old_amt)} → {format_vnd(new_amt)}"
                    actions.append(action_msg)
                    print("Proceeding!")
                else:
                    action_msg = f"[{timestamp}] [Change Failed] {display_names.get(cat, cat)} → {format_vnd(new_amt)} (Insufficient funds)"
                    actions.append(action_msg)
                    print("Declining! Not enough funds.")

            elif hasattr(tree, 'addCategory') and tree.addCategory():
                cat = tree.addCategory().CATEGORY().getText()
                cat_lower = cat.lower()
                amt_text = tree.addCategory().AMOUNT().getText()
                if not re.match(r'^\d+(\.\d{3})*$', amt_text):
                    print("Invalid amount format. Use e.g., 1.000.000.")
                    continue
                new_amt = float(amt_text.replace(".", ""))
                if new_amt <= 0:
                    print("Error: Category amount must be positive.")
                    continue

                total_allocated = sum(categories.values())
                current_used = salary - total_allocated

                print(f"DEBUG: Adding {cat} with {new_amt}. Available funds: {current_used}")
                if new_amt <= current_used and cat_lower not in categories:
                    categories[cat_lower] = new_amt
                    display_names[cat_lower] = cat
                    initial_allocated += new_amt
                    action_msg = f"[{timestamp}] [Add] {cat}: {format_vnd(new_amt)}"
                    actions.append(action_msg)
                    print("Proceeding!")
                else:
                    reason = "Category already exists" if cat_lower in categories else "Insufficient funds"
                    action_msg = f"[{timestamp}] [Add Failed] {cat}: {format_vnd(new_amt)} ({reason})"
                    actions.append(action_msg)
                    print(f"Declining! {reason}.")

            elif hasattr(tree, 'deleteCategory') and tree.deleteCategory():
                cat = tree.deleteCategory().CATEGORY().getText().lower()
                print(f"DEBUG: Deleting {cat}")
                if cat in categories:
                    deleted_amt = categories[cat]
                    initial_allocated -= deleted_amt
                    display_name = display_names.get(cat, cat)
                    del categories[cat]
                    del display_names[cat]
                    action_msg = f"[{timestamp}] [Delete] {display_name} (Freed {format_vnd(deleted_amt)})"
                    actions.append(action_msg)
                    print(f"Deleted {display_name} category. Freed {format_vnd(deleted_amt)}.")
                else:
                    action_msg = f"[{timestamp}] [Delete Failed] {cat} (Category not found)"
                    actions.append(action_msg)
                    print(f"Category {cat} not found.")

            elif hasattr(tree, 'resetCommand') and tree.resetCommand():
                salary, initial_allocated, categories, display_names, actions = reset_data()

        except RecognitionException as e:
            print(f"Invalid command syntax: {str(e)}. Expected formats: Food: Item (50.000 VND), Change Food (1.000.000 VND), Add Clothes (1.000.000 VND), Delete Food, Reset")
        except Exception as e:
            print(f"Unexpected error: {e}. Please check command syntax.")

        write_log(file_path, salary, initial_allocated, categories, display_names, actions)
        print("Update recorded.")

if __name__ == '__main__':
    main()