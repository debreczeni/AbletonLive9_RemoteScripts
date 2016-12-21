# Embedded file name: c:\Jenkins\live\output\win_32_static\Release\python-bundle\MIDI Remote Scripts\VCM600\TransportComponent.py
from _Framework.TransportComponent import TransportComponent as TransportComponentBase

class TransportComponent(TransportComponentBase):

    def __init__(self, *a, **k):
        super(TransportComponent, self).__init__(*a, **k)
        self._punch_in_toggle.is_momentary = False
        self._punch_out_toggle.is_momentary = False