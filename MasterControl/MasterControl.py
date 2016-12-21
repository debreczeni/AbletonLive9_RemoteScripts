# Embedded file name: c:\Jenkins\live\output\win_32_static\Release\python-bundle\MIDI Remote Scripts\MasterControl\MasterControl.py
from MackieControl.MackieControl import MackieControl

class MasterControl(MackieControl):
    """ Main class derived from MackieControl """

    def __init__(self, c_instance):
        MackieControl.__init__(self, c_instance)