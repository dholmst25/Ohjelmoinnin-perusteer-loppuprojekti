import HotelRooms

def book_room(room_id, rooms):
    for room in rooms:
        if room["room_id"] == room_id:
            if room["room_availability"]:
                room["room_availability"] = False
                return "Huone varattu onnistuneesti!"
            else:
                return "Huone on jo varattu!"
    return "Huonetta ei löytynyt!"


print(book_room(104, HotelRooms.rooms))