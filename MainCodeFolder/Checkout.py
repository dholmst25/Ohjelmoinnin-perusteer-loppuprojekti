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

while True:
    print("1. Checkout")
    print("2. Exit")
    choice = input("Valinta:")

    if choice == "1":
        room_id = int(input("Anna huoneen numero jossa olit:"))
        Checkout(rooms, room_id)
    elif choice == "2":
        break