s_no = (input("Enter the S.No: "))
date = input("Enter the Date: ")
def validate_date(date_str):
    try:
        valid_date = datetime.strptime(date_str,"%d-%m-%y")
        print("Great! you entered a valid date:",
        valid_date.strftime("%d-%M-%Y"))
    except ValueError:
        print("That's not a real date please try again.")
category1 = input("Enter the first category: ")
category2 = input("Enter the second category: ")
try:
    amount1 = int(input(f"Enter the amount for {category1}: "))
    amount2 = int(input(f"Enter the amount for {category2}: "))
    total_expense = amount1 + amount2 
    print("\nExpense Summary:")
    print(f"S.No: {s_no}")
    print(f"Date: {date}")
    print(f"{category1}: {amount1}")
    print(f"{category2}: {amount2}")
    print(f"Total Expense: {total_expense}")
except ValueError:
    print("Invalid input! Please enter numeric values for amounts.")
    print(s_no, date, category1, category2)