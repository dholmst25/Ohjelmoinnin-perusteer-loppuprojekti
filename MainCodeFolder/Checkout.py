import HotelRooms


def Checkout(rooms, room_id):
    for room in rooms:
        if room["room_id"] == room_id:
            if room["room_availability"] == "Yes":
                print("Room already available!")
            elif room["room_availability"] == "Being cleaned":
                print("Room not available!")     
            else:
                room["room_availability"] == "No"
                room["room_availability"] = "Yes"
                print(f"Checkout successful. Room {room_id} is now available.")
            return
    print("Room not found!")


