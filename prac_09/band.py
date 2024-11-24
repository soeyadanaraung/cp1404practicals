from musician import Musician

class Band:
    """Class representing a band that has musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Ask each musician in the band to play."""
        for musician in self.musicians:
            print(musician.play())

    def __str__(self):
        """Return a string representation of the band and its musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"
