class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=""):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        return self.balance
    
    def check_funds(self, amount):
        return amount <= self.balance

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def transfer(self, amount, instance):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({'amount': -amount, 'description': "Transfer to " + instance.category})
            instance.balance += amount
            instance.ledger.append({'amount': amount, 'description': "Transfer from " + self.category})
            return True
        return False

    def __str__(self):
        title = f"{self.category:*^30}"
        items = "\n".join([f"{item['description'][:23]:23}{item['amount']:>7.2f}" for item in self.ledger])
        total = f"Total: {self.balance:.2f}"
        return f"{title}\n{items}\n{total}"


def create_spend_chart(categories):
    
    total_withdrawals = {category.category: sum(transaction['amount'] for transaction in category.ledger if transaction['amount'] < 0) for category in categories}
    max_name_length = max(len(category.category) for category in categories)

    
    total_spent = sum(total_withdrawals.values())
    percentages = [(withdrawals * 100 // total_spent) // 10 * 10 for withdrawals in total_withdrawals.values()]

    
    chart = "Percentage spent by category\n"
    for percentage in reversed(range(0, 110, 10)):
        chart += f"{percentage:3}| "
        for p in percentages:
            chart += "o  " if p >= percentage else "   "
        chart += "\n"

    
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            name = category.category
            chart += name[i] + "  " if i < len(name) else "   "
        if i < max_name_length - 1:  
            chart += "\n"

    return chart