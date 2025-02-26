from pymongo import MongoClient
from bson.objectid import ObjectId



def DefaultCategories(users, user_id):
    print(
        "\nThe current categories are: Housing, Food, Transportation and Lifestyle. \n" )
    
    categories = [
        {
            "categoryID" : ObjectId(),
            "category_name": "Housing",
            "budget_amount": None,  
            "spent": 0 
        },
        {
            "categoryID" : ObjectId(),            
            "category_name": "Food",
            "budget_amount": None,  
            "spent": 0 
        },
        {
            "categoryID" : ObjectId(),
            "category_name": "Transportation",
            "budget_amount": None,  
            "spent": 0 
        },
        {
            "categoryID" : ObjectId(),
            "category_name": "Lifestyle",
            "budget_amount": None,  
            "spent": 0 
        }
    ] 
    
    users.update_one(
        {"_id": user_id},
        {"$set": {"categories": categories}}
    )
    
    return True
