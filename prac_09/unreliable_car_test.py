from unreliable_car import UnreliableCar

def main():
    """Test the UnreliableCar class with the specified output format."""

    # Create two UnreliableCar instances
    prius_1 = UnreliableCar("Prius 1", 100, 50)  # 50% reliability
    prius_2 = UnreliableCar("Prius 2", 100, 80)  # 80% reliability

    # Number of test drives
    test_drives = 3
    drive_distance = 30  # Attempt to drive 30 km each time

    for _ in range(test_drives):
        # Test driving each car
        prius_1_distance = prius_1.drive(drive_distance)
        prius_2_distance = prius_2.drive(drive_distance)

        # Print results in the desired format
        print(f"{prius_1.name} drove {prius_1_distance}km")
        print(f"{prius_2.name} drove {prius_2_distance}km")
        print()  # Blank line between attempts

if __name__ == "__main__":
    main()

