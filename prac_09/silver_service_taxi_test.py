from prac_09.taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    """Test the SilverServiceTaxi class."""

    fancy_taxi = SilverServiceTaxi("Hummer", 200, 2)
    fancy_taxi.drive(18)

    print(fancy_taxi)
    print(f"Fare for 18 km: ${fancy_taxi.get_fare():.2f}")

    expected_fare = 18 * (Taxi.price_per_km * 2) + SilverServiceTaxi.flagfall
    assert abs(fancy_taxi.get_fare() - expected_fare) < 0.01, "Fare calculation is incorrect!"

if __name__ == "__main__":
    main()
