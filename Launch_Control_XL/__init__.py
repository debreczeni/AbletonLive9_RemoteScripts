# Embedded file name: c:\Jenkins\live\output\win_32_static\Release\python-bundle\MIDI Remote Scripts\Launch_Control_XL\__init__.py
from LaunchControlXL import LaunchControlXL
from _Framework.Capabilities import controller_id, inport, outport, CONTROLLER_ID_KEY, PORTS_KEY, NOTES_CC, SCRIPT, AUTO_LOAD_KEY

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=4661, product_ids=[97], model_name='Launch Control XL'),
     PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT]), outport(props=[NOTES_CC, SCRIPT])],
     AUTO_LOAD_KEY: True}


def create_instance(c_instance):
    return LaunchControlXL(c_instance)