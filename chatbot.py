import os
import re
from CompiledFiles.FinanceLexer import FinanceLexer
from CompiledFiles.FinanceParser import FinanceParser
from antlr4 import *
from collections import defaultdict

def parse_command(command):
    input_stream = InputStream(command)
    lexer = FinanceLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FinanceParser(stream)
    tree = parser.command()
    return tree

def write_log(file_path, salary, categories, actions):
    total_spent = sum(categories.values())
    not_used = salary - total_spent

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"Salary: {salary:,.0f} VND\n")
        f.write(f"# Not used (Salary - Total money for spending categories): {not_used:,.0f} VND\n")
        f.write("Spending categories:\n")
        for k, v in categories.items():
            f.write(f"- {k}: {v:,.0f} VND\n")
        f.write("\n--------------------Record Of Actions--------------------\n")
        for action in actions:
            f.write(action + "\n")
            
def main():
    print("Hello, User. I am here to help you on your finance.")
    salary_input = input("Your salary: ")
    salary = int(salary_input.replace(".", "").replace(",", "").replace("VND", "").strip())
    
    print("Your spending categories:")
    raw_categories = input("Example: Renting (5.000.000 VND), Food (1.000.000 VND), ...\n> ")
    categories = defaultdict(float)

    for cat in re.findall(r'([A-Za-z]+)\s*\(([\d.]+)\s*VND\)', raw_categories):
        categories[cat[0]] = float(cat[1].replace(".", ""))

    actions = []
    file_path = "finance_record.txt"

    while True:
        cmd = input("Command: ")
        if cmd.lower() in ['exit', 'quit']:
            break

        try:
            tree = parse_command(cmd)
            if tree.addExpense():
                cat = tree.addExpense().CATEGORY().getText()
                desc = tree.addExpense().description().getText().strip()
                amt = float(tree.addExpense().AMOUNT().getText().replace(".", ""))

                if cat in categories and categories[cat] >= amt:
                    categories[cat] -= amt
                    actions.append(f"[{cat}] {desc} -{amt:,.0f} VND")
                else:
                    print(f"Not enough money in {cat} category.")

            elif tree.changeCategory():
                changes = tree.changeCategory().categoryChangeList().categoryChange()
                total_available = sum(categories.values())
                for change in changes:
                    cat = change.CATEGORY().getText()
                    amt = float(change.AMOUNT().getText().replace(".", ""))

                    if amt > total_available:
                        print(f"Invalid since the money is not enough.")
                        break

                    old = categories.get(cat, 0)
                    categories[cat] = amt
                    actions.append(f"[Change] {cat}: {old:,.0f} VND → {amt:,.0f} VND")
                    total_available -= amt

        except Exception as e:
            print("Invalid command. Please try again.")
            print(f"Error: {e}")

        write_log(file_path, salary, categories, actions)
        print("Update recorded.")

if __name__ == '__main__':
    main()
