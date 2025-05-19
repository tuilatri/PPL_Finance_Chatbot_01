import re

def format_vnd(amount):
    """Format a number in Vietnamese VND format with dots (e.g., 10000000 -> 10.000.000)."""
    amount_str = str(amount)
    length = len(amount_str)
    if length <= 3:
        return amount_str
    
    result = []
    for i in range(length - 1, -1, -1):
        result.insert(0, amount_str[i])
        if i > 0 and (length - i) % 3 == 0:
            result.insert(0, '.')
    
    return ''.join(result)

def read_finance_data(filename):
    """Read finance data from file."""
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        data = {"salary": 0, "not_used": 0, "categories": {}, "actions": []}
        
        section = None
        for line in lines:
            line = line.strip()
            if line.startswith("Salary:"):
                data["salary"] = int(line.split(":")[1].strip().replace('.', '').replace(' VND', ''))
            elif line.startswith("Not used:"):
                data["not_used"] = int(line.split(":")[1].strip().replace('.', '').replace(' VND', ''))
            elif line.startswith("Spending categories:"):
                section = "categories"
            elif line.startswith("--------------------Record Of Actions--------------------"):
                section = "actions"
            elif section == "categories" and line and not line.startswith("-"):
                parts = line.split(":")
                if len(parts) == 2:
                    category, amount = parts
                    data["categories"][category.strip()] = int(amount.strip().replace('.', '').replace(' VND', ''))
            elif section == "actions" and line:
                data["actions"].append({"description": line})
        
        return data
    except FileNotFoundError:
        return {"salary": 0, "not_used": 0, "categories": {}, "actions": []}

def write_finance_data(filename, data):
    """Write finance data to file with VND formatting and currency."""
    with open(filename, 'w') as f:
        f.write(f"Salary: {format_vnd(data['salary'])} VND\n")
        f.write(f"Not used: {format_vnd(data['not_used'])} VND\n")
        f.write("Spending categories:\n")
        for category, amount in data["categories"].items():
            f.write(f"{category.capitalize()}: {format_vnd(amount)} VND\n")
        f.write("--------------------Record Of Actions--------------------\n")
        for action in data["actions"]:
            description = action['description']
            # Format amounts directly from action data
            if 'Set salary' in description and 'amount' in action:
                description = f"Set salary to {format_vnd(action['amount'])} VND"
            elif 'Added categories' in description and 'categories' in action:
                formatted_list = [(cat.capitalize(), f"{format_vnd(amount)} VND") for cat, amount in action['categories']]
                description = f"Added categories: {formatted_list}"
            elif 'Spent' in description and 'amount' in action:
                description = f"Spent {format_vnd(action['amount'])} VND on {action.get('item', '')} in {action.get('category', '').capitalize()}"
            f.write(f"{description}\n")

def check_funds(category_amount, spend_amount):
    """Check if there are sufficient funds in the category."""
    return category_amount >= spend_amount

def check_unallocated(not_used, amount):
    """Check if there is enough unallocated money."""
    return not_used >= amount