from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys

class BoxSelection(object):
    def __init__(self):
        # Current contact when editing.
        self.current_box_id = None

        # List of dicts, where each dict contains a single contact, containing
        # name, address, phone, email and notes fields.
        self.boxes = []