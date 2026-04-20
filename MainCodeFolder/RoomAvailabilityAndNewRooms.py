# ------------------ SHOW AVAILABLE ROOMS ------------------
def room_availability(rooms):
    print("+---------+-----------------+----------------------------------------+------+--------------+-----------+")
    print("| Room ID | Name            | Bed Configuration                      | Cost | Breakfast    | Available |")
    print("+---------+-----------------+----------------------------------------+------+--------------+-----------+")

    for room in rooms:
        if room["room_availability"] == "Yes":
            print(f"| {room['room_id']}      | {room['room_name']} | {room['rooms_beds']} | {room['room_cost']}  | {room['room_breakfast']} | {room['room_availability']}       |")

    print("+---------+-----------------+----------------------------------------+------+--------------+-----------+")


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