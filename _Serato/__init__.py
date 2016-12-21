# Embedded file name: c:\Jenkins\live\output\win_32_static\Release\python-bundle\MIDI Remote Scripts\_Serato\__init__.py
from Serato import Serato
HIDE_SCRIPT = True

def create_instance(c_instance):
    """ Creates and returns the Serato script """
    return Serato(c_instance)