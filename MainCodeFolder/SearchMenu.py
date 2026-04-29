import HotelRooms

def availability():                                                                     
    available_rooms = [] 
    for room in HotelRooms.rooms:
        if room["room_availability"].strip().lower() == "yes":
            available_rooms.append(room)
    return available_rooms
        
def beingcleaned():
    cleaned_rooms = []
    for room in HotelRooms.rooms:
        if room["room_availability"].strip().lower() == "being cleaned": 
            cleaned_rooms.append(room)
    return cleaned_rooms

def bookedrooms():
    bookedrooms = []
    for room in HotelRooms.rooms:
        if room["room_availability"].strip().lower() == "no": 
            bookedrooms.append(room)
    return bookedrooms

def maxcost(): 
    while True:   
        try:
            maxprice = int(input("Give the maximum price: "))
            break
        except ValueError:
            input("Must be a number. Enter to try again:")

        
    maxcost = []
    for room in HotelRooms.rooms:
        if room["room_cost"] <= maxprice:
            maxcost.append(room)
    return maxcost

def print_rooms(rooms):                                                             # For UI / UX 
    if not rooms:
        print(" -----------------")
        print("| No rooms found. |")
        print(" -----------------")
        return
    for room in rooms:
        print()
        print(f"Room {room['room_id']} | "f"Available: {room['room_availability']} | "f"Price: {room['room_cost']} €")

def search_menu():    


    while True:
        print(" -------------------")
        print("| Hotel room search |")
        print(" -------------------\n")
        print("1 - Search available rooms")
        print("2 - Search rooms that are being cleaned")
        print("3 - Search rooms that are booked")
        print("4 - Search rooms with defined price limit")
        print("5 - Exit search\n")
        
        try:
            search = int(input("What do you want to do? Give number:"))    
        except ValueError:
                input("\nMust be a number. Press enter and try again:")
                continue
        
        if 1 <= search <= 5: 
            print(f"Option {search}")
        else:
            input("\nIncorrect value given. Press enter and try again:")

        if search == 1:
            print("\n ---------------------")
            print("| All available rooms |")
            print(" ---------------------")
            print_rooms(availability())
            input("\nEnter to continue search:")
        elif search == 2:
            print()
            print(" ---------------------")
            print("| Rooms being cleaned |")
            print(" ---------------------")
            print_rooms(beingcleaned())
            input("\nEnter to continue search:")
        elif search == 3:
            print()
            print(" ------------------")
            print("| All booked rooms |")
            print(" ------------------")
            print_rooms(bookedrooms())
            input("\nEnter to continue search:")
        elif search == 4:
            print()
            print(" -------------------------------")
            print("| Rooms for defined price limit |")
            print(" -------------------------------")            
            print_rooms(maxcost())
            input("\nEnter to continue search:")
        elif search == 5:
            print("\nGoodbye and see you next time!\n")
            break