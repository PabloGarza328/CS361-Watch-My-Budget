from pymongo import MongoClient


def DefaultCategories(budgetingAppCollection, user_id):
    print(
        "\nThe current categories are: Housing, Food, Transportation and Lifestyle. \n" 
        "You will first define how many categories you want in total, \n"
        "and then asked to name each one.")
    
    categories = [
        {
            "category_name": "Housing",
            "budget_amount": None,  
            "spent": 0 
        },
        {
            "category_name": "Food",
            "budget_amount": None,  
            "spent": 0 
        },
        {
            "category_name": "Transportation",
            "budget_amount": None,  
            "spent": 0 
        },
        {
            "category_name": "Lifestyle",
            "budget_amount": None,  
            "spent": 0 
        }
    ] 
    
    budgetingAppCollection.update_one(
        {"user_id": user_id},
        {"$set": {"categories": categories}}
    )
    
    return True
