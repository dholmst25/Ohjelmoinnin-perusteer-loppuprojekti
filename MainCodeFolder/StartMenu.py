import HotelRooms
from RoomAvailabilityAndNewRooms import room_availability
from RoomAvailabilityAndNewRooms import add_room
from RoomAvailabilityAndNewRooms import remove_room
from Checkout import Checkout
from Room_booking import book_room
from SearchMenu import search_menu
from Cleaning import Cleaning

def startmenu():
    print("+-----------------------------------------------+")
    print("|1 = Search for rooms                           |")
    print("|2 = List all available rooms                   |") 
    print("|3 = Book a room                                |") 
    print("|4 = Check-out                                  |") 
    print("|5 = Clean room (cleaning staff only)           |")
    print("|6 = Add room listing (admin only)              |")
    print("|7 = Remove room listing (admin only)           |")
    print("|8 = Exit the program                           |")
    print("+-----------------------------------------------+")
    while True:
        try:
            StartDecision = int(input("Enter a number (1-7)"))
            if 1 <= StartDecision <= 8: #Käytetään numeroita 1-8 aloittamaan eri osat ohjelmaa ja turvataan, jos käyttäjä antaa väärän numeron.
                return StartDecision
            else:
                print("Incorrect value given. Try again.")
        except ValueError:
                print("Invalid number given. Please try again.")

def exit_program():
    print(f"Goodbye!")
    print("Thank you for choosing us!")

while True:
    choice = startmenu()

    if choice == 1:
        search_menu()
        input("\nEnter to continue:")
    elif choice == 2:
        room_availability(HotelRooms.rooms)
        input("\nEnter to continue:")
    elif choice == 3:
        print("\nWelcome to booking system!")
        book_room(HotelRooms.rooms)
        input("\nEnter to continue:")       
    elif choice == 4:
        Checkout(HotelRooms.rooms)
        input("\nEnter to continue:")
    elif choice == 5:
        Cleaning(HotelRooms.rooms)
        input("\nEnter to continue:")
    elif choice == 6:
        add = add_room(HotelRooms.rooms)
        print(add)
        input("\nEnter to continue:")
    elif choice == 7:
        remove = remove_room(HotelRooms.rooms)
        print(remove)
        input("\nEnter to continue:")
    elif choice == 8:
        exit_program()
        break