from searchlogic import search_rooms

print()
print("Hotel room search")
print()
print("You can only search available rooms.")
print()
price_input = input("Give the maximum room cost (or press enter to skip): ")
bed_input = input("Search by bed type (or press enter to skip): ")
room_type_input = input("Search by room type (or press enter to skip): ")

# --- INPUT → VALUES ---
max_cost = int(price_input) if price_input else None
bed_keyword = bed_input if bed_input else None
room_type_keyword = room_type_input if room_type_input else None

# --- SEARCH ---
results = search_rooms(
    max_cost=max_cost,
    bed_keyword=bed_keyword,
    room_type_keyword=room_type_keyword
)

# --- OUTPUT ---
print("\nAvailable rooms:")

if not results:
    print("No rooms found with given criteria.")
else:
    for room in results:
        print(
            f"- {room['room_name']} | "
            f"{room['room_cost']} € | "
            f"{room['rooms_beds']}"
        )