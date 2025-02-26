from pymongo import MongoClient
import time

def PrintBudget(users, user_id):

    document = users.find_one({"_id": user_id})
    categories = document['categories']

    print("\nThis is your current monthly budget:\n")

    for category in categories:
        print(f"{category['category_name']}: {category['budget_amount']}")

    time.sleep(5)  # Add a 2-second break after each input

    return

