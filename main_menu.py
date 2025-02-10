def MainMenu():
    print("\nMenu")
    print("     1. Add Expense")
    print("     2. Modify budget ")
    print("     3. See currenty montly budget ")

    while True:
        try: 
            decision = int(input("\n Please type a menu option: "))
            if decision > 0 and decision < 4:
                break;
            else:
                print("Invalid input")
        except:
            print("Invalid input")


    return decision