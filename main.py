from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
# from kivy.uix.slider import Slider


# Designate our .kv design file
Builder.load_file('25_slider.kv')


class MyLayout(Widget):
    def slide_it(self, *args):
        self.slide_text.text = str(int(args[1]))
        self.slide_text.font_size = str(int(args[1]) * 5)


class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp ().run()
