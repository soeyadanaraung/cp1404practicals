import random
from car import Car  # Assuming Car is the base class

class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Drive the car a certain distance based on its reliability.
        Only drives if a random number is less than the reliability.
        """
        random_number = random.uniform(0, 100)
        if random_number < self.reliability:
            return super().drive(distance)
        else:
            return 0  # Car didn't drive any distance
