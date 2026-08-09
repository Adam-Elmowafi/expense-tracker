expense = [
    {"category": "Food", "amount": 150, "date": "2024-01-15"},
    {"category": "Transport", "amount": 50, "date": "2024-01-15"},
    {"category": "Entertainment", "amount": 200, "date": "2024-01-14"},
    {"category": "Food", "amount": 100, "date": "2024-01-13"}
]

def add_expense():
    category=input("Enter the category : ")
    amount=int(input("What is the amount: "))
    date=input("Enter the date : ")
    expense_dict ={
        "category":category,
        "amount":amount,
        "date":date
    }
    expense.append(expense_dict)

def show_expenses():
    for item in expense:
        print(item)

def show_total():
    total=0
    for items in expense:
        sum=items.get("amount")
        total+=sum
    print(f"The total is {total}")       

def show_by_category():
    category=input("Enter the category : ")
    for items in expense:
        if items["category"] == category:
            print(items)

def delete_expense():
    for items in expense:
            print(items.get("amount"))
    choice = int(input("Enter expense number: "))
    item = expense[choice - 1] 
    expense.remove(item)

def exit():
    print("End of the program")   



while True:
    print("===== Expense Tracker =====")
    print("""1. Add Expense
2. Show Expenses
3. Show Total
4. Show by Category
5. Delete Expense
6. Exit""")
    
    goal = input("Choose an Operation: ").strip().title()
    
    if goal == "Add Expense":
        add_expense()
    elif goal == "Show Expenses":
        show_expenses()
    elif goal == "Show Total":
        show_total()
    elif goal == "Show By Category":
        show_by_category()
    elif goal == "Delete Expense":
        delete_expense()
    elif goal == "Exit":
        print("End of the program")
        break  

