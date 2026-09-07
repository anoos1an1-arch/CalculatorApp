from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
from kivy.graphics import RoundedRectangle, Color
import webbrowser

Window.clearcolor = (0.04, 0.04, 0.06, 1)


class ModernButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 0.05)
            self.rect = RoundedRectangle(radius=[20])
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class Calculator(App):
    def build(self):
        self.exp = ""
        self.history = []

        root = BoxLayout(orientation="vertical", padding=15, spacing=10)

        root.add_widget(Label(text="CALCULATOR", font_size=32, size_hint_y=0.08))

        self.display = Label(text="0", font_size=60, size_hint_y=0.20)
        root.add_widget(self.display)

        self.history_label = Label(text="History", font_size=16, size_hint_y=0.10)
        root.add_widget(self.history_label)

        grid = GridLayout(cols=4, spacing=8)

        keys = [
            "AC","DEL","COPY","/",
            "7","8","9","*",
            "4","5","6","-",
            "1","2","3","+",
            "(","0",")","."
        ]

        for key in keys:
            if key in ["+","-","*","/"]:
                color = (1,0.5,0.1,1)
                size = 42
            elif key in ["AC","DEL","COPY"]:
                color = (0.9,0.2,0.2,1)
                size = 22
            else:
                color = (0.15,0.15,0.2,1)
                size = 30

            btn = ModernButton(
                text=key,
                font_size=size,
                background_normal="",
                background_color=color
            )
            btn.bind(on_press=self.press)
            grid.add_widget(btn)

        root.add_widget(grid)

        equal = ModernButton(
            text="=",
            font_size=48,
            size_hint_y=0.12,
            background_normal="",
            background_color=(0.1,0.8,0.35,1)
        )
        equal.bind(on_press=self.press)
        root.add_widget(equal)

        telegram = ModernButton(
            text="Telegram",
            font_size=25,
            size_hint_y=0.08,
            background_normal="",
            background_color=(0.05,0.35,0.8,1)
        )
        telegram.bind(on_press=self.open_telegram)
        root.add_widget(telegram)

        return root

    def open_telegram(self, instance):
        webbrowser.open("https://t.me/AnasX_Top")

    def press(self, btn):
        key = btn.text

        if key == "AC":
            self.exp = ""
        elif key == "DEL":
            self.exp = self.exp[:-1]
        elif key == "COPY":
            Clipboard.copy(self.exp)
        elif key == "=":
            try:
                old = self.exp
                self.exp = str(eval(self.exp))
                self.history.append(old + " = " + self.exp)
                self.history_label.text = "History:\n" + "\n".join(self.history[-3:])
            except:
                self.exp = "Error"
        else:
            self.exp += key

        self.display.text = self.exp if self.exp else "0"


Calculator().run()
