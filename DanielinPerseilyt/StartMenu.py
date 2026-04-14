def startmenu():
    print("┌───────────────────────────────────────────────┐")
    print("|1 = Add room details                           |")
    print("|2 = View all available rooms                   |") 
    print("|3 = Book a room                                |") 
    print("|4 = Check-out                                  |") 
    print("|5 = Remove room listing                        |")
    print("|6 = Exit the program                           |")
    print("└───────────────────────────────────────────────┘")
    while True:
        try:
            StartDecision = int(input("Enter a number (1-6)"))
            if 1 <= StartDecision <= 6: #Käytetään numeroita 1-6 aloittamaan eri osat ohjelmaa ja turvataan, jos käyttäjä antaa väärän numeron.
                return StartDecision
            else:
                print("Incorrect value given. Try again.")
        except ValueError:
                print("Invalid number given. Please try again.")

def exit_program():
    print("Thank you for choosing us!")
    return False

while True:
    choice = startmenu()

    if choice == 1:
        print(f"You have selected option {choice}")
        print("Ho ho ho!")
    elif choice == 2:
        print(f"You have selected option {choice}")
        print("Hahaa")
    elif choice == 3:
        print(f"You have selected option {choice}")
        print("Hoo")
    elif choice == 4:
        print(f"You have selected option {choice}")
        print("Sazam!")
    elif choice == 5:
        print(f"You have selected option {choice}")
        print("Haha")
    elif choice == 6:
        print(f"You have selected option {choice}")
        exit_program()
        break