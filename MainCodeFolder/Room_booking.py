import HotelRooms
import time

def book_room(room_id, rooms):    
    try:
        room_id = int(room_id)
    except ValueError:
        return "Room ID must be a number."

    print("Processing...")
    time.sleep(2.5)

    
    for room in rooms:      
        if room["room_id"] == room_id:
            if room["room_availability"] == "Yes":
                room["room_availability"] = "No"
                return "Room successfully booked!"
            else:
                return "Room already booked!"
    return "Room not found!"