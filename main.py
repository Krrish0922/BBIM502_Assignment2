from datetime import datetime
import math

rooms = []

def display_rooms():
    # Check if any rooms are added to the system
    if len(rooms) == 0:
        print("No rooms available.")
        return
    
    for room in rooms:
        print("Room number:", room["number"])
        print("Room Type:", room["type"])
        print("Price per Night:", room["price"])
        if room["allocated"]:
            print("Status: Occupied")
        else:
            print("Status: Available")

def delete_room():
    try:
        # Get room number
        room_number = int(input("Enter room number to delete: "))
        
        for room in rooms:
            if room["number"] == room_number:
                # Prevent deletion of an allocated room
                if room["allocated"]:
                    print("Room is currently allocated and cannot be deleted.")
                    return
                # Remove room
                rooms.remove(room)
                print("Room deleted successfully.")
                return
        print("Room not found.")
    except ValueError:
        print("Invalid input. Please enter a valid room number.")
        

def add_room():
    try:
        # Get and validate room number
        room_number = int(input("Enter room number: "))
        if room_number <= 0:
            print("Room number must be a positive integer.")
            return
        
        # Check whether the room number already exists
        for room in rooms:
            if room["number"] == room_number:
                print("Room already exists.")
                return

        # Get and validate room type
        allowed_types = ["Single", "Double", "Deluxe"]
        room_type = input("Enter room type (Single/Double/Deluxe): ").strip()
        # Check if the input is non-empty
        if (room_type == ""):
            print("Room type cannot be empty")
            return
        # Make sure the entered room type is one of the accepted options
        if room_type not in allowed_types:
            print("Invalid room type. Please choose Single, Double, or Deluxe.")
            return

        # Get and validate room price
        price = float(input("Enter price per night: "))
        if not math.isfinite(price) or price <= 0:
            print("Room price must be a valid number greater than zero.")
            return

        room = {
            "number": room_number,
            "type": room_type,
            "price": price,
            "allocated": False,
            "customer_id": None,
            "customer_name": None,
            "nights": 0
        }
        
        # Add room to the rooms list
        rooms.append(room)
        print("Room added successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def show_menu():
    print("\nLANGHAM HOTEL MANAGEMENT SYSTEM")
    print("1. Add room")
    print("2. Delete Room")
    print("3. Display Room Details")
    print("4. Allocate Room")
    print("5. Display Room Allocation Details")
    print("6. Billing and De-Allocation")
    print("7. Save Room Allocations")
    print("8. Display Saved Allocations")
    print("9. Backup and Clear File")
    print("0. Exit")
    
while True:
    show_menu()
    choice = input("Enter your choice (0-9): ")
    
    if choice == "0":
        print("Thank you for using the system.")
        break
    elif choice == "1":
        add_room()
    else:
        print("Invalid choice. Enter a number from 0 to 9.")