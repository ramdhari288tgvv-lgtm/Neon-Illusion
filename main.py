__version__ = "1.0"

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Line, Ellipse
from kivy.clock import Clock
from math import sin, cos, pi

class Tunnel(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.t = 0
        with self.canvas:
            Color(0.0, 0.8, 1.0, 1)
            self.rings = [Line(width=2) for _ in range(12)]
            Color(0.2, 0.9, 1, 1)
            self.dot = Ellipse(size=(20, 20))
        Clock.schedule_interval(self.animate, 1 / 60)

    def animate(self, dt):
        self.t += dt
        cx, cy = self.center_x, self.center_y
        self.dot.pos = (cx - 10, cy - 10)
        max_radius = min(self.width, self.height) * 0.65
        for i, ring in enumerate(self.rings):
            p = (i / 12 + self.t * 0.35) % 1
            radius = 20 + p * max_radius
            points = []
            for j in range(81):
                angle = j / 80 * 2 * pi
                r = radius + sin(self.t * 3 + angle * 5) * 5
                points.extend([cx + cos(angle) * r, cy + sin(angle) * r])
            ring.points = points

class MyApp(App):
    def build(self):
        self.root = FloatLayout()
        self.tunnel = Tunnel(size_hint=(1, 1))
        self.root.add_widget(self.tunnel)
        Clock.schedule_once(self.show_main, 3)
        return self.root

    def show_main(self, dt):
        self.root.remove_widget(self.tunnel)
        button = Button(
            text="ENTER",
            font_size="24sp",
            size_hint=(0.6, 0.15),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            background_color=(0.0, 0.7, 1.0, 1)
        )
        button.bind(on_press=self.enter)
        self.root.add_widget(button)

    def enter(self, button):
        button.text = "WELCOME"

MyApp().run()
