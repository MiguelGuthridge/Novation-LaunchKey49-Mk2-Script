"""
processfirst.py
This file processes events before anything else.

"""

import transport
import ui

import config
import eventprocessor
import eventconsts
import internal
import lighting

def redraw(lights):

    # In Popup Menu
    if ui.isInPopupMenu():
        lights.setPadColour(1, 0, lighting.UI_NAV_VERTICAL)         # Up
        lights.setPadColour(1, 1, lighting.UI_NAV_VERTICAL)         # Down
        lights.setPadColour(0, 1, lighting.UI_NAV_HORIZONTAL)       # Left
        lights.setPadColour(2, 1, lighting.UI_NAV_HORIZONTAL)       # Right
        lights.setPadColour(3, 1, lighting.UI_REJECT)               # No
        lights.setPadColour(4, 1, lighting.UI_ACCEPT)               # Yes
        lights.solidifyAll()

    # Shift key triggers window switcher
    if internal.shift.getDown():
        
        lights.setPadColour(0, 1, lighting.WINDOW_PLAYLIST)         # Playlist
        lights.setPadColour(1, 1, lighting.WINDOW_CHANNEL_RACK)     # Channel rack
        lights.setPadColour(2, 1, lighting.WINDOW_PIANO_ROLL)       # Piano roll
        lights.setPadColour(3, 1, lighting.WINDOW_MIXER)            # Mixer
        lights.setPadColour(4, 1, lighting.WINDOW_BROWSER)          # Browser

        lights.setPadColour(6, 0, lighting.UI_NAV_HORIZONTAL)       # Prev plugin
        lights.setPadColour(7, 0, lighting.UI_NAV_HORIZONTAL)       # Prev plugin

        lights.solidifyAll()


    return

def process(command):

    command.actions.addProcessor("Primary Processor")

    # If in extended mode
    if internal.PORT == config.DEVICE_PORT_EXTENDED:

        # Pads down (white light)
        if command.type == eventconsts.TYPE_BASIC_PAD or command.type == eventconsts.TYPE_PAD:
            if command.value: # Press down
                internal.pads.press(command.padX, command.padY)
            else:
                internal.pads.lift(command.padX, command.padY)

        # Shift button (in control for pads (window switcher))
        if command.id == config.SHIFT_BUTTON:
            if command.is_lift:
                internal.extendedMode.revert(eventconsts.INCONTROL_PADS)
            else:
                internal.extendedMode.setVal(True, eventconsts.INCONTROL_PADS)

        # Shift down - Window switcher
        if internal.shift.getDown() and command.type == eventconsts.TYPE_PAD and command.is_lift:
            
            if command.note == eventconsts.Pads[0][1]: 
                ui.showWindow(config.WINDOW_PLAYLIST)
                command.actions.appendAction("Switched window to Playlist")
                command.handled = True

            if command.note == eventconsts.Pads[1][1]: 
                ui.showWindow(config.WINDOW_CHANNEL_RACK)
                command.actions.appendAction("Switched window to Channel rack")
                command.handled = True

            if command.note == eventconsts.Pads[2][1]: 
                ui.showWindow(config.WINDOW_PIANO_ROLL)
                command.actions.appendAction("Switched window to Piano roll")
                command.handled = True
            
            if command.note == eventconsts.Pads[3][1]: 
                ui.showWindow(config.WINDOW_MIXER)
                command.actions.appendAction("Switched window to Mixer")
                command.handled = True
            
            if command.note == eventconsts.Pads[4][1]: 
                ui.showWindow(config.WINDOW_BROWSER)
                command.actions.appendAction("Switched window to Browser")
                command.handled = True
            
            if command.note == eventconsts.Pads[6][0]: 
                ui.selectWindow(True)
                command.actions.appendAction("Previous window")
                command.handled = True
            
            if command.note == eventconsts.Pads[7][0]: 
                ui.selectWindow(False)
                command.actions.appendAction("Next window")
                command.handled = True

            

        # Right click menu
        if ui.isInPopupMenu() and command.type == eventconsts.TYPE_PAD and command.is_lift:
            
            # Always handle all presses
            command.handled = True

            if command.note == eventconsts.Pads[1][0]:
                ui.up()
                command.actions.appendAction("UI Up")

            if command.note == eventconsts.Pads[1][1]:
                ui.down()
                command.actions.appendAction("UI Down")

            if command.note == eventconsts.Pads[0][1]:
                ui.left()
                command.actions.appendAction("UI Left")
            
            if command.note == eventconsts.Pads[2][1]:
                ui.right()
                command.actions.appendAction("UI Right")

            if command.note == eventconsts.Pads[3][1]:
                ui.escape()
                command.actions.appendAction("UI Escape")

            if command.note == eventconsts.Pads[4][1]:
                ui.enter()
                command.actions.appendAction("UI Enter")

        #
        # Extended Mode signals
        #

        # All
        if command.id == eventconsts.SYSTEM_EXTENDED:
            internal.extendedMode.recieve(not command.is_lift)
            command.actions.appendAction("Set Extended Mode to " + str(not command.is_lift))
            command.handled = True

        # Knobs
        if command.id == eventconsts.INCONTROL_KNOBS:
            internal.extendedMode.recieve(not command.is_lift, eventconsts.INCONTROL_KNOBS)
            command.actions.appendAction("Set Extended Mode (Knobs) to " + str(not command.is_lift))
            command.handled = True
        
        # Faders
        if command.id == eventconsts.INCONTROL_FADERS:
            internal.extendedMode.recieve(not command.is_lift, eventconsts.INCONTROL_FADERS)
            command.actions.appendAction("Set Extended Mode (Faders) to " + str(not command.is_lift))
            command.handled = True
        
        # Pads
        if command.id == eventconsts.INCONTROL_PADS:
            internal.extendedMode.recieve(not command.is_lift, eventconsts.INCONTROL_PADS)
            command.actions.appendAction("Set Extended Mode (Pads) to " + str(not command.is_lift))
            command.handled = True
        
        # That random event on the knobs button
        if command.id == eventconsts.SYSTEM_MISC:
            command.handled = True
    
    # Add did not handle flag if not handled
    if command.handled is False: 
        command.actions.appendAction("[Did not handle]")
