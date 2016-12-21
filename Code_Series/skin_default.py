# Embedded file name: c:\Jenkins\live\output\win_32_static\Release\python-bundle\MIDI Remote Scripts\Code_Series\skin_default.py
from ableton.v2.control_surface import Skin
from ableton.v2.control_surface.elements import Color

class Colors:

    class DefaultButton:
        On = Color(127)
        Off = Color(0)
        Disabled = Color(0)

    class Transport:
        PlayOn = Color(127)
        PlayOff = Color(0)


def make_default_skin():
    return Skin(Colors)