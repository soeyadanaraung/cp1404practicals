from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

class MainLayout(BoxLayout):
    total_price = NumericProperty(0)

    def add_to_total(self, price):
        """Increase the total price by the selected item's price."""
        self.total_price += price

    def reset_total(self):
        """Reset the total price to 0."""
        self.total_price = 0

