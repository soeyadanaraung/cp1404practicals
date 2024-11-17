# class Monitor:
#     """A class representing a monitor with model, width, and height attributes."""
#
#     def __init__(self, model: str, width: int, height: int):
#         """Initialize the Monitor with model, width, and height."""
#         self.model = model
#         self.width = width
#         self.height = height
#
#     def get_resolution(self) -> tuple:
#         """Return (width, height)."""
#         return self.width, self.height
#
#     def get_total_pixels(self) -> int:
#         """Return (width * height) for the monitor."""
#         return self.width * self.height

class Monitor:
    def _init_(self, width, height):
        self.width = width
        self.height = height

    def is_equal(self, other):
        return self.width == other.width and self.height == other.height

monitor1 = Monitor(1920, 1080)
monitor2 = Monitor(1920, 1080)
monitor3 = Monitor(1280, 720)

print(monitor1.is_equal(monitor2))  # Expected: True
print(monitor1.is_equal(monitor3))  # Expected: False
