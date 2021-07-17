# flake8: noqa
from asciimatics.widgets import Widget


class MyWidget(Widget):
    """
    The most basic widget i could do, update func ripped off from horizontaldivider.

    Cant figure out how to make a box
    """

    __slots__ = ["_required_height"]

    def __init__(self, height=Widget.FILL_FRAME, name=None):
        super().__init__(name, tab_stop=False)
        self._required_height = height

    def update(self, frame_no):
        """
        calls whenever the widget needs to redraw itself.
        """
        (color, attr, background) = self._frame.palette["borders"]
        vert = u"│" if self._frame.canvas.unicode_aware else "|"
        hori = u"─" if self._frame.canvas.unicode_aware else "-"
        for i in range(self._h):
            self._frame.canvas.print_at(vert, self._x, self._y + i, color, attr, background)
        for i in range(self._w):
            self._frame.canvas.print_at(hori, self._x + i, self._y, color, attr, background)


    def process_event(self, event):
        return event

    def required_height(self, offset, width):
        return self._required_height

    def reset(self):
        pass

    @property
    def value(self):
        """
        The current value.
        """
        return self._value
