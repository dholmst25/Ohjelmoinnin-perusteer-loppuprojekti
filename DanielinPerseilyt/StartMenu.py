def startmenu():
    print("┌───────────────────────────────────────────────┐")
    print("|1 = Add room details                           |")
    print("|2 = View all available rooms                   |") 
    print("|3 = · Update stock levels (restock, sell items)|") 
    print("|4= Search for a product by name                |") 
    print("|5 = Remove a product                           |")
    print("└───────────────────────────────────────────────┘")
    while True:
        try:
            StartDecision = int(input("Enter a number (1-5)"))
            if 1 <= StartDecision <= 5: #Käytetään numeroita 1-5 aloittamaan eri osat ohjelmaa ja turvataan, jos käyttäjä antaa väärän numeron.
                return StartDecision
            else:
                print("Incorrect value given. Try again.")
                startmenu()
        except ValueError:
            print("Invalid number given. Please try again.")
choice = startmenu()
print(f"You have selected option {choice}")