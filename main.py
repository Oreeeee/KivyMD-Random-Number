# Import libraries
from kivymd.app import MDApp
from kivy.lang import Builder as KivyBuilder
from kivy.uix.screenmanager import Screen as KivyScreen
from kivy.uix.screenmanager import ScreenManager as KivyScreenManager
import random

# Make a classes for screens
class MainScreen(KivyScreen):
    def accept_input(self, min_random_value, max_random_value, root):
        global kivyapp_min_random_value
        global kivyapp_max_random_value

        try:
            kivyapp_min_random_value = int(min_random_value)
            self.manager.get_screen(
                "main_screen").ids.min_random_value.error = False
            self.manager.get_screen(
                "main_screen").ids.min_random_value.helper_text = ""
        except ValueError:
            self.manager.get_screen(
                "main_screen").ids.min_random_value.error = True
            self.manager.get_screen(
                "main_screen").ids.min_random_value.helper_text = "This field must be a number!"
            return

        try:
            kivyapp_max_random_value = int(max_random_value)
            self.manager.get_screen(
                "main_screen").ids.max_random_value.error = False
            self.manager.get_screen(
                "main_screen").ids.max_random_value.helper_text = ""
        except ValueError:
            self.manager.get_screen(
                "main_screen").ids.max_random_value.error = True
            self.manager.get_screen(
                "main_screen").ids.max_random_value.helper_text = "This field must be a number!"
            return

        if kivyapp_max_random_value < kivyapp_min_random_value:
            self.manager.get_screen(
                "main_screen").ids.max_random_value.error = True
            self.manager.get_screen(
                "main_screen").ids.max_random_value.helper_text = "Max value must be larger than min value"
            return

        root.manager.current = 'generation_screen'


class GenerationScreen(KivyScreen):
    def generate_number(self):
        random_number = random.randrange(
            kivyapp_min_random_value, kivyapp_max_random_value + 1)
        self.manager.get_screen(
            "generation_screen").ids.number_label.text = f"Your random number is: {random_number}"


# Initialize ScreenManager and add screens to that ScreenManager
sm = KivyScreenManager()
sm.add_widget(GenerationScreen(name="main_screen"))
sm.add_widget(GenerationScreen(name="generation_screen"))


class RandomNumberApp(MDApp):

    def build(self):
        return KivyBuilder.load_file("app.kv")


# Start the app
if __name__ == "__main__":
    RandomNumberApp().run()
