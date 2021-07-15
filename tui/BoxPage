from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from asciimatics.particles import SerpentFirework,ParticleEmitter
from asciimatics.paths import Path
from asciimatics.widgets import Frame,Layout,Button,Label,widget
from time import sleep
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
        y_pos=1
        cnt=1
        for key in list(box.keys()):
            y_pos+=1
            if(cnt==5):
                h_pos+=1
                y_pos=1
                cnt=1
            layout2.print_at(x=h_pos,y=y_pos,text=box.get(key))
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
        
    def _onclick_pgsettings(self):
            #settings page undiscussed daddy cool knows
            raise NextScene("Settings")


def main(screen, scene):
    scenes = [
        Scene([BoxPage(screen)], -1, name="BoxPage")
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
