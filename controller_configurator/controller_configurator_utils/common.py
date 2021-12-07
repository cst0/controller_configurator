#!/usr/bin/env python3

from enum import Enum
import pygame
from typing import List

# using these wrapper classes because that'll allow for using something other
# than pygame later if I need to go that route

class ResponseType(Enum):
    ALWAYS=0,
    ONCE=1,
    ON_CHANGE=2

class ControlType(object):
    def __init__(self):
        self.type = None

class ButtonStates(ControlType):
    def __init__(self, buttons:List[bool]):
        self.type = 'button'
        self.buttons = buttons

class JoystickStates(ControlType):
    def __init__(self, joysticks:List[float]):
        self.type = 'joystick'
        self.joysticks = joysticks

class HatStates(ControlType):
    def __init__(self, hats:List[tuple]):
        self.type = 'hat'
        self.hats = hats

class ControllerState:
    def __init__(self, buttons:ButtonStates, joysticks:JoystickStates, hats:HatStates, _id=0):
        self.buttons = buttons
        self.joysticks = joysticks
        self.hats = hats
        self.id = _id

def get_controller_state(_id=0) -> ControllerState:
    return ControllerState(ButtonStates([True, True, False, False]), JoystickStates([1.0, 0.95, 0, -0.875]), HatStates([]))

def get_controller_ids() -> List[int]:
    return [0]

def init_controllers():
    pass

class TopicMetaData:
    def __init__(self, topic:str):
        pass

def get_topic_metadata(topic:str) -> TopicMetaData:
    return TopicMetaData(topic)
