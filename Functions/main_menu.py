def MainMenu():
    print("\nMenu")
    print("     1. Add Expense")
    print("     2. Modify budget ")
    print("     3. See currenty montly budget ")
    print("     4. View current spending")
    print("     5. Exit the program")

    while True:
        try: 
            decision = int(input("\n Please type a menu option: "))
            if decision > 0 and decision < 6:
                break
            else:
                print("Invalid input")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            exit()
        except:
            print("Invalid input")


    return decision