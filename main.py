from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.core.window import Window
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

import ctypes

class PitchTacticsApp(Widget):
    pass

class FootballApp(App):
    def build(self):
        Window.size = (810, 1200)

        # Get the screen width and height using ctypes
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)

        print(screen_height, screen_width)

        # Calculate the position to center the window
        window_x = screen_width // 2
        window_y = 100

        print(window_x, window_y)

        # Set the window position to center it on the screen
        Window.right = window_x
        Window.top = window_y
        return PitchTacticsApp()
    

if __name__ == "__main__":
    FootballApp().run()