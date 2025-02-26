from pymongo import MongoClient
import certifi
import time  # Import the time module to use time.sleep()
import os
from dotenv import load_dotenv

## LOCAL HELPER FUNCTIONS
## -----------------------------------------------------
from Functions.define_categories import DefineCategories  # Import the function from define_categories.py
from Functions.define_Budgets import defineBudgets 
from Functions.main_menu import MainMenu
from Functions.print_budgets import PrintBudget
from Functions.default_categories import DefaultCategories
from Functions.addExpense.add_Expense import addExpense
from Functions.viewExpenses.view_expenses import viewExpenses
## -----------------------------------------------------

# Load environment variables from .env file
load_dotenv()

first_login = False

# Access environment variables
database_url = os.getenv("MONGO_DB_URL")

# Connect to MongoDB database
client = MongoClient(
    database_url,
    tlsCAFile=certifi.where() ) 

db = client['budgetingApp']  # Replace with your database name
users  = db['users']  

# Create a new document to insert into the collection 

# Check if John Doe is already registered
document = users.find_one({"Name": "John Doe"})
if document:
    print("Document found:", document)
if not document:
    print("No document found with Name: 'John Doe'")
    new_document = {
    "Name": "John Doe", 
    "user_id": "user123",    
    }
    result = users.insert_one(new_document)
    document = users.find_one({"Name": "John Doe"})
    first_login = True



print("Welcome to")
print("▗▖ ▗▖ ▗▄▖▗▄▄▄▖▗▄▄▖▗▖ ▗▖    ▗▖  ▗▖▗▖  ▗▖    ▗▄▄▖ ▗▖ ▗▖▗▄▄▄  ▗▄▄▖▗▄▄▄▖▗▄▄▄▖\n"
      "▐▌ ▐▌▐▌ ▐▌ █ ▐▌   ▐▌ ▐▌    ▐▛▚▞▜▌ ▝▚▞▘     ▐▌ ▐▌▐▌ ▐▌▐▌  █▐▌   ▐▌     █  \n"
      "▐▌ ▐▌▐▛▀▜▌ █ ▐▌   ▐▛▀▜▌    ▐▌  ▐▌  ▐▌      ▐▛▀▚▖▐▌ ▐▌▐▌  █▐▌▝▜▌▐▛▀▀▘  █  \n"
      "▐▙█▟▌▐▌ ▐▌ █ ▝▚▄▄▖▐▌ ▐▌    ▐▌  ▐▌  ▐▌      ▐▙▄▞▘▝▚▄▞▘▐▙▄▄▀▝▚▄▞▘▐▙▄▄▖  █  \n"                                                            
      "                                                                   "
     "                                                                  ")

# time.sleep(2) 

print("An app that lets you set spending budgets and track your spending.\n")

# time.sleep(2) 

user_id = document.get("_id")  # Get the user_id field from the document

if first_login:
    print("The default spending categories are: Housing, Food, Transportation and Lifestyle \n")

    # time.sleep(3)  # Add a 2-second break after each input

    print(
        "Do you wish to add/remove budget categories so they better meet your needs? \n"
        "You can only do so when first registering.")

    decision = input("y / n: ")

    if decision == "y":
        DefineCategories(users, user_id)
    else:
        DefaultCategories(users, user_id)


    # Define Budget 
    print("It's time to Define your Monthly Budgets. You can later update these numbers.\n") 
    defineBudgets(users, user_id)

while True:
    #Main Menu
    menuOption = MainMenu()
    
    if menuOption == 1: ## Add expense
        addExpense(users, user_id)
    elif menuOption == 2:
        PrintBudget(users, user_id)
        print("Alright, now let's define your budgets.")
        defineBudgets(users, user_id)

    elif menuOption == 3:
        PrintBudget(users, user_id)

    elif menuOption == 4:
        viewExpenses(users, user_id)

    elif menuOption == 5:
        print("Goodbye!")
        break
