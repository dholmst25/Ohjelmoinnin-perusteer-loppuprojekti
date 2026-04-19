import HotelRooms

def book_room(room_id, rooms):
    for room in rooms:
        if room["room_id"] == room_id and room["room_availability"]:
            room["room_availability"] = False
            return "Room booked successfully!"
    return "Room not available!"