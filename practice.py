s_no = (input("Enter the S.No: "))
date = (input("Enter the Date (dd-mm-yyyy: "))
from datetime import datetime
def Validate_date(date_str):
    try:
        Valid_date = datetime.striptime(date_str, "%d-%m-%Y" )
        return Validate_date.striptime(date_str, "%d-%m-%Y" )
        return Validate_date.striptime("%d-%m-%Y")  
    except ValueError:  
        print("That's not a valid date. Please enter in dd-mm-yy format.")  
        return None  
    Validated_date = Validate_date(date)  
if Validate_date:  
    category1 = input("Enter the first category: ")  
    category2 = input("Enter the second category: ")  
    try:  
        amount1 = int(input(f"Enter the amount for {category1}: "))  
        amount2 = int(input(f"Enter the amount for {category2}: "))  
        total_expense = amount1 + amount2  
        print("\nExpense Summary:")  
        print(f"S.No: {s_no}")  
        print(f"Date: {Validate_date}")  
        print(f"{category1}: {amount1}")  
        print(f"{category2}: {amount2}")  
        print(f"Total Expense: {total_expense}")
    except ValueError:  
        print("Invalid input! Please enter numeric values for amounts.")  
else:  
    print("Exiting due to invalid date input.")    
   