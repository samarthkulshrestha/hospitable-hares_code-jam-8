# flake8: noqa

import sys, os

from asciimatics.exceptions import ResizeScreenError
from asciimatics.scene import Scene
from asciimatics.screen import Screen

from tui.view.box_page import BoxPage, NewBoxPage
from tui.view.chat import ChatPage
from tui.view.home import HomePage
from tui.view.settings import Settings
from tui import api_wrapper
from tui import crypt


class BoxSelection(object):
    """State controller object"""

    def __init__(self):
        # Current contact when editing.
        self.current_box_id = None

        # List of dicts, where each dict contains a single contact, containing
        # name, address, phone, email and notes fields.
        z = os.path.isfile("key.key")
        if not z:
            crypt.write_key()
        x = os.path.isfile("token")
        if not x:
            api_wrapper.join()
        self.boxes = dict()
        self.refresh()
        '''
        get_posts() -> box_id, page_no, load_more
        post() -> box_id, message_body
        '''

    def refresh(self):
        
        self.boxes = 
        pass
    def new_box(self, data):

        pass


chat_data = {
    "chat": ["This is the first text", "This is the second text"],
    "my_message": '',
}


def main(screen: Screen, scene: Scene) -> None:
    """The class's docstring"""
    boxselection = BoxSelection()
    #boxselection.refresh()

    scenes = [
        Scene([HomePage(screen)], -1, name="HomePage"),
        Scene([BoxPage(screen, box_selection=boxselection)], -1, name="BoxPage"),
        Scene([ChatPage(screen, chat_data=chat_data)], -1, name="ChatPage"),
        Scene([NewBoxPage(screen, boxselection)], -1, name="NewBoxPage"),
        Scene([Settings(screen)], -1, name="Settings"),
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
