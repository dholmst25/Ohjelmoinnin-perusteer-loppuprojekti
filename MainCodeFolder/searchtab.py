from searchlogic import search_rooms                                                  

def search_menu():
    print()
    print("Hotel room search by feature")
    print()
    print("You can now search for available rooms with defined features. Non-available rooms are not listed.")
    print()
    price_input = input("Give the maximum room cost (or press enter): ")               
    bed_input = input("Search by bed type (or press enter): ")
    room_type_input = input("Search by room type (or press enter): ")
                                                                                    # NONE skips definition
    max_cost = int(price_input) if price_input else None                            # Defines MAX for search if defined
    bed_keyword = bed_input if bed_input else None                                  # Defines bed keyword if type is defined
    room_type_keyword = room_type_input if room_type_input else None                # Defines room type keyword if type is defined

    results = search_rooms(max_cost=max_cost, bed_keyword=bed_keyword, room_type_keyword=room_type_keyword)

    print("Available rooms:")
    if not results:                                                     # If the search doesn't succeed
        print("No rooms found.")
    else:                                                               # Prints the results
        for room in results:
            print(f"- Room number: {room['room_id']} | "f"- Room type: {room['room_name']} | "f"- Room cost: {room['room_cost']} € | "f"- Bed type: {room['rooms_beds']}")