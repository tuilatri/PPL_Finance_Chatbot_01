import os
from antlr4 import *
from CompiledFiles.FinanceLexer import FinanceLexer
from CompiledFiles.FinanceParser import FinanceParser
from CompiledFiles.FinanceListener import FinanceListener

class FinanceChatbotListener(FinanceListener):
    def __init__(self):
        self.salary = 0.0
        self.categories = {}  # {category: amount}
        self.not_used = 0.0
        self.record_file = "finance_record.txt"
        self.initialize_record()

    def initialize_record(self):
        with open(self.record_file, 'w') as f:
            f.write("Salary: 0 VND\nNot used: 0 VND\nSpending categories: None\n")
            f.write("--------------------Record Of Actions--------------------\n")

    def update_record(self, action, status):
        with open(self.record_file, 'a') as f:
            f.write(f"{action} - {status}\n")
        self.write_header()

    def write_header(self):
        categories_str = ", ".join(f"{cat} ({self.format_currency(amt)} VND)" for cat, amt in self.categories.items())
        if not categories_str:
            categories_str = "None"
        with open(self.record_file, 'r') as f:
            lines = f.readlines()
        lines[0] = f"Salary: {self.format_currency(self.salary)} VND\n"
        lines[1] = f"Not used: {self.format_currency(self.not_used)} VND\n"
        lines[2] = f"Spending categories: {categories_str}\n"
        with open(self.record_file, 'w') as f:
            f.writelines(lines)

    def format_currency(self, amount):
        # Convert float to string with dots (e.g., 10000000 -> 10.000.000)
        parts = f"{int(amount)}"[::-1]
        formatted = ".".join(parts[i:i+3] for i in range(0, len(parts), 3))[::-1]
        return formatted

    def parse_currency(self, number_text):
        # Convert string like '10.000.000' to float
        return float(number_text.replace('.', ''))

    def enterSalaryInput(self, ctx):
        self.salary = self.parse_currency(ctx.NUMBER().getText())
        self.not_used = self.salary
        self.update_record(f"Set salary to {self.format_currency(self.salary)} VND", "Proceeding")
        print(f"Salary set to {self.format_currency(self.salary)} VND")

    def enterCategoriesInput(self, ctx):
        total_category_amount = 0.0
        new_categories = {}
        for cat_ctx in ctx.category():
            cat_name = cat_ctx.ID().getText()
            amount = self.parse_currency(cat_ctx.NUMBER().getText())
            if cat_name in new_categories or cat_name in self.categories:
                print(f"Declining: Category {cat_name} already exists")
                self.update_record(f"Add category {cat_name} ({self.format_currency(amount)} VND)", "Declining")
                continue
            new_categories[cat_name] = amount
            total_category_amount += amount

        if total_category_amount <= self.not_used:
            self.categories.update(new_categories)
            self.not_used -= total_category_amount
            for cat_name, amount in new_categories.items():
                print(f"Added category {cat_name} ({self.format_currency(amount)} VND)")
                self.update_record(f"Add category {cat_name} ({self.format_currency(amount)} VND)", "Proceeding")
        else:
            print("Declining: Insufficient funds for categories")
            self.update_record(f"Add categories", "Declining")
        self.write_header()

    def enterSpendCommand(self, ctx):
        cat_name = ctx.ID(0).getText()
        item = ctx.ID(1).getText()
        amount = self.parse_currency(ctx.NUMBER().getText())
        if cat_name in self.categories and self.categories[cat_name] >= amount:
            self.categories[cat_name] -= amount
            print("Enough Money, Proceeding")
            self.update_record(f"{cat_name}: {item} ({self.format_currency(amount)} VND)", "Proceeding")
        else:
            print("Insufficient Money, Declining")
            self.update_record(f"{cat_name}: {item} ({self.format_currency(amount)} VND)", "Declining")
        self.write_header()

    def enterChangeCommand(self, ctx):
        cat_name = ctx.ID().getText()
        new_amount = self.parse_currency(ctx.NUMBER().getText())
        if cat_name in self.categories:
            current_amount = self.categories[cat_name]
            delta = new_amount - current_amount
            if delta <= self.not_used:
                self.categories[cat_name] = new_amount
                self.not_used -= delta
                print("Proceeding!")
                self.update_record(f"Change {cat_name} ({self.format_currency(new_amount)} VND)", "Proceeding")
            else:
                print("Declining: Insufficient funds")
                self.update_record(f"Change {cat_name} ({self.format_currency(new_amount)} VND)", "Declining")
        else:
            print(f"Declining: Category {cat_name} does not exist")
            self.update_record(f"Change {cat_name} ({self.format_currency(new_amount)} VND)", "Declining")
        self.write_header()

    def enterAddCommand(self, ctx):
        cat_name = ctx.ID().getText()
        amount = self.parse_currency(ctx.NUMBER().getText())
        if cat_name not in self.categories and amount <= self.not_used:
            self.categories[cat_name] = amount
            self.not_used -= amount
            print("Proceeding!")
            self.update_record(f"Add {cat_name} ({self.format_currency(amount)} VND)", "Proceeding")
        else:
            print("Declining: Category exists or insufficient funds")
            self.update_record(f"Add {cat_name} ({self.format_currency(amount)} VND)", "Declining")
        self.write_header()

    def enterDeleteCommand(self, ctx):
        cat_name = ctx.ID().getText()
        if cat_name in self.categories:
            self.not_used += self.categories[cat_name]
            del self.categories[cat_name]
            print("Proceeding!")
            self.update_record(f"Delete {cat_name}", "Proceeding")
        else:
            print(f"Declining: Category {cat_name} does not exist")
            self.update_record(f"Delete {cat_name}", "Declining")
        self.write_header()

    def enterResetCommand(self, ctx):
        self.salary = 0.0
        self.categories = {}
        self.not_used = 0.0
        self.initialize_record()
        print("Reset successful!")
        self.update_record("Reset", "Proceeding")

def main():
    print("Hello, User. I am here to help you on your finance.")
    listener = FinanceChatbotListener()

    while True:
        try:
            print("Your salary (e.g., 10.000.000 VND): ", end="")
            salary_input = input().strip()
            if salary_input.lower() == "exit":
                break
            lexer = FinanceLexer(InputStream(salary_input))
            stream = CommonTokenStream(lexer)
            parser = FinanceParser(stream)
            tree = parser.salaryInput()
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
            break
        except Exception as e:
            print(f"Invalid input. Please use format like '10.000.000 VND'. Error: {e}")

    if listener.salary == 0.0:
        print("No salary set. Exiting.")
        return

    while True:
        try:
            print("Your spending categories (e.g., Renting (5.000.000 VND), Food (1.000.000 VND)): ", end="")
            categories_input = input().strip()
            if categories_input.lower() == "exit":
                break
            lexer = FinanceLexer(InputStream(categories_input))
            stream = CommonTokenStream(lexer)
            parser = FinanceParser(stream)
            tree = parser.categoriesInput()
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
            break
        except Exception as e:
            print(f"Invalid input. Please use format like 'Renting (5.000.000 VND), Food (1.000.000 VND)'. Error: {e}")

    while True:
        print("Command (e.g., Food: Milktea (50.000 VND), Change Food (1.000.000 VND), Add Clothes (1.000.000 VND), Delete Food, Reset, or exit): ", end="")
        command = input().strip()
        if command.lower() == "exit":
            break
        try:
            lexer = FinanceLexer(InputStream(command))
            stream = CommonTokenStream(lexer)
            parser = FinanceParser(stream)
            tree = parser.command()
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
        except Exception as e:
            print(f"Invalid command. Please use correct format. Error: {e}")
            listener.update_record(command, "Declining")

if __name__ == "__main__":
    main()