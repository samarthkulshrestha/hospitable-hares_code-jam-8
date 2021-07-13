from asciimatics.exceptions import NextScene, StopApplication
from asciimatics.screen import Screen
from asciimatics.widgets import Button, Frame, Label, Layout


class LoginPage(Frame):
    """The class def for login page"""

    def __init__(self, screen: Screen):
        #
        super().__init__(screen, screen.height * 2 // 3, screen.width * 2 // 3)

        # Frame can contain multiple layouts, add display-widgets to layout to display the data you want
        # first parameter explained: no of items on list = no of columns. value of list item = column width
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        self._page_title = Label("Login Page")
        layout.add_widget(self._page_title)
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

    def _onclick_previous(self) -> None:
        raise NextScene("HomePage")

    def _onclick_quit(self) -> None:
        raise StopApplication("User pressed quit")
