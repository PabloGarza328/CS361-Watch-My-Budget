from pymongo import MongoClient
import requests
import time



def printSpendingBasic(spendingDict):

    print("\nThis is what you've spent this month:\n")

    for key in spendingDict:
        print(f"{key}: {spendingDict[key]}")

    time.sleep(5)

    return

def printSpendingDetailed(spendingDict):

    print("\nThis is your detailed spending record for this month:\n")

    for key in spendingDict:
        print(key)
        for expense in spendingDict[key]:
            print ("  ", expense)

    time.sleep(5)

    return




def viewExpenses(users, user_id):   # ------> Make get request to Microservice C for non detailed spending
    
    
    api_url = "http://127.0.0.1:5001/view_expenses"
    params = {"user_id": user_id, "detailed": False}
    try:
        # print("Sending request to server...")
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        
        printSpendingBasic(response.json())


    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}{http_err.response.text}")
 
    

    while True:  # --------------------> Get detailed spending decision
        try:
            decision = input("\nDo you wish to see all your individual expenses for this month? y/n: ")
            if decision == "y":
                break
            elif decision == "n":
                break
            else:
                print("Invalid input")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            exit()
        except:
            print("Invalid input")

    
    if decision == "y":  ## ---------------> Make get request to Microservice C for detailed spending
        
        params = {"user_id": user_id, "detailed": True}
        
        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()

            printSpendingDetailed(response.json())
            

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}{http_err.response.text}")
    


    return
