import HotelRooms
from Room_booking import book_room

def startmenu():
    print("+-----------------------------------------------+")
    print("|1 = View all available rooms                   |")
    print("|2 = Book a room                                |") 
    print("|3 = Check-out                                  |") 
    print("|4 = Add room listing                           |") 
    print("|5 = Remove room listing                        |")
    print("|6 = Exit the program                           |")
    print("+-----------------------------------------------+")
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
        print("Add here")
    elif choice == 3:
        try:
            room_id = int(input("Anna huoneen ID: "))
        except ValueError:
            print("Huoneen ID täytyy olla numero.")
        else:
            result = book_room(room_id, HotelRooms.rooms)
            print(result)
        input("Enter to continue:")
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