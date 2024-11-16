from kivy.app import App
from classes import MainLayout

class ShoppingApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    ShoppingApp().run()



