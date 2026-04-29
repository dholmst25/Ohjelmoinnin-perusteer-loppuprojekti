import HotelRooms


def Checkout(rooms):
    try:
        room_id = int(input("Give the ID of the room you had:"))
    except ValueError:
        return print("Room ID must be a number.")
    
    for room in rooms:
        if room["room_id"] == room_id:
            if room["room_availability"] == "Yes":
                print("Room already available!")
            elif room["room_availability"] == "Being cleaned":
                print("Room not available!")
            elif room["room_availability"] == "No":
                room["room_availability"] = "Being cleaned"
                print(f"Checkout successful. Room {room_id} is now being cleaned.")
            break
    else:           
        print("Room not found!")

