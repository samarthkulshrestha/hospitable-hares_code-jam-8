import sys

from asciimatics.exceptions import ResizeScreenError
from asciimatics.scene import Scene
from asciimatics.screen import Screen

from tui.view.home import HomePage
from tui.view.login import LoginPage


def main(screen: Screen, scene: Scene) -> None:
    """The class's docstring"""
    scenes = [
        Scene([HomePage(screen)], -1, name="HomePage"),
        Scene([LoginPage(screen)], -1, name="LoginPage"),
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
