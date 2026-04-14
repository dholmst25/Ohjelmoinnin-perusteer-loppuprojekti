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
choice = startmenu()
print(f"You have selected option {choice}")
if choice == 1:
    def
if choice == 2:
    def
if choice == 3:
    def
if choice == 4:
    def
if choice == 5:
    def
if choice == 6:
    exit