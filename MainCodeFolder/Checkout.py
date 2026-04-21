import HotelRooms


def Checkout(rooms, room_id):
    for room in rooms:
        if room["room_id"] == room_id:
            if room["room_availability"] == "Yes":
                print("Huone on jo vapaa")
            else:
                room["room_availability"] == "No"
                room["room_availability"] = "Yes"
                print(f"Checkout successful. Room {room_id} is now available.")
            return
    print("Huonetta ei löydy")


