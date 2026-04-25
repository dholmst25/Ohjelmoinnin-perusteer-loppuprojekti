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
        room_id_check = int(input("Enter new room ID (1-999): "))
        if 1 <= room_id_check <= 999:
            room_id = room_id_check
        else:
            return "Maximum room id number is 999."
    except ValueError:
        return "Room ID must be a number."

    # tarkistetaan ettei ID ole jo käytössä
    for room in rooms:
        if room["room_id"] == room_id:
            return "Room with this ID already exists!"

    try: 
        room_name = input("Enter room name (Max character limit is 15): ")[:name_w] #Limits name length
    except ValueError:
        return "Maximum room name character limit is 15"
    try:
        rooms_beds = input("Enter bed configuration (Max character limit is 39): ")[:bed_w]
    except ValueError:
        return "Maximum room configuration character limit is 39"
    try:
        room_cost_check = int(input("Enter room cost (1-9999): "))
        if 1 <= room_cost_check <= 9999:
            room_cost = room_cost_check
        else:
            return "Maximum room cost is 9999"
    except ValueError:
        return "Cost must be a number."

    try:
        print("Breakfast")
        print("1 = Included")
        print("2 = Not Included")
        room_breakfast_check = int(input("Enter a number (1-2):"))
        if 1 <= room_breakfast_check <= 2:
            if room_breakfast_check == 1:
                room_breakfast = "Included"
            elif room_breakfast_check == 2:
                room_breakfast = "Not Included"
            else:
                return "Incorrect value given."
    except ValueError:
        return "Invalid number given."
    
    try:
        print("Availability")
        print("1 = Yes")
        print("2 = No")
        print("3 = Being cleaned")
        room_availability_check = int(input("Enter a number (1-3):"))
        if 1 <= room_availability_check <= 2:
            if room_availability_check == 1:
                room_availability = "Yes"
            elif room_availability_check == 2:
                room_availability = "No"
            elif room_availability_check == 3:
                room_availability = "Being cleaned"
        else:
            return "Incorrect value given."
    except ValueError:
            return "Invalid number given."
    

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