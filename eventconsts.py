"""
eventconsts.py
This file contains constants for buttons/faders/knobs sent from the controller.

You shouldn't need to adjust these values, 
but if you are modifying the script for use with a different controller with the same features,
this is the place to start.
"""
# Define contant for determining event type
TYPE_UNRECOGNISED = -1
TYPE_SYSTEM_MSG = 0
TYPE_INCONTROL = 1
TYPE_TRANSPORT = 2
TYPE_KNOB = 3
TYPE_FADER = 4
TYPE_MIXER_BUTTON = 5
TYPE_PAD = 6

# Define System Message
SYSTEM_IN_CONTROL = 0x0C9F

SystemMessages = [SYSTEM_IN_CONTROL]

# Define InControl Buttons

INCONTROL_KNOBS = 0x0D9F
INCONTROL_FADERS = 0x0E9F
INCONTROL_PADS = 0x0F9F

InControlButtons = [INCONTROL_KNOBS, INCONTROL_FADERS, INCONTROL_PADS]

# Define transport controls

TRANSPORT_BACK = 0x70BF
TRANSPORT_FORWARD = 0x71BF
TRANSPORT_STOP = 0x72BF
TRANSPORT_PLAY = 0x73BF
TRANSPORT_LOOP = 0x74BF
TRANSPORT_RECORD = 0x75BF

TransportControls = [TRANSPORT_BACK, TRANSPORT_FORWARD, TRANSPORT_STOP, TRANSPORT_PLAY, TRANSPORT_LOOP, TRANSPORT_RECORD]


# Define faders

FADER_1 = 0x29BF
FADER_2 = 0x2ABF
FADER_3 = 0x2BBF
FADER_4 = 0x2CBF
FADER_5 = 0x2DBF
FADER_6 = 0x2EBF
FADER_7 = 0x2FBF
FADER_8 = 0x30BF
FADER_9 = 0x07BF

Faders = [FADER_1, FADER_2, FADER_3, FADER_4, FADER_5, FADER_6, FADER_7, FADER_8, FADER_9]


# Define faders

BASIC_FADER_1 = 0x29B0
BASIC_FADER_2 = 0x2AB0
BASIC_FADER_3 = 0x2BB0
BASIC_FADER_4 = 0x2CB0
BASIC_FADER_5 = 0x2DB0
BASIC_FADER_6 = 0x2EB0
BASIC_FADER_7 = 0x2FB0
BASIC_FADER_8 = 0x30B0
BASIC_FADER_9 = 0x07B0

BasicFaders = [BASIC_FADER_1, BASIC_FADER_2, BASIC_FADER_3, BASIC_FADER_4, BASIC_FADER_5, BASIC_FADER_6, BASIC_FADER_7, BASIC_FADER_8, BASIC_FADER_9]


# Define pad references

PAD_TOP_1 = 0x60
PAD_TOP_2 = 0x61
PAD_TOP_3 = 0x62
PAD_TOP_4 = 0x63
PAD_TOP_5 = 0x64
PAD_TOP_6 = 0x65
PAD_TOP_7 = 0x66
PAD_TOP_8 = 0x67

PAD_BOTTOM_1 = 0x70
PAD_BOTTOM_2 = 0x71
PAD_BOTTOM_3 = 0x72
PAD_BOTTOM_4 = 0x73
PAD_BOTTOM_5 = 0x74
PAD_BOTTOM_6 = 0x75
PAD_BOTTOM_7 = 0x76
PAD_BOTTOM_8 = 0x77

PAD_TOP_BUTTON = 0x68
PAD_BOTTOM_BUTTON = 0x78

Pads = [PAD_TOP_1, PAD_TOP_2, PAD_TOP_3, PAD_TOP_4, PAD_TOP_5, PAD_TOP_6, PAD_TOP_7, PAD_TOP_8, PAD_BOTTOM_1, PAD_BOTTOM_2, PAD_BOTTOM_3, PAD_BOTTOM_4, PAD_BOTTOM_5, PAD_BOTTOM_6, PAD_BOTTOM_7, PAD_BOTTOM_8, PAD_TOP_BUTTON, PAD_BOTTOM_BUTTON]

# Define Basic Mode pad references

BASIC_PAD_TOP_1 = 0x28
BASIC_PAD_TOP_2 = 0x29
BASIC_PAD_TOP_3 = 0x2A
BASIC_PAD_TOP_4 = 0x2B
BASIC_PAD_TOP_5 = 0x30
BASIC_PAD_TOP_6 = 0x31
BASIC_PAD_TOP_7 = 0x32
BASIC_PAD_TOP_8 = 0x33

BASIC_PAD_BOTTOM_1 = 0x24
BASIC_PAD_BOTTOM_2 = 0x25
BASIC_PAD_BOTTOM_3 = 0x26
BASIC_PAD_BOTTOM_4 = 0x27
BASIC_PAD_BOTTOM_5 = 0x2C
BASIC_PAD_BOTTOM_6 = 0x2D
BASIC_PAD_BOTTOM_7 = 0x2E
BASIC_PAD_BOTTOM_8 = 0x2F

BASIC_PAD_TOP_BUTTON = 0x68
BASIC_PAD_BOTTOM_BUTTON = 0x69

