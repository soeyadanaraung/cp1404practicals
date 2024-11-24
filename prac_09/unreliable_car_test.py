from unreliable_car import UnreliableCar

# Create two UnreliableCar instances with different reliability
unreliable_car = UnreliableCar("Prius 1", 100, 20)
reliable_car = UnreliableCar("Prius 2", 100, 85)

for attempt in range(1, 4):
    print(f"Attempt {attempt}:")
    print(f"{unreliable_car.name} drove {unreliable_car.drive(30)}km")
    print(f"{reliable_car.name} drove {reliable_car.drive(30)}km")
    print()


