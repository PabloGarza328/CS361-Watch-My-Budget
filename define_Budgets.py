from pymongo import MongoClient
import time

def defineBudgets(budgetingAppCollection, user_id):
    
    document = budgetingAppCollection.find_one({"user_id": user_id})
    categories = document["categories"]

    for category in categories:
        while True:
            try:
                budget = float(input(f"{category['category_name']}: "))
                category["budget_amount"] = budget
                break
            except ValueError:
                print("Invalid input. Please enter a valid number")
    
    budgetingAppCollection.update_one(
        {"user_id": user_id},
        {"$set": {"categories": categories}}
    )

    print("Budgets updated successfully... \n")

    time.sleep(3)  # Add a 2-second break after each input


    return

            



    





    
    