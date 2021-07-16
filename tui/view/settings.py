from os import name
import asciimatics
import __future__
import curses
from asciimatics.screen import Screen, _CursesScreen
from asciimatics.widgets import * 
from asciimatics.scene import *

our_data = {
    "ddl1": "",
    "ddl2": "",
    "ddl3": "",
}

options_ddl1 = ["COLOUR_BLACK = 0",
    "COLOUR_RED = 1",
    "COLOUR_GREEN = 2",
    "COLOUR_YELLOW = 3",
    "COLOUR_BLUE = 4",
    "COLOUR_MAGENTA = 5",
    "COLOUR_CYAN = 6",
    "COLOUR_WHITE = 7",]
options_ddl2 = options_ddl1
options_ddl3 = options_ddl1
def demo(screen):

    setting_frame = Frame(screen, screen.height, screen.width, has_border=False, title="Setting", data=our_data)
    layout = Layout([1,18,1])

    setting_frame.add_layout(layout)

    layout.add_widget(Divider(draw_line=False, height=screen.height// 3),1)
    layout.add_widget(DropdownList( [],
            label= "foreground",
            name= "ddl1",
            ), 1)
    layout.add_widget(DropdownList( [],
            label= "background",
            name= "ddl2",
            ), 1)
    layout.add_widget(DropdownList( [],
            label= "text",
            name= "ddl3",
            ), 1)
    
    setting_frame.fix()

    scene_list = [
        Scene([setting_frame], -1, name="Settings")
    ]

    screen.play(scene_list)

Screen.wrapper(demo)