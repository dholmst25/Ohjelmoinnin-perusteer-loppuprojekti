import HotelRooms
import time

def book_room(rooms):    
    try:
        room_id = int(input("Give room ID: "))
    except ValueError:
        return print("Room ID must be a number.")

    print("Processing...")
    time.sleep(2.5)

    
    for room in rooms:      
        if room["room_id"] == room_id:
            if room["room_availability"] == "Yes":
                room["room_availability"] = "No"
                return print("Room successfully booked!")
            else:
                return print("Room already booked!")
    return print("Room not found!")