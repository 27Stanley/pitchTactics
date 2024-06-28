from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse
import ctypes

class Player(Widget):
    radius = NumericProperty(15)
    color = ListProperty([1,1,1,1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(rgba = self.color)
            self.ellipse = Ellipse(pos=(self.center_x - self.radius, self.center_y - self.radius),
                                   size=(self.radius * 2, self.radius * 2))

        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        self.ellipse.pos = (self.center_x - self.radius, self.center_y - self.radius)
        self.ellipse.size = (self.radius * 2, self.radius * 2)

class PitchTacticsApp(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.team1 = [
            {'x': 100, 'y': 100, 'radius': 20, 'color': (0, 0, 1, 1)},
            {'x': 200, 'y': 100, 'radius': 20, 'color': (0, 0, 1, 1)},
            {'x': 300, 'y': 100, 'radius': 20, 'color': (0, 0, 1, 1)},
            {'x': 400, 'y': 100, 'radius': 20, 'color': (0, 0, 1, 1)},
            
        ]
        self.team2 = [
            {'x': 100, 'y': 1000, 'radius': 20, 'color': (1, 0, 0, 1)},
            {'x': 200, 'y': 1000, 'radius': 20, 'color': (1, 0, 0, 1)},
            {'x': 300, 'y': 1000, 'radius': 20, 'color': (1, 0, 0, 1)},
            {'x': 400, 'y': 1000, 'radius': 20, 'color': (1, 0, 0, 1)},
            
        ]

        self.setup_players()

    def setup_players(self):
        for player_data in self.team1 + self.team2:
            player = Player(pos=(player_data['x'], player_data['y']),
                            radius=player_data['radius'],
                            color=player_data['color'])
            self.add_widget(player)

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