import HotelRooms

# ------------------ SHOW AVAILABLE ROOMS ------------------
id_w, name_w, bed_w, cost_w, break_w, avail_w = 7, 15, 39, 4, 12, 13 #W = width
def room_availability(rooms):
    print("+---------+-----------------+-----------------------------------------+------+--------------+---------------+")
    print("| Room ID | Name            | Bed Configuration                       | Cost | Breakfast    | Available     |")
    print("+---------+-----------------+-----------------------------------------+------+--------------+---------------+")

    for room in rooms:
        if room["room_availability"] == "Yes":
            print(f"| {room['room_id']:<{id_w}} | "
                  f"{room['room_name']:<{name_w}} | "
                  f"{room['rooms_beds']:<{bed_w}} | "
                  f"{room['room_cost']:<{cost_w}} | "
                  f"{room['room_breakfast']:<{break_w}} | "
                  f"{room['room_availability']:<{avail_w}} |")

    print("+---------+-----------------+-----------------------------------------+------+--------------+---------------+")


# ------------------ ADD ROOM ------------------
def add_room(rooms):
    try:
        room_id = int(input("Enter new room ID: "))
    except ValueError:
        return "Room ID must be a number."

    # tarkistetaan ettei ID ole jo käytössä
    for room in rooms:
        if room["room_id"] == room_id:
            return "Room with this ID already exists!"

    room_name = input("Enter room name: ")
    rooms_beds = input("Enter bed configuration: ")

    try:
        room_cost = int(input("Enter room cost: "))
    except ValueError:
        return "Cost must be a number."

    room_breakfast = input("Breakfast (Included/Not Included): ")
    room_availability = input("Availability (Yes/No/Being cleaned): ")

    new_room = {
        "room_id": room_id,
        "room_name": room_name,
        "rooms_beds": rooms_beds,
        "room_cost": room_cost,
        "room_breakfast": room_breakfast,
        "room_availability": room_availability
    }

    rooms.append(new_room)
    return "Room added successfully!"


# ------------------ REMOVE ROOM ------------------
def remove_room(rooms):
    try:
        room_id = int(input("Enter room ID to remove: "))
    except ValueError:
        return "Room ID must be a number."

    for room in rooms:
        if room["room_id"] == room_id:
            rooms.remove(room)
            return "Room removed successfully!"

    return "Room not found!"