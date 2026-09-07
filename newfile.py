from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import webbrowser

Window.clearcolor = (0, 0, 0, 1)


class Calculator(App):

    def build(self):

        self.exp = ""

        root = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )


        self.display = Label(
            text="0",
            font_size=55,
            size_hint_y=0.25
        )

        root.add_widget(equal)


           telegram = Button(
    text="Telegram",
    font_size=25,
    size_hint_y=0.10,
    background_normal="",
    background_color=(0.05,0.35,0.8,1)
)

def open_telegram(instance):
    try:
        import webbrowser
        webbrowser.open(
            "https://t.me/AnasX_Top"
        )
    except:
        pass

telegram.bind(
    on_press=open_telegram
)

root.add_widget(telegram)

        grid = GridLayout(
            cols=4,
            spacing=8
        )


        keys = [
            "AC","DEL","%","/",
            "7","8","9","*",
            "4","5","6","-",
            "1","2","3","+",
            "(","0",")","."
        ]


        for key in keys:

            if key in ["+","-","*","/"]:
                color = (1,0.45,0.05,1)
                size = 42

            elif key in ["AC","DEL"]:
                color = (0.8,0.1,0.1,1)
                size = 25

            else:
                color = (0.18,0.18,0.22,1)
                size = 30


            btn = Button(
                text=key,
                font_size=size,
                background_normal="",
                background_color=color
            )

            btn.bind(
                on_press=self.press
            )

            grid.add_widget(btn)


        root.add_widget(grid)


        equal = Button(
            text="=",
            font_size=40,
            size_hint_y=0.15,
            background_normal="",
            background_color=(0.05,0.7,0.3,1)
        )


        equal.bind(
            on_press=self.press
        )


        root.add_widget(equal)


        return root



    def press(self, btn):

        key = btn.text


        if key == "AC":

            self.exp = ""


        elif key == "DEL":

            self.exp = self.exp[:-1]


        elif key == "=":

            try:

                self.exp = str(
                    eval(self.exp)
                )

            except:

                self.exp = "Error"


        else:

            self.exp += key


        self.display.text = (
            self.exp
            if self.exp
            else "0"
        )



Calculator().run()