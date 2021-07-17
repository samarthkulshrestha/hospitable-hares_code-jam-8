import sys
from tui.view.settings import Settings

from asciimatics.exceptions import ResizeScreenError
from asciimatics.scene import Scene
from asciimatics.screen import Screen

from tui.view.box_page import BoxPage, NewBoxPage
from tui.view.chat import ChatPage
from tui.view.home import HomePage


class BoxSelection(object):
    def __init__(self):
        # Current contact when editing.
        self.current_box_id = None

        # List of dicts, where each dict contains a single contact, containing
        # name, address, phone, email and notes fields.
        self.boxes = dict()
    
    def refresh():
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
