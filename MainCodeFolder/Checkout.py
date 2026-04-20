def Checkout(rooms, room_id):
    for room in rooms:
        if room["room_id"] == room_id:
            if room["available"]:
                print("Huone on jo vapaa")
            else:
                room["available"] = True
                print(f"Checkout onnistui. Huone {room_id} on nyt vapaa.")
            return
    print("Huonetta ei löydy")

room_id = int(input("Anna huoneen numero jossa olit:"))
checkout(rooms, room_id)