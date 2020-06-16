"""
processmixer.py
This script processes events when the browser window is active

"""

import mixer

import eventconsts
import internal
import config



def process(command):

    command.actions.addProcessor("Browser Processor")

    

    # Add did not handle flag if not handled
    if command.handled is False: 
        command.actions.appendAction("[Did not handle]")
