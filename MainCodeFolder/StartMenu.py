import HotelRooms
import time
from RoomAvailabilityAndNewRooms import room_availability
from RoomAvailabilityAndNewRooms import add_room
from RoomAvailabilityAndNewRooms import remove_room
from Checkout import Checkout
from Room_booking import book_room
from searchtab import search_menu

def startmenu():
    print("+-----------------------------------------------+")
    print("|1 = Search for rooms                           |")
    print("|2 = List all available rooms                   |") 
    print("|3 = Book a room                                |") 
    print("|4 = Check-out                                  |") 
    print("|5 = Add room listing (admin only)              |")
    print("|6 = Remove room listing (admin only)           |")
    print("|7 = Exit the program                           |")
    print("+-----------------------------------------------+")
    while True:
        try:
            StartDecision = int(input("Enter a number (1-7)"))
            if 1 <= StartDecision <= 7: #Käytetään numeroita 1-6 aloittamaan eri osat ohjelmaa ja turvataan, jos käyttäjä antaa väärän numeron.
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
        search = search_menu()
        print(search)
        input("\nEnter to continue:")
    elif choice == 2:
        available = room_availability(HotelRooms.rooms)
        print(available)
        input("\nEnter to continue:")
    elif choice == 3:
        try:
            print("\nWelcome to booking system!")
            room_id = int(input("Give room ID: "))
            print("Processing...")
            time.sleep(2.5)
        except ValueError:
            print("Room ID must be a number.")
        else:
            result = book_room(room_id, HotelRooms.rooms)
            print(result)
        input("\nEnter to continue:")
    elif choice == 4:
        room_id = int(input("Give the ID of the room you had:"))
        Checkout(HotelRooms.rooms, room_id)
        input("\nEnter to continue:")
    elif choice == 5:
        add = add_room(HotelRooms.rooms)
        print(add)
        input("\nEnter to continue:")
    elif choice == 6:
        remove = remove_room(HotelRooms.rooms)
        print(remove)
        input("\nEnter to continue:")
    elif choice == 7:
        print(f"Goodbye!")
        exit_program()
        break