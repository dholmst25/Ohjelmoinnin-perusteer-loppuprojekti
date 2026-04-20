print("+---------+-----------------+----------------------------------------+------+--------------+-----------+")
print("| Room ID | Name            | Bed Configuration                      | Cost | Breakfast    | Available |")
print("+---------+-----------------+----------------------------------------+------+--------------+-----------+")
for room in rooms:
  if room["room_availability"] == "Yes":
    print(f"|Room {room['room_id']} | {room['room_name']} | {room['rooms_beds']} | {room['room_cost']}  | {room['room_breakfast']} | {room['room_availability']}       |")

print("+---------+-----------------+----------------------------------------+------+--------------+-----------+")