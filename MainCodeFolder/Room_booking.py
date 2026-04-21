def book_room(room_id, rooms):
    for room in rooms:
        if room["room_id"] == room_id:
            if room["room_availability"]:
                room["room_availability"] = False
                return "Room booked successfully!"
            else:
                return "Room already booked!"
    return "Room not found!"