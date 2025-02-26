from pymongo import MongoClient
from bson.objectid import ObjectId


def DefineCategories(users, user_id):
    print(
        "\nThe current categories are: Housing, Food, Transportation and Lifestyle. \n" 
        "You will first define how many categories you want in total, \n"
        "and then asked to name each one.")
    
    while True:
        category_input= input("\nHow many categories will do you wish to have? (Choose between 1 and 10):")
        try: 
            category_Number = int(category_input)
            if category_Number > 0 and category_Number < 11:
                break
            else:
                print("Incorrect input")
        except:
            print("Incorrect input")
    
    categories = []  # List to store the category names

    print("\nGreat, now it's time to name each one.")
    for i in range(category_Number):
        category_Name = input(f"Category #{i+1}:")
         # Add each category as a sub-document with the required fields
        category = {
            "categoryID" : ObjectId(),
            "category_name": category_Name,
            "budget_amount": None,  
            "spent": 0 
        }
        categories.append(category)  # Add category sub-document to the list
    users.update_one(
        {"_id": user_id},
        {"$set": {"categories": categories}}
    )
    
    return True


