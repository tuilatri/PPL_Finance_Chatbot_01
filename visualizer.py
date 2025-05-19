import matplotlib.pyplot as plt

def generate_spending_graph(spending):
    """Generate a pie chart of spending by category in a pop-up window with a legend."""
    categories = list(spending.keys())
    amounts = list(spending.values())
    
    # Create pie chart with larger size
    plt.figure(figsize=(6, 4))
    plt.pie(amounts, labels=None, autopct='%1.1f%%', startangle=140, textprops={'color': 'white', 'fontsize': 12})
    plt.title('Spending by Category (VND)')
    
    # Add legend
    plt.legend(categories, title="Categories", loc="center left", bbox_to_anchor=(1, 0.5))
    
    # Adjust layout to prevent legend clipping
    plt.tight_layout()
    
    # Display in pop-up window
    plt.show()