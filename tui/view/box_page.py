# flake8: noqa

from time import sleep

from asciimatics.exceptions import (
    NextScene, ResizeScreenError, StopApplication
)
from asciimatics.particles import ParticleEmitter, SerpentFirework
from asciimatics.paths import Path
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Button, Frame, Label, Layout, widget

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
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ adding title of page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self._page_title = Label("BOX's")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        layout.add_widget(self._page_title)
        layout3 = Layout([3,3,3])
        layout2=Layout([int(wdt/5),int(wdt/5),int(wdt/5),int(wdt/5),int(wdt/5)])
        self.add_layout(layout2)
        self.add_layout(layout3)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ adding boxs at in the middle~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        h_pos=1
        y_pos=0
        cnt=1
        for key in list(box.keys()):
            y_pos+=1
            if(cnt==5):
                h_pos+=1
                y_pos=0
                cnt=1
            layout2.add_widget(Button(str(box.get(key)),self._onclickbox(b_id=key),y_pos))
            cnt+=1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ adding buttons at bottom~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        layout3.add_widget(Button("Settings", self._onclick_pgsettings), 0)
        layout3.add_widget(Button("Load More", self._onclick_loadmore), 1)
        layout3.add_widget(Button("Refresh", self._onclick_refresh), 2)
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
    
    def _onclickbox(b_id=0):
            BoxTest.name=box.get(b_id)
            BoxTest.b_id=b_id
            raise NextScene("BoxTest")

    def _onclick_pgsettings(self):
            #settings page undiscussed daddy cool knows
            raise NextScene("Settings")
    def _onclickbox(b_id=0):
            BoxTest.name=box.get(b_id)
            BoxTest.b_id=b_id
            raise NextScene("BoxTest")

def main(screen, scene):
    scenes = [
        Scene([BoxPage(screen)], -1, name="BoxPage")
    ]
    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)



class BoxTest(Frame):
    name,b_id="",""
    def __init__(self, screen):

        super().__init__(screen, screen.height , screen.width )
        global box
        hgt=screen.height
        wdt=screen.width
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        self._page_title = Label("box id: ",b_id,"Box name:" ,name)
        layout2=Layout([2,2])
        layout2.add_widget(Button("Back",self._onclick_back),1)
    def _onclick_back():
             raise NextScene("BoxPage")




if __name__ == "__main__":
    last_scene = None
    while True:
        try:
            Screen.wrapper(main, catch_interrupt=True, arguments=[last_scene])
        except ResizeScreenError as e:
            last_scene = e.scene
