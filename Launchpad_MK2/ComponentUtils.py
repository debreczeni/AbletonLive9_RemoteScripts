# Embedded file name: c:\Jenkins\live\output\win_32_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_MK2\ComponentUtils.py


def skin_scroll_component(component):
    for button in (component.scroll_up_button, component.scroll_down_button):
        button.color = 'Scrolling.Enabled'
        button.pressed_color = 'Scrolling.Pressed'
        button.disabled_color = 'Scrolling.Disabled'