# Embedded file name: c:\Jenkins\live\output\win_32_static\Release\python-bundle\MIDI Remote Scripts\pushbase\transport_component.py
from __future__ import absolute_import, print_function
from ableton.v2.control_surface import components

class TransportComponent(components.TransportComponent):

    def __init__(self, *a, **k):
        super(TransportComponent, self).__init__(*a, **k)
        self._metronome_toggle.view_transform = lambda v: ('Metronome.On' if v else 'Metronome.Off')