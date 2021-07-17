from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from asciimatics.particles import SerpentFirework,ParticleEmitter
from asciimatics.paths import Path
from asciimatics.widgets import Frame,Layout,Button,Label,widget,TextBox,Divider,VerticalDivider,PopupMenu,Widget,DropdownList
from time import sleep
import requests as req
import json
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
        layout4 = Layout([1,1,1,1,1])
        col=[]
        for i in range(0,len(box)):
                for i in range (1,3): col.append(1)
        layout2=Layout(col)
        layout3=Layout(col)
        self.add_layout(layout3)
        self.add_layout(layout2)
        self.add_layout(layout4)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ adding boxs at in the middle~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        h_pos=1
        y_pos=1
        cnt=1
        for key in list(box.keys()):
            layout=layout2

            y_pos+=1
            if(cnt==2):
                h_pos+=1
                y_pos=1
                cnt=1
            if(h_pos>1):
                    layout=layout3                
            layout.add_widget(Label(""))
            layout.add_widget(Divider(height=1),y_pos)
            layout.add_widget(Label(box.get(key),align="<"),y_pos)
 
            layout2.add_widget(Divider(height=1),y_pos)
##                layout2.add_widget(Button(box.get(key),self._onclickbox(),y_pos))
            cnt+=1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ adding buttons at bottom~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~          
        layout4.add_widget(Button("Settings", self._onclick_pgsettings), 0)
        layout4.add_widget(Button("Load More", self._onclick_loadmore), 1)
        layout4.add_widget(Button("Refresh", self._onclick_refresh), 2)
        layout4.add_widget(Button("Create New Box", self._onclick_newbx), 3)
        layout4.add_widget(Button("Quit",self._onclick_quit),4)
        
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
        layout5=Layout([1,1])
    
        self.add_layout(layout5)
        layout5.add_widget(Button("Create",self._onclick_create),0)
        layout5.add_widget(Button("Cancel",self._onclick_cancel),1)


    def _onclick_create(self):
                return
    def _onclick_cancel(self):
                raise NextScene("BoxPage")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SETTINGS CODE (DADDY COOL)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from asciimatics.screen import Screen
# from asciimatics.scene import Scene
# from time import sleep
from asciimatics.widgets import Divider, DropdownList, Frame, Layout, Button
from asciimatics.exceptions import NextScene

settings_data = {
    "fg": "",
    "bg": "",
    "txt": ""
}

options_ddl1 = ["COLOUR_BLACK = 0",
                "COLOUR_RED = 1",
                "COLOUR_GREEN = 2",
                "COLOUR_YELLOW = 3",
                "COLOUR_BLUE = 4",
                "COLOUR_MAGENTA = 5",
                "COLOUR_CYAN = 6",
                "COLOUR_WHITE = 7"
                ]
options_ddl2 = options_ddl1
options_ddl3 = options_ddl1


class Settings(Frame):

    """
    This class will display the setting pane.
    If you want to get access to data you can use the `get_settings` function or access `settings_data` dictionary.
    """

    def __init__(self, screen: Screen) -> None:
        global settings_data
        super().__init__(screen, screen.height, screen.width,
                         has_border=False, title="Setting", data=settings_data, name="settings_form")
        layout = Layout([1, 18, 1])

        self.add_layout(layout)

        layout.add_widget(Divider(draw_line=False, height=screen.height // 3), 1)
        layout.add_widget(DropdownList([(x, i) for i, x in enumerate(options_ddl1)],
                                       label="foreground",
                                       name="fg",
                                       on_change=self._on_change,
                                       ), 1)
        layout.add_widget(DropdownList([(x, i) for i, x in enumerate(options_ddl2)],
                                       label="background",
                                       name="bg",
                                       on_change=self._on_change,
                                       ), 1)
        layout.add_widget(DropdownList([(x, i) for i, x in enumerate(options_ddl3)],
                                       label="text",
                                       name="txt",
                                       on_change=self._on_change,
                                       ), 1)

        # adding divider
        layout2 = Layout([10])
        self.add_layout(layout2)

        layout2.add_widget(Divider(draw_line=False, height=5))

        # adding the button
        layout3 = Layout([1, 1, 3])
        self.add_layout(layout3)

        layout3.add_widget(Button('back', on_click=self._on_back), 2)

        self.fix()

    def _on_change(self) -> None:
        self.save()
        global settings_data
        settings_data = self.data

    def _on_back(self) -> None:
        raise NextScene("BoxPage")


def get_settings() -> dict:
    """This will return the settings data collected"""
    return settings_data

# while True:
#     def demo(screen):
#         x = Scene([Settings(screen)], 150, name="Settings")
#         screen.play([x], repeat=False)
#         # st = settings_data["ddl1"]+', '+settings_data["ddl2"]+', '+settings_data["ddl3"]
#         screen.clear()
#         screen.refresh()
#         screen.print_at(settings_data,0,0)
#         screen.refresh()
#         sleep(10)
#     Screen.wrapper(demo)

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
