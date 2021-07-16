import sys

from asciimatics.exceptions import ResizeScreenError
from asciimatics.scene import Scene
from asciimatics.screen import Screen

from tui.view.box_page import BoxPage
from tui.view.chat import ChatPage
from tui.view.home import HomePage

chat_data = {
    "chat": ["This is the first text", "This is the second text"]
}


def main(screen: Screen, scene: Scene) -> None:
    """The class's docstring"""
    scenes = [
        Scene([HomePage(screen)], -1, name="HomePage"),
        Scene([ChatPage(screen, chat_data=chat_data)], -1, name="ChatPage"),
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
