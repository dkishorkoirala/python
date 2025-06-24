expenses = []

def add_expense(amount, category):
    expenses.append({
        "amount": int(amount),
        "category": category
    })
    print(f"\nAdded: Rs.{int(amount)} for {category}")

def show_expenses():
    if not expenses:
        return "\nNo expenses yet!!"

    result = "\nAll Expenses:\n"
    total = 0
    for i in range(len(expenses)):
        amt = expenses[i]["amount"]
        cat = expenses[i]["category"]
        result += f"{i+1}. Rs. {amt} - {cat}\n"
        total += amt 

    result +=  f"\nTotal spent: rs.{int(total)}"
    return result
