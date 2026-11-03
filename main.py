try:
    from datetime import datetime
    import math
except ImportError:
    print("Required module or import could not be loaded.")
    exit()

# Store the hotel room details while the program is running
filename = "LHMS_850011804.txt"
rooms = []

def backup_file():
    try:
        # Read the saved allocation details
        with open(filename, "r", encoding = "utf-8") as file:
            data = file.read()

        # If empty, no need to create a backup
        if data == "":
            print("File is empty. Nothing to backup.")
            return
        
        # Add the current date and time to the backup filename
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = filename.replace(
            ".txt", "_Backup_" + current_time + ".txt"
        )

        # Write into the backup file
        with open(backup_name, "a", encoding="utf-8") as file:
            file.write(data)
        
        #  Reset the original file to empty
        with open(filename, "w", encoding="utf-8") as file:
            file.write("")

        print("Backup created successfully.")
        print("Backup File:", backup_name)
        print("Original file cleared.")
        
    except FileNotFoundError:
        print("File not found. Please save allocations first.")
    except OSError:
        print("Error during backup.")

# Read the saved allocations from the original file
def read_allocations():
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read()
            if data == "":
                print("File is empty.")
            else:
                print(data)
    except FileNotFoundError:
        print("File not found. Please save allocations first.")
    except OSError:
        print("Error while reading the file.")

# Save only the allocated rooms
def save_allocations():
    try: 
        with open(filename, "w", encoding="utf-8") as file:
            for room in rooms:
                if room["allocated"]:
                    # Write each room's allocation details on a separate line
                    file.write("Room Number: " + str(room["number"]) + "\n")
                    file.write("Customer ID: " + str(room["customer_id"]) + "\n")
                    file.write("Customer Name: " + room["customer_name"] + "\n")
                    file.write("Nights: " + str(room["nights"]) + "\n")
                    file.write("-------------------------\n")
        print("Room allocations saved successfully.")
    except OSError:
        print("Error while saving the file.")

def billing():
    try:
        # Get room number
        room_number = int(input("Enter room number for billing: "))
        
        # Loop through the rooms list
        for room in rooms:
            # Find the room where room["number"] matches the input
            if room["number"] == room_number:
                if room["number"] == room_number:
                    print("Room is not allocated.")
                    return
                
                # Calculate the total price
                total = room["price"] * room["nights"]
                
                # Average cost is calculated only to demonstrate Zero Division Error
                average_cost = total / room["nights"]
                if not math.isfinite(total):
                    raise OverflowError("Bill amount is too large.")
                
                print("---------- BILL ----------")
                print("Room Number:", room["number"])
                print("Customer Name:", room["customer_name"])
                print("Price per Night: $", room["price"])
                print("Number of Nights:", room["nights"])
                print("Total Bill: $", total)
                print("--------------------------")
                
                # Confirm if the user wants to check-out
                confirm = input("De-allocate room? (yes/no): ").lower()
                
                # Clear the customer details after successful de-allocation
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
                return
        print("Room not found.")
    except ValueError:
        print("Invalid room number.")
    except ZeroDivisionError:
        print("Cannot calculate average cost because nights cannot be zero.")
    except (OverflowError, TypeError):
        print("Unable to calculate the bill.")
    except EOFError:
        print("Input was interrupted. Billing was not finished.")

def display_allocations():
    # Keep track of whether atleast one room has been allocated
    found = False
    
    for room in rooms:
        # Display details only for rooms that are currently occupied
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
        # Get and validate your room number
        room_number = int(input("Enter room number to allocate: "))
        if room_number <= 0:
            print("Room number must be positive.")
            return
        
        # Check for each room in rooms list if some room matches with the input
        for room in rooms:
            if room["number"] == room_number:
                # Check whether the selected room is already occupied
                if room["allocated"]:
                    print("Room is already occupied.")
                    return
                
                # Collect and validate customer details
                customer_id = int(input("Enter customer ID: "))
                customer_name = input("Enter customer name: ").strip()
                nights = int(input("Enter number of nights: "))
                
                if customer_id <= 0 or customer_name == "" or nights <= 0:
                    print("Please enter valid customer details.")
                    return
                
                # Store the customer information in the selected room
                room["customer_id"] = customer_id
                room["customer_name"] = customer_name
                room["nights"] = nights
                room["allocated"] = True
                print("Room allocated successfully.")
                return
        print("Room not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except EOFError:
        print("Input was interrupted. Room was not allocated.")

def display_rooms():
    # Check if any rooms are added to the system
    if len(rooms) == 0:
        print("No rooms available.")
        return
    
    # Display details of each room in the rooms list
    for room in rooms:
        print("Room number:", room["number"])
        print("Room Type:", room["type"])
        print("Price per Night:", room["price"])
        
        # Show the current availability status
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
    except EOFError:
        print("Input was interrupted. Room was not deleted.")

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
    except EOFError:
        print("Input was interrupted. Room was not added.")

def show_menu():
    # Display all available hotel management operations
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
    
# Keep showing menu and asking for choice until the user exits the system
while True:
    try:
        show_menu()
        choice = input("Enter your choice (0-9): ")
        
        if choice == "0":
            print("Thank you for using the system.")
            break
        elif choice == "1":
            add_room()
        elif choice == "2":
            delete_room()
        elif choice == "3":
            display_rooms()
        elif choice == "4":
            allocate_room()
        elif choice == "5":
            display_allocations()
        elif choice == "6":
            billing()
        elif choice == "7":
            save_allocations()
        elif choice == "8":
            read_allocations()
        elif choice == "9":
            backup_file()
        else:
            print("Invalid choice. Enter a number from 0 to 9.")
    except EOFError:
        print("\nInput ended. Closing application.")
        break

    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
        break