from asciimatics.exceptions import NextScene, StopApplication
from asciimatics.screen import Screen
from asciimatics.widgets import Button, Frame, Layout, TextBox
from asciimatics.widgets.widget import Widget


class ChatPage(Frame):
    """The class def for login page"""

    def __init__(self, screen: Screen, chat_data: dict):
        #
        super().__init__(screen, screen.height * 2 // 3, screen.width * 2 // 3)
        self._chat_data = chat_data
        # Frame can contain multiple layouts, add display-widgets to layout to display the data you want
        # first parameter explained: no of items on list = no of columns. value of list item = column width
        layout = Layout([500], fill_frame=True)
        self.add_layout(layout)
        self._chat_box = TextBox(Widget.FILL_FRAME, None, "chat", as_string=False, line_wrap=True, readonly=True)
        layout.add_widget(self._chat_box)
        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)
        # Read the widget part on the docuemtation for info about the parameters
        layout2.add_widget(Button("Previous Page", self._onclick_previous), 0)
        layout2.add_widget(Button("Quit", self._onclick_quit), 3)
        # Fix the layouts and calculate the locations of all the widgets.
        # This function should be called once all Layouts have been added
        # to the Frame and all widgets added to the Layouts.
        # Method Belongs to parent class (FRAME)
        self.fix()

    def reset(self) -> None:
        """Check docs"""
        super().reset()
        self.data = self._chat_data

    def _onclick_previous(self) -> None:
        raise NextScene("HomePage")

    def _onclick_quit(self) -> None:
        raise StopApplication("User pressed quit")
