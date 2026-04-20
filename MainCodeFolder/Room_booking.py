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

try:
    room_id = int(input("Anna huoneen ID: "))
except ValueError:
    print("Huoneen ID täytyy olla numero.")
else:
    result = book_room(room_id, HotelRooms.rooms)
    print(result)