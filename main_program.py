from pymongo import MongoClient
import certifi
from define_categories import DefineCategories  # Import the function from define_categories.py
from define_Budgets import defineBudgets 
from main_menu import MainMenu
from print_budgets import PrintBudget
from default_categories import DefaultCategories
import time  # Import the time module to use time.sleep()
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
database_url = os.getenv("MONGO_DB_URL")

# Connect to MongoDB database
client = MongoClient(
    database_url,
    tlsCAFile=certifi.where() ) 

db = client['budgetingApp']  # Replace with your database name
budgetingApp_collection  = db['budgetingApp']  

# Create a new document to insert into the collection 

# Check if John Doe is already registered
document = budgetingApp_collection.find_one({"Name": "John Doe"})

# if document:
    # print("Document found:", document)
if not document:
    print("No document found with Name: 'John Doe'")
    new_document = {
    "Name": "John Doe", 
    "user_id": "user123",    
    }
    result = budgetingApp_collection.insert_one(new_document)



print("Welcome to")
print("▗▖ ▗▖ ▗▄▖▗▄▄▄▖▗▄▄▖▗▖ ▗▖    ▗▖  ▗▖▗▖  ▗▖    ▗▄▄▖ ▗▖ ▗▖▗▄▄▄  ▗▄▄▖▗▄▄▄▖▗▄▄▄▖\n"
      "▐▌ ▐▌▐▌ ▐▌ █ ▐▌   ▐▌ ▐▌    ▐▛▚▞▜▌ ▝▚▞▘     ▐▌ ▐▌▐▌ ▐▌▐▌  █▐▌   ▐▌     █  \n"
      "▐▌ ▐▌▐▛▀▜▌ █ ▐▌   ▐▛▀▜▌    ▐▌  ▐▌  ▐▌      ▐▛▀▚▖▐▌ ▐▌▐▌  █▐▌▝▜▌▐▛▀▀▘  █  \n"
      "▐▙█▟▌▐▌ ▐▌ █ ▝▚▄▄▖▐▌ ▐▌    ▐▌  ▐▌  ▐▌      ▐▙▄▞▘▝▚▄▞▘▐▙▄▄▀▝▚▄▞▘▐▙▄▄▖  █  \n"                                                            
      "                                                                   "
     "                                                                  ")

time.sleep(2) 

print("An app that lets you set spending budgets and track your spending.\n")

time.sleep(2) 

print("The default spending categories are: Housing, Food, Transportation and Lifestyle \n")

time.sleep(3)  # Add a 2-second break after each input

print(
    "Do you wish to add/remove budget categories so they better meet your needs? \n"
    "You can only do so when first registering.")

decision = input("y / n: ")

user_id = document.get("user_id")  # Get the user_id field from the document
if decision == "y":
    DefineCategories(budgetingApp_collection, user_id)
else:
    DefaultCategories(budgetingApp_collection, user_id)


# Define Budget 
print("It's time to Define your Monthly Budgets. You can later update these numbers.\n") 
defineBudgets(budgetingApp_collection, user_id)

while True:
    #Main Menu
    menuOption = MainMenu()
    
    if menuOption == 1:
        print("Yet to develop this feature")
    elif menuOption == 2:
        PrintBudget(budgetingApp_collection, user_id)
        print("Alright, now let's define your budgets.")
        defineBudgets(budgetingApp_collection, user_id)

    elif menuOption == 3:
        PrintBudget(budgetingApp_collection, user_id)
