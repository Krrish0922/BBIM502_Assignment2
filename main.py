from datetime import datetime
import math

rooms = []

def display_rooms():
    for room in rooms:
        print("Room number:", room["number"])
        print("Room Type:", room["type"])
        print("Price per Night:", room["price"])
        if room["allocated"]:
            print("Status: Occupied")
        else:
            print("Status: Available")

def delete_room():
    room_number = input("Enter room number to delete: ")
    for room in rooms:
        if room["number"] == room_number:
            rooms.remove(room)
            print("Room deleted successfully.")
            return

def add_room():
    room_number = input("Enter room number: ")
    
    for room in rooms:
        if room["number"] == room_number:
            print("Room already exists.")
            return
    
    room_type = input("Enter room type (Single/Double/Deluxe): ").strip()
    if (room_type == ""):
        print("Room type cannot be empty")
        return
    
    price = input("Enter price per night: ")
    if price <= 0:
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
    
    rooms.append(room)
    print("Room added successfully.")

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