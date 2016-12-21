# Embedded file name: c:\Jenkins\live\output\win_32_static\Release\python-bundle\MIDI Remote Scripts\VCM600\__init__.py
from VCM600 import VCM600

def create_instance(c_instance):
    """ Creates and returns the ADA1 script """
    return VCM600(c_instance)