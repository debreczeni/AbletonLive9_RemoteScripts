# Embedded file name: c:\Jenkins\live\output\win_32_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_Pro\LedLightingComponent.py
from _Framework.Control import ButtonControl
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent

class LedLightingComponent(ControlSurfaceComponent):
    button = ButtonControl(color='Misc.Shift', pressed_color='Misc.ShiftOn')