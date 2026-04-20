def check_out(hotel, room_number):
    for room in rooms:
        if room.number == room_number:
            if not room.is_available:
                print(f"Room {room_number} is now free (guest was {room.guest}).")
                room.is_available = True
                room.guest = None
            else:
                print("Room is already free")
            return
    print("Room not found")