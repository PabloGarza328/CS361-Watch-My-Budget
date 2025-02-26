from pymongo import MongoClient
import time
import requests
import json



def addExpense(users, user_id):

    print("")
    user_document = users.find_one({"_id": user_id})
    categories = user_document["categories"]
    
    category_dict = {}  # To match input number with categoryID
    
    menu_option = 1
    for category in categories:
        print(" " + str(menu_option) + ". " + category['category_name'])
        category_dict[menu_option] = category['category_name']
        menu_option += 1
    
    while True:  # --------------------> Validate input
        try:
            category_decision = int(input("What category does the expense belong to? "))
            if category_decision > 0 and category_decision <= menu_option:
                break
            else:
                print("Invalid input")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            exit()
        except:
            print("Invalid input")

    
    while True:  # --------------------> Get spending amount
        try:
            expense = int(input("How much did you spend? "))
            if expense> 0:
                break
            else:
                print("Invalid input")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            exit()
        except:
            print("Invalid input")

    while True:  # --------------------> Get expense description
        try:
            description = (input("Add a brief description of the expense: "))
            if len(description) > 1:
                break
            else:
                print("Invalid input")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            exit()
        except:
            print("Invalid input")

    # Make POST request to microservice B

    api_url = "http://127.0.0.1:5000/add_expense"
    category = category_dict[category_decision]


    params = {"category": category, "expense": expense, "user_id": user_id, "description": description}
    try: 
        print("Sending request to server...")
        response = requests.post(api_url, params=params)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # print("Server Response: ",json.dumps(response.json(), indent=4))
        print("\nSuccesfully added expense...")
        time.sleep(2)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}{http_err.response.text}")
 
    return