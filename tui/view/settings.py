
from logging import disable
from asciimatics.exceptions import NextScene
from asciimatics.screen import Screen
# from asciimatics.scene import Scene
# from time import sleep
from asciimatics.widgets import Button, Divider, DropdownList, Frame, Layout, Text

settings_data = {
    "fg": 0,
    "bg": 0,
    "txt": 0
}

options_ddl1 = ["COLOUR_BLACK = 0",
                "COLOUR_RED = 1",
                "COLOUR_GREEN = 2",
                "COLOUR_YELLOW = 3",
                "COLOUR_BLUE = 4",
                "COLOUR_MAGENTA = 5",
                "COLOUR_CYAN = 6",
                "COLOUR_WHITE = 7"
                ]
options_ddl2 = options_ddl1
options_ddl3 = [
    "A_BOLD = 1",
    "A_NORMAL = 2",
    "A_REVERSE = 3",
    "A_UNDERLINE = 4"
]


class Settings(Frame):
    """
    This class will display the setting pane.

    If you want to get access to data you can use the `get_settings` function or access `settings_data` dictionary.
    """

    def __init__(self, screen: Screen) -> None:
        global settings_data
        super().__init__(screen, screen.height*2//3, screen.width*2//3,
                         has_border=False, title="Setting", data=settings_data, name="settings_form")
        layout = Layout([1, 18, 1])
        # self.screen = screen
        self.add_layout(layout)

        layout.add_widget(Divider(draw_line=False, height=screen.height // 3), 1)
        layout.add_widget(Text(name="widget_name", label="name of widget:", on_change=self._shift_widget_focus), 1)

        self._fg_list = DropdownList([(x, i) for i, x in enumerate(options_ddl1)],
                                       label="foreground",
                                       name="fg",
                                       on_change=self._on_change,
                                       )
        self._bg_list = DropdownList([(x, i) for i, x in enumerate(options_ddl2)],
                                       label="background",
                                       name="bg",
                                       on_change=self._on_change,
                                       )
        self._txt_list = DropdownList([(x, i) for i, x in enumerate(options_ddl3)],
                                       label="text",
                                       name="txt",
                                       on_change=self._on_change,
                                       )
        layout.add_widget(self._fg_list, 1)
        layout.add_widget(self._bg_list, 1)
        layout.add_widget(self._txt_list, 1)

        # adding divider
        layout2 = Layout([10])
        self.add_layout(layout2)

        layout2.add_widget(Divider(draw_line=False, height=5))

        # adding the button
        layout3 = Layout([1, 1, 3])
        self.add_layout(layout3)

        layout3.add_widget(Button('back', on_click=self._on_back, name='test_button'), 2)

        self.fix()

    def _on_change(self) -> None:
        self.save()
        global settings_data
        if "widget_name" in self.data and self.data["widget_name"] != "":
            all_data_list = dict()
            all_true = True
            for i in ['fg', 'bg', 'txt']:
                if i in self.data:
                    all_data_list[i] = self.data[i]
                else:
                    all_true = False
            if all_true:
                settings_data[self.data["widget_name"]] = all_data_list
                self.palette[self.data["widget_name"]] = (int(settings_data['fg']), int(settings_data['txt'])+1,
                                                          int(settings_data['bg']))
                self.screen.refresh()
        

    def _on_back(self) -> None:
        self.save()
        raise NextScene("HomePage")
    
    def _shift_widget_focus(self) -> None:
        self.save()



def get_settings() -> dict:
    """This will return the settings data collected"""
    return settings_data

# while True:
#     def demo(screen):
#         x = Scene([Settings(screen)], 150, name="Settings")
#         screen.play([x], repeat=False)
#         # st = settings_data["ddl1"]+', '+settings_data["ddl2"]+', '+settings_data["ddl3"]
#         screen.clear()
#         screen.refresh()
#         screen.print_at(settings_data,0,0)
#         screen.refresh()
#         sleep(10)
#     Screen.wrapper(demo)
