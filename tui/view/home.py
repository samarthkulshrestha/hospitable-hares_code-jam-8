import random
import string

from asciimatics.exceptions import NextScene
from asciimatics.screen import Screen
from asciimatics.widgets import Button, Frame, Label, Layout


class HomePage(Frame):
    """A HomePage widget"""

    def __init__(self, screen: Screen) -> None:
        #
        super().__init__(screen, screen.height * 2 // 3, screen.width * 2 // 3)

        # Frame can contain multiple layouts, add display-widgets to layout to display the data you want
        # first parameter explained: no of items on list = no of columns. value of list item = column width
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        self._page_title = Label("HOMEPAGE")
        layout.add_widget(self._page_title)
        layout2 = Layout([1, 2])
        self.add_layout(layout2)
        # Read the widget part on the docuemtation for info about the parameters
        layout2.add_widget(Button("Chat Page", self._onclick_next), 0)
        layout2.add_widget(Button("Change Title", self._onclick_change_title), 1)
        # Fix the layouts and calculate the locations of all the widgets.
        # This function should be called once all Layouts have been added to the
        # frame and all widgets added to the Layouts.
        # Method Belongs to parent class (FRAME)
        self.fix()

    def _onclick_next(self) -> None:
        raise NextScene("ChatPage")

    def _onclick_change_title(self) -> None:
        self._page_title.text = self._get_random_string()

    def _get_random_string(self) -> str:
        letters = string.ascii_uppercase
        result_str = "".join(random.choice(letters) for i in range(7))
        return result_str

        # sads
