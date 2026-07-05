import csv
from datetime import datetime
import os

FILE_NAME = "expense_data.csv"

# Create file if it does not exist
if not os.path.exists(FILE_NAME):
    file = open(FILE_NAME, "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["Item", "Amount", "Category", "Date"])
    file.close()


def add_expense():
    item = input("Enter Expense Name: ")
    amount = int(input("Enter Amount: "))
    category = input("Enter Category (Food/Travel/Shopping): ")

    date = datetime.now().strftime("%Y-%m-%d")

    file = open(FILE_NAME, "a", newline="")
    writer = csv.writer(file)
    writer.writerow([item, amount, category, date])
    file.close()

    print("Expense Added Successfully.")


def view_expenses():
    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    next(reader)

    print("\n------ Expense List ------")
    found = False

    for row in reader:
        found = True
        print("Item:", row[0])
        print("Amount:", row[1])
        print("Category:", row[2])
        print("Date:", row[3])
        print("-------------------------")

    if not found:
        print("No Expense Found")

    file.close()


def search_category():
    search = input("Enter Category: ")

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    next(reader)

    found = False

    print("\nSearch Result")

    for row in reader:
        if row[2].lower() == search.lower():
            found = True
            print(row)

    if not found:
        print("No Expense Found")

    file.close()


def category_total():
    category = input("Enter Category: ")

    total = 0

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        if row[2].lower() == category.lower():
            total = total + int(row[1])

    file.close()

    print("Total", category, "Expense =", total)


def monthly_total():
    month = input("Enter Month (YYYY-MM): ")

    total = 0

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        if row[3].startswith(month):
            total = total + int(row[1])

    file.close()

    print("Monthly Expense =", total)


while True:

    print("\n====== Expense Tracker 2.0 ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search by Category")
    print("4. Category Total")
    print("5. Monthly Total")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        search_category()

    elif choice == "4":
        category_total()

    elif choice == "5":
        monthly_total()

    elif choice == "6":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")