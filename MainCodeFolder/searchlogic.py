import HotelRooms

def search_rooms(max_cost=None, bed_keyword=None, room_type_keyword=None):      # None makes them optional choice
    found_rooms = []

    for room in HotelRooms.rooms:                                               
        if room["room_availability"] == "No":                                   # Has to be available
            continue
        if max_cost is not None:                                                # Maximum cost
            if room["room_cost"] > max_cost:                                    # Skips prices too high
                continue
        if bed_keyword is not None:                                             # Search by bed
            if bed_keyword.lower() not in room["rooms_beds"].lower():           # Skips rooms that are not searched
                continue
        if room_type_keyword is not None:                                       # Search by room type
            if room_type_keyword.lower() not in room["room_name"].lower():      # Skips rooms by type not found
                continue
        found_rooms.append(room)                                                # Adds found room last in list

    return found_rooms