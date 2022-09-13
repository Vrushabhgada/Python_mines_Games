#importing modules
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import Config
import random
from pprint import pprint

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', '0')
 
# fix the width of the window
Config.set('graphics', 'width', '700')
 
# fix the height of the window
Config.set('graphics', 'height', '700')
# Screen manger 
screen_manager = ScreenManager()


class FirstWindow(Screen):
    def __init__(self, **kwargs):
        super(FirstWindow,self).__init__(**kwargs)
# Adding the first row with the title
        layout1 = GridLayout(cols=1)
        layout1.add_widget(Label(text ="Wellcome to play game",font_size= 50, color =[117/255, 215/255, 255/255, 1]))
# Adding the second row for the option
        layout11=GridLayout(cols = 3)
        layout11.add_widget(Label())
        b1=Button(text="5x5",font_size=30,color=[0,0,0,1],background_color =[117/255, 215/255, 255/255, 1],on_press=self.ClickFive)
        layout11.add_widget(b1)
        layout11.add_widget(Label())
        layout1.add_widget(layout11)
# Adding and empty row
        layout11=GridLayout()
        layout11.add_widget(Label())
        layout1.add_widget(layout11)
# Adding the full layout to screen
        self.add_widget(layout1)
# Change the screen if 5x5 button is pressed
    def ClickFive(self,buttonid):
        self.parent.current="FivexFive"


class EndgameScreen(Screen):
    def __init__(self, **kwargs):
        super(EndgameScreen,self).__init__(**kwargs)
# Adding the first row with the title
        layout1 = GridLayout(cols=1)
        layout1.add_widget(Label(text ="Game Ended",font_size= 50, color =[117/255, 215/255, 255/255, 1]))
# Adding the second row for the option
        layout11=GridLayout(cols = 5)
        layout11.add_widget(Label())
        b1=Button(text="Retry",font_size=30,color=[0,0,0,1],background_color =[117/255, 215/255, 255/255, 1],on_press=self.ClickFive)
        layout11.add_widget(b1)
        layout11.add_widget(Label())
        b1=Button(text="Quit",font_size=30,color=[0,0,0,1],background_color =[117/255, 215/255, 255/255, 1],on_press=self.Quit)
        layout11.add_widget(b1)
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

    def ClickFive(self,buttonid):
        self.parent.current="FivexFive"
    def Quit(self,buttonid):
        quit()

class wongame(Screen):
    def __init__(self, **kwargs):
        super(wongame,self).__init__(**kwargs)
# Adding the first row with the title
        layout1 = GridLayout(cols=1)
        layout1.add_widget(Label(text ="You won the game",font_size= 50, color =[117/255, 215/255, 255/255, 1]))
# Adding the second row for the option
        layout11=GridLayout(cols = 5)
        layout11.add_widget(Label())
        b1=Button(text="New game",font_size=30,color=[0,0,0,1],background_color =[117/255, 215/255, 255/255, 1],on_press=self.ClickFive)
        layout11.add_widget(b1)
        layout11.add_widget(Label())
        b1=Button(text="Quit",font_size=30,color=[0,0,0,1],background_color =[117/255, 215/255, 255/255, 1],on_press=self.Quit)
        layout11.add_widget(b1)
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

    def ClickFive(self,buttonid):
        self.parent.current="FivexFive"
    def Quit(self,buttonid):
        quit()

class FivexFive(Screen):
    def __init__(self, **kwargs):
        super(FivexFive,self).__init__(**kwargs)
        layout1 = GridLayout(cols=1)
        layout11=GridLayout(cols=2)
        layout11.add_widget(Label(text ="lets play 5x5",font_size= 50, color =[117/255, 215/255, 255/255, 1]))
        b1=Button(text="Back to main page",font_size=30,color=[0,0,0,1],background_color =[117/255, 215/255, 255/255, 1],on_press=self.back)
        layout11.add_widget(b1)
        layout1.add_widget(layout11)
        layout1.add_widget(Label())
        buttonnumber=0
        
        for i in range(1,6):
            rowbutton=GridLayout(cols=7)
            rowbutton.add_widget(Label())
            for j in range(1,6):
                bb=Button(background_color =[0.8, 0.8, 0.8, 1],color=[0,0,0,1],on_press=self.check)
                self.ids[buttonnumber]=bb
                rowbutton.add_widget(bb)
                buttonnumber+=1
            rowbutton.add_widget(Label())
            layout1.add_widget(rowbutton)

        self.endlaout=Label(color=[0,0,0,1],font_size=50)
        layout1.add_widget(self.endlaout)
        self.new5x5play()


        self.add_widget(layout1)
    def back(self,buttonid):
        self.new5x5play()
        self.parent.current="FirstWindow"
    def check(self,buttonid):
        # Checking if button which play has pressed
        for key, value in self.ids.items():
            if buttonid == value:
                y=key//5
                x=key%5
                value=(self.playlist[y][x])
                # has player pressed the button with mine
                if value>15:
                    buttonid.background_color=[1,0,0,1]
                    self.new5x5play()
                    self.parent.current="EndgameScreen"
                # has player pressed an empty button
                elif value==0:
                    buttonid.text="0"
                    buttonid.background_color=[0,1,0,1]
                    # Check all the surround button in every direction until border or the number is encounterd
                    self.checkedlist=[]
                    self.checkedvalue=[]
                    if x+1<5:
                        self.checkedlist.append([x+1,y])
                        self.checkedvalue.append([x+1,y])
                    if x-1>-1:
                        self.checkedlist.append([x-1,y])
                        self.checkedvalue.append([x-1,y])
                    if y+1<5:
                        self.checkedlist.append([x,y+1])
                        self.checkedvalue.append([x,y+1])
                    if y-1>-1:
                        self.checkedlist.append([x,y-1])
                        self.checkedvalue.append([x,y-1])
                    
                    while len(self.checkedlist)!=0:
                        [x,y]=(self.checkedlist.pop())
                        value=(self.playlist[y][x])

                        plbutton=self.ids[y*5+x]
                        
                        if value==0:
                            plbutton.text="0"
                            plbutton.background_color=[0,1,0,1]
                            if x+1<5 and self.checkedvalue.count([x+1,y])==0:
                                self.checkedlist.append([x+1,y])
                                self.checkedvalue.append([x+1,y])
                            if x-1>-1 and self.checkedvalue.count([x-1,y])==0:
                                self.checkedlist.append([x-1,y])
                                self.checkedvalue.append([x-1,y])
                            if y+1<5 and self.checkedvalue.count([x,y+1])==0:
                                self.checkedlist.append([x,y+1])
                                self.checkedvalue.append([x,y+1])
                            if y-1>-1 and self.checkedvalue.count([x,y-1])==0:
                                self.checkedlist.append([x,y-1])
                                self.checkedvalue.append([x,y-1])
                        else:
                            plbutton.text=str(value)
                            plbutton.background_color=[0,1,0,1]
                    self.checkedvalue=[]
                    self.checkedlist=[]
                #has player pressed the button with number on it
                else :
                    buttonid.background_color=[0,1,0,1]
                    buttonid.text=str(value)
                break
        
#Checking if the play is won or not
        counter=0
        for key, value in self.ids.items():
            if value.text!="":
                counter+=1
        print("Printing Counter"+str(counter))
        if counter==22:
            print("YOU won the game")
            self.new5x5play()
            self.parent.current="wongame"
                    

    def new5x5play(self):
# creating the new game play using random        
        self.endlaout.text=""
        randomlist = random.sample(range(0, 24), 3)
        self.playlist=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        for k in randomlist:
            i=k//5
            j=k%5
            self.playlist[i][j]=20
            if (i-1)>-1:
                self.playlist[i-1][j]+=1
            if (j-1)>-1:
                self.playlist[i][j-1]+=1
            if (j-1)>-1 and (i-1)>-1:
                self.playlist[i-1][j-1]+=1

            if (j-1)>-1 and (i+1)<5:
                self.playlist[i+1][j-1]+=1
            if (j+1)<5 and (i-1)>-1:
                self.playlist[i-1][j+1]+=1

            if (i+1)<5:
                self.playlist[i+1][j]+=1
            if (j+1)<5:
                self.playlist[i][j+1]+=1
            if (j+1)<5 and (i+1)<5:
                self.playlist[i+1][j+1]+=1
        for key, value in self.ids.items():
            value.text=""
            value.background_color=[0.8,0.8,0.8,1]
        pprint(self.playlist)

# Screen added to screen mangaer
screen_manager.add_widget(FirstWindow(name ="FirstWindow"))
screen_manager.add_widget(FivexFive(name ="FivexFive"))
screen_manager.add_widget(EndgameScreen(name ="EndgameScreen"))
screen_manager.add_widget(wongame(name ="wongame"))

class Mines(App):
    def build(self):
        Window.clearcolor=(1,1,1,1)
        return screen_manager

if __name__ == "__main__":
    print("in")
    Mines().run()