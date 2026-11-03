from datetime import datetime
import math

filename = "LHMS_850011804.txt"
rooms = []

def backup_file():
    try:
        with open(filename, "r", encoding = "utf-8") as file:
            data = file.read()

        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = filename.replace(
            ".txt", "_Backup_" + current_time + ".txt"
        )

        with open(backup_name, "a", encoding="utf-8") as file:
            file.write(data)
        with open(filename, "w", encoding="utf-8") as file:
            file.write("")

        print("Backup created successfully.")
        print("Backup File:", backup_name)
        print("Original file cleared.")
        
    except FileNotFoundError:
        print("File not found. Please save allocations first.")
    except OSError:
        print("Error during backup.")

def read_allocations():
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print("File not found. Please save allocations first.")
    except OSError:
        print("Error while reading the file.")

def save_allocations():
    try: 
        with open(filename, "w", encoding="utf-8") as file:
            for room in rooms:
                file.write("Room Number: " + str(room["number"]) + "\n")
                file.write("Customer ID: " + str(room["customer_id"]) + "\n")
                file.write("Customer Name: " + room["customer_name"] + "\n")
                file.write("Nights: " + str(room["nights"]) + "\n")
                file.write("-------------------------\n")
    except OSError:
        print("Error while saving the file.")

def billing():
    try:
        room_number = int(input("Enter room number for billing: "))
        
        for room in rooms:
            if room["number"] == room_number:
                total = room["price"] * room["nights"]
                print("---------- BILL ----------")
                print("Room Number:", room["number"])
                print("Customer Name:", room["customer_name"])
                print("Price per Night: $", room["price"])
                print("Number of Nights:", room["nights"])
                print("Total Bill: $", total)
                print("--------------------------")
                
                confirm = input("De-allocate room? (yes/no): ").lower()
                
                if confirm == "yes":
                    room["allocated"] = False
                    room["customer_id"] = None
                    room["customer_name"] = None
                    room["nights"] = 0
                    
                    print("Room de-allocated successfully.")
                elif confirm == "no":
                    print("De-allocation cancelled.")
                else:
                    print("Incorrect input. De-allocation cancelled.")
    except ValueError:
        print("Invalid room number.")
    except EOFError:
        print("Input was interrupted. Billing was not finished.")

def display_allocations():
    found = False
    for room in rooms:
        if room["allocated"]:
            found = True
            print("-------------------------")
            print("Room Number:", room["number"])
            print("Customer ID:", room["customer_id"])
            print("Customer Name:", room["customer_name"])
            print("Number of Nights:", room["nights"])
    if not found:
        print("No rooms are currently allocated.")

def allocate_room():
    try:
        room_number = int(input("Enter room number to allocate: "))
        
        for room in rooms:
            if room["number"] == room_number:
                customer_id = int(input("Enter customer ID: "))
                customer_name = input("Enter customer name: ").strip()
                nights = int(input("Enter number of nights: "))
                
                room["customer_id"] = customer_id
                room["customer_name"] = customer_name
                room["nights"] = nights
                room["allocated"] = True
                print("Room allocated successfully.")
                return
        print("Room not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

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