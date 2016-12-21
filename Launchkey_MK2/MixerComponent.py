# Embedded file name: c:\Jenkins\live\output\win_32_static\Release\python-bundle\MIDI Remote Scripts\Launchkey_MK2\MixerComponent.py
from _Framework.MixerComponent import MixerComponent as MixerComponentBase

class MixerComponent(MixerComponentBase):

    def set_volume_control(self, control):
        self._selected_strip.set_volume_control(control)