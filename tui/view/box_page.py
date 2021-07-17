# flake8: noqa
# from tui.__main__ import BoxSelection
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from asciimatics.particles import SerpentFirework,ParticleEmitter
from asciimatics.paths import Path
from asciimatics.widgets import Frame,Layout,Button,Label,widget,TextBox,Divider,VerticalDivider,PopupMenu,Widget,DropdownList, ListBox
from time import sleep
from asciimatics.event import KeyboardEvent
from tui.view.settings import Settings, get_settings
import requests as req
import json
import sys


box={ 1 : "SHOWER THOUGHTS",
      2 :  "BIG BRAINERS",
      3 :  "WHY WORLD",
      4 : "SCIENCE CAN SMD",
      5 : "SOZ FOR THE WIERD NAMES BOIS ITS 1AM IM DEAD ON THE INSIDE"}

class BoxPage(Frame):

    def __init__(self, screen, box_selection):

        super().__init__(screen, screen.height*2//3, screen.width*2//3, hover_focus=True, can_scroll=True)
        global box

        self._box_selection = box_selection

        scr_height = screen.height
        scr_width = screen.width

        # Box layout
        box_layout = Layout([100], fill_frame=True)
        self.add_layout(box_layout)
        self._page_title = Label("BOXs available", align="^")
        box_layout.add_widget(self._page_title)

        box_list = []
        for i in box:
            box_list.append(box[i])

        list_box = ListBox(
            Widget.FILL_FRAME,
            [(box_list[i], i) for i in range(len(box_list))],
            name="box_name",
            add_scroll_bar=True,
            on_change=self._on_pick,
            on_select=self._edit,
        )
        box_layout.add_widget(list_box)


        # divider
        # divider_layout = Layout([100])
        # self.add_layout(divider_layout)
        # # TODO - div_height change
        # div_height = 3
        # divider_layout.add_widget(Divider(draw_line=False, height=div_height))

        # adding ending_buttons
        ending_buttons_layout = Layout([1,1,1,1,1])
        self.add_layout(ending_buttons_layout)
        ending_buttons_layout.add_widget(Button("Settings", self._onclick_pgsettings), 0)
        ending_buttons_layout.add_widget(Button("Load More", self._onclick_loadmore), 1)
        ending_buttons_layout.add_widget(Button("Refresh", self._onclick_refresh), 2)
        ending_buttons_layout.add_widget(Button("Create New Box", self._onclick_newbx), 3)
        ending_buttons_layout.add_widget(Button("Quit" , self._onclick_quit), 4)
        

        self.fix()

    def _onclick_loadmore(self):
            global box

            box={"1":"yes ",
                     "2":"no"}
            raise NextScene("BoxPage")
        
    def _onclick_refresh(self):
        global box
        box={"1":"HESUS I REFRESHED",
        " 2": "GOD PLS LET ME SLEEP",
        " 3" : "random discord moments smh"}
        raise NextScene("BoxPage")
        
    def _onclick_pgsettings(self):
            raise NextScene("Settings")

    def _onclick_newbx(self):   
            raise NextScene("NewBoxPage")

    def _onclick_quit(self):
            raise StopApplication("usr prssed exit")

    def _edit(self):
        self.save()
        self._model.current_id = self.data["box_name"]
        raise NextScene("ChatPage")

    def _on_pick(self):
        pass


class BoxButtons(Button):
    def __init__(self, title, id, url=''):
        self.title = title
        self.id = id
        self.url = url
        super().__init__(self.title, self._on_click)
    
    def _on_click():
        # call url or from id
        pass


newboxdata = {}

class NewBoxPage(Frame):

    def __init__(self, screen, box_selection):
        
        super().__init__(screen, screen.height*2//3, screen.width*2//3, data=newboxdata)
        
        self.box_selection = box_selection

        enter_name = Layout([1], fill_frame=True)
        self.add_layout(enter_name)
        enter_name.add_widget(TextBox(1, label="Enter box name: ", name="box_name", on_focus=self._focus_on_text))

        newbox_buttons = Layout([1, 1])

        self.add_layout(newbox_buttons)
        newbox_buttons.add_widget(Button("Create", self._onclick_create, on_focus=self._focus_not_on_text), 0)
        newbox_buttons.add_widget(Button("Cancel", self._onclick_cancel, on_focus=self._focus_not_on_text), 1)

        self.fix()


    def _onclick_create(self):
        self.save()
        newboxdata = self.data
        self.box_selection.new_box(newboxdata)
        raise NextScene("ChatPage")
    def _onclick_cancel(self):
        raise NextScene("BoxPage")
    def _onclick_quit(self):
        raise StopApplication("usr prssed exit")

    def _focus_on_text(self):
        self.data['is_on_text'] = True

    def _focus_not_on_text(self):
        self.data['is_on_text'] = False

    def process_event(self, event):
        if isinstance(event, KeyboardEvent):
            if event.key_code in [Screen.ctrl("c")]:
                raise StopApplication("User quit")
            if event.key_code in [10, 13]:
                # self.save()
                if self.data['is_on_text']:
                    self._chat_data['chat'].append(self.data['my_message'])
                    self.reset()
                
        return super().process_event(event)


def main(screen, scene):
    scenes = [
        Scene([BoxPage(screen)], -1, name="BoxPage"),
        Scene([Settings(screen)], -1, name="Settings"),
        Scene([NewBoxPage(screen)], -1, name="NewBoxPage")
    ]
    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)


if __name__ == "__main__":
    last_scene = None
    while True:
        try:
            Screen.wrapper(main, arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError as e:
            last_scene = e.scene
