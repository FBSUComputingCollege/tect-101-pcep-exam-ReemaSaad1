# Function to add expenses for the day
def add_expenses(expenses_dict):
    date = input("Enter the date (YYYY-MM-DD): ")
    expenses = float(input("Enter the total expenses for the day: $"))
    expenses_dict[date] = expenses
    print("Expenses added successfully!")

# Function to view expenses for each day and overall total
def view_expenses(expenses_dict):
    if not expenses_dict:
        print("No expenses recorded yet.")
        return
    
    print("\nExpense Summary:")
    total_expenses = 0
    for date, expenses in expenses_dict.items():
        print(f"{date}: ${expenses:.2f}")
        total_expenses += expenses
    print(f"Overall Total Expenses: ${total_expenses:.2f}")

# Function to save expense data to a file
def save_to_file(expenses_dict):
    filename = "expenses.txt"
    with open(filename, "w") as file:
        for date, expenses in expenses_dict.items():
            file.write(f"{date}: {expenses:.2f}\n")
    print(f"Expense data saved to {filename}")

# Main function
def main():
    expenses_dict = {}
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Save to File")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_expenses(expenses_dict)
        elif choice == "2":
            view_expenses(expenses_dict)
        elif choice == "3":
            save_to_file(expenses_dict)
        elif choice == "4":
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()