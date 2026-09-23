def main():
    print("=== Hotel Reservation System ===")

    # Collecting input
    serial_number = input("Enter Serial Number: ")
    reservation_mode = input("Enter Reservation Mode: ")
    name_and_address = input("Enter Name and Address: ")
    contact_number = input("Enter Contact Number: ")
    check_in = input("Enter Check-in Time and Date: ")
    check_out = input("Enter Checkout Time and Date: ")
    pax = input("Enter Pax: ")
    room_type = input("Enter Room Type (AC or non AC): ")
    occupants = input("Enter Number of Occupants: ")
    remarks = input("Enter Remarks: ")

    # Displaying summary
    print("\n--- Reservation Summary ---")
    print(f"Serial Number:        {serial_number}")
    print(f"Reservation Mode:     {reservation_mode}")
    print(f"Name and Address:     {name_and_address}")
    print(f"Contact Number:       {contact_number}")
    print(f"Check-in Time & Date: {check_in}")
    print(f"Checkout Time & Date: {check_out}")
    print(f"Pax:                  {pax}")
    print(f"Room Type:            {room_type}")
    print(f"Number of Occupants:  {occupants}")
    print(f"Remarks:              {remarks}")
    print("---------------------------")

if __name__ == "__main__":
    main()
