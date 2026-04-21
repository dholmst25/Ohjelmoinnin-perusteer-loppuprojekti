import HotelRooms


def Checkout(rooms, room_id):
    for room in rooms:
        if room["room_id"] == room_id:
            if room["room_availability"] == "Yes":
                print("Huone on jo vapaa")
            else:
                room["room_availability"] == "No"
                print(f"Checkout onnistui. Huone {room_id} on nyt vapaa.")
            return
    print("Huonetta ei löydy")


