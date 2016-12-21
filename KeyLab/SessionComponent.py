# Embedded file name: c:\Jenkins\live\output\win_32_static\Release\python-bundle\MIDI Remote Scripts\KeyLab\SessionComponent.py
from _Arturia.SessionComponent import SessionComponent as SessionComponentBase

class SessionComponent(SessionComponentBase):

    def set_selected_scene_launch_button(self, button):
        self.selected_scene().set_launch_button(button)