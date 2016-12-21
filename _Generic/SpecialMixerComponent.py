# Embedded file name: c:\Jenkins\live\output\win_32_static\Release\python-bundle\MIDI Remote Scripts\_Generic\SpecialMixerComponent.py
import Live
from _Framework.MixerComponent import MixerComponent
from SelectChanStripComponent import SelectChanStripComponent

class SpecialMixerComponent(MixerComponent):
    """ Class encompassing several selecting channel strips to form a mixer """

    def _create_strip(self):
        return SelectChanStripComponent()