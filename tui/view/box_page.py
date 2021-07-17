from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from asciimatics.particles import SerpentFirework,ParticleEmitter
from asciimatics.paths import Path
from asciimatics.widgets import Frame,Layout,Button,Label,widget,TextBox,Divider,VerticalDivider,PopupMenu,Widget
from time import sleep
import requests as req
import json
from Settings import Settings
import sys

 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       
#QUERRY TO FILL BOX DICT {"KEY":"boxid", "VALUE":"BOX NAME"}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
box={ "1" : "SHOWER THOUGHTS",
          "2" :  "BIG BRAINERS",
          "3" :  "WHY WORLD",
          "4" : "SCIENCE CAN SMD",
          "5": "SOZ FOR THE WIERD NAMES BOIS ITS 1AM IM DEAD ON THE INSIDE"}

class BoxPage(Frame):

    def __init__(self, screen):

        super().__init__(screen, screen.height , screen.width )
        global box
        hgt=screen.height
        wdt=screen.width
        layout = Layout([100])
        self.add_layout(layout)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ adding title of page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self._page_title = Label("BOX's",align="^")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
        layout.add_widget(self._page_title)
        layout3 = Layout([1,1,1,1,1])
        col=[]
        for i in range(0,len(box)):
                for i in range (1,3): col.append(1)
        layout2=Layout(col)
        self.add_layout(layout2)
        self.add_layout(layout3)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ adding boxs at in the middle~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        h_pos=1
        y_pos=1
        cnt=1
        for key in list(box.keys()):
            y_pos+=1
            if(cnt==2):
                h_pos+=1
                y_pos=1
                cnt=1
                layout2.add_widget(Label(""))
                layout2.add_widget(VerticalDivider(height=1),y_pos+1)
                layout2.add_widget(Divider(height=1),y_pos)
                layout2.add_widget(Label(box.get(key),align="^"),y_pos)
                layout2.add_widget(VerticalDivider(height=1),y_pos+1)
                layout2.add_widget(Divider(height=1),y_pos)
##                layout2.add_widget(Button(box.get(key),self._onclickbox(),y_pos))
            cnt+=1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ adding buttons at bottom~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~          
        layout3.add_widget(Button("Settings", self._onclick_pgsettings), 0)
        layout3.add_widget(Button("Load More", self._onclick_loadmore), 1)
        layout3.add_widget(Button("Refresh", self._onclick_refresh), 2)
        layout3.add_widget(Button("Create New Box", self._onclick_newbx), 3)
        layout3.add_widget(Button("Quit",self._onclick_quit),4)
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        

        self.fix()

    def _onclick_loadmore(self):
            global box

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
#LOAD MORE QUERY REQUIRED:
            box={"1":"yes ",
                     "2":"no"}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
            raise NextScene("BoxPage")
        
    def _onclick_refresh(self):
        global box
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
#REFRESH QUERY REQUIRED
        box={"1":"HESUS I REFRESHED",
        " 2": "GOD PLS LET ME SLEEP",
        " 3" : "random discord moments smh"}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
        raise NextScene("BoxPage")
        
    def _onclick_pgsettings(self):
            raise NextScene("Settings")

    def _onclick_newbx(self):   
            raise NextScene("NewBoxPage")

##    def _onclickbox(self):
##                
####            BoxTest.name=box.get(b_id)
####            BoxTest.b_id=b_id
##            return
        
    def _onclick_quit(self):
            raise StopApplication("usr prssed exit")

class NewBoxPage(Frame):

    def __init__(self, screen):

        super().__init__(screen, screen.height , screen.width )
        layout5=Layout([100])
    

        layout6.add_widget(Button("Create",self._onclick_create),0)
        layout6.add_widget(Button("Cancel",self._onclick_cancel),1)


    def _onclick_create(self):
                return
    def _onclick_cancel(self):
                raise NextScene("BoxPage")


##class BoxTest(Frame):
##    name,b_id="",""    
##    def __init__(self, screen):
##
##        super().__init__(screen, screen.height , screen.width )
##        global box
##        hgt=screen.height
##        wdt=screen.width
##        layout = Layout([100], fill_frame=True)
##        self.add_layout(layout)
##        self._page_title = Label("box id: ",b_id,"Box name:" ,name)
##        layout2=Layout([2,2])
##        layout2.add_widget(Button("Back",self._onclick_back),1)
##    def _onclick_back():
##             raise NextScene("BoxPage")
##              
##        

def main(screen, scene):
    scenes = [
        Scene([BoxPage(screen)], -1, name="BoxPage"),
##        Scene([BoxTest(screen)], -1, name="BoxTest"),
        Scene([Settings(screen)], -1, name="Settings"),
        Scene([NewBoxPage(screen)], -1, name="NewBoxPage")
    ]
    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)






if __name__ == "__main__":
    last_scene = None
    while True:
        try:
            Screen.wrapper(main, catch_interrupt=True, arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError as e:
            last_scene = e.scene
