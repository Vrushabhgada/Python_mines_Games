#importing modules
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', '0')
 
# fix the width of the window
Config.set('graphics', 'width', '500')
 
# fix the height of the window
Config.set('graphics', 'height', '500')
# Screen manger 
screen_manager = ScreenManager()


class FirstWindow(Screen):
    def __init__(self, **kwargs):
        super(FirstWindow,self).__init__(**kwargs)
        WindowHeight=self.height
        layout1 = GridLayout(cols=1)
        layout1.add_widget(Label(text ="Wellcome to play game",font_size= 0.5*self.height, color =[0, 0, 0, 1]))

        layout11=GridLayout(cols = 5)
        layout11.add_widget(Label())
        layout11.add_widget(Button(background_normal="5.png", color =[0, 0, 0, 1]))
        layout11.add_widget(Label())
        layout11.add_widget(Button(text ="9x9", color =[0, 0, 0, 1]))
        layout11.add_widget(Label())
        layout1.add_widget(layout11)

        layout11=GridLayout(cols = 5)
        layout11.add_widget(Label())
        layout11.add_widget(Label())
        layout11.add_widget(Label())
        layout11.add_widget(Label())
        layout11.add_widget(Label())
        layout1.add_widget(layout11)

        layout11=GridLayout(cols = 5)
        layout11.add_widget(Label())
        layout11.add_widget(Button(text ="16x16", color =[0, 0, 0, 1]))
        layout11.add_widget(Label())
        layout11.add_widget(Button(text ="20x20", color =[0, 0, 0, 1]))
        layout11.add_widget(Label())
        layout1.add_widget(layout11)

        layout11=GridLayout(cols = 5)
        layout11.add_widget(Label())
        layout11.add_widget(Label())
        layout11.add_widget(Label())
        layout11.add_widget(Label())
        layout11.add_widget(Label())
        layout1.add_widget(layout11)


        self.add_widget(layout1)



# Screen added to screen mangaer
screen_manager.add_widget(FirstWindow(name ="FirstWindow"))

 

class Mines(App):
    def build(self):
        Window.clearcolor=(1,1,1,1)
        return screen_manager

if __name__ == "__main__":
    print("in")
    Mines().run()