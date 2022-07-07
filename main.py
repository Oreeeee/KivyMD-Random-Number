# Import libraries
from kivymd.app import MDApp
from kivy.lang import Builder as KivyBuilder
from kivy.uix.screenmanager import Screen as KivyScreen
from kivy.uix.screenmanager import ScreenManager as KivyScreenManager
import random

# Make a class for a screen
class GenerationScreen(KivyScreen):
    def generate_number(self):
        random_number = random.randrange(1, 100)
        self.manager.get_screen("main_screen").ids.number_label.text = f"Your random number is: {random_number}"
        print(random_number)

# Initialize ScreenManager and add GenerationScreen to that ScreenManager
sm = KivyScreenManager()
sm.add_widget(GenerationScreen(name="main_screen"))

class RandomNumberApp(MDApp):

    def build(self):
        return KivyBuilder.load_file("app.kv")

    

# Start the app
if __name__ == "__main__":
    RandomNumberApp().run()