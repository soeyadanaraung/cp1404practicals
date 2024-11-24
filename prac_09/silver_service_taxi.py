from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness and flagfall."""

    flagfall = 4.50
    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Calculate the fare for the trip including flag fall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        return f"{super().__str__()}, ${self.price_per_km:.2f}/km plus flag fall of ${self.flagfall:.2f}"
