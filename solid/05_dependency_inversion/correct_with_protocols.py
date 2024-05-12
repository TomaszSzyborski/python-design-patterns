"""
Principle: Dependency Inversion

Rule: High-level modules should depend on abstractions rather than concrete implementations.

Example: PowerController class rely on stable abstraction - Switchable abstract class

In other words:
- avoid multiple inheritance
- rely on stable abstractions
- don't refer to volatile concrete classes - refer to abstract interfaces instead
"""
from enum import auto, StrEnum
from typing import Protocol


class State(StrEnum):
    ON = auto()
    OFF = auto()


class Switchable(Protocol):
    """
    Protocol for switchable items
    """
    state: State

    def turn_on(self) -> None:
        ...

    def turn_off(self) -> None:
        ...


class LightBulb:
    """
    Light bulb that can be turned on and off
    """

    def __init__(self, state: State = State.OFF):
        self.state = state

    def turn_on(self):
        self.state = State.ON
        print("Lightbulb: turned on")

    def turn_off(self):
        self.state = State.OFF
        print("Lightbulb: turned off")


class Vacuum:
    """
    Simplified implementation of vacuum which turns on and off.
    """

    def __init__(self, state: State = State.OFF):
        self.state = state

    def turn_on(self):
        self.state = State.ON
        print("Vacuum: turned on")

    def turn_off(self):
        self.state = State.OFF
        print("Vacuum: turned off")


class PowerController:
    """
    This class controls device power management. Turning power on and off with press of a button.
    """

    # Now we are passing ANY switchable device that can be switched on and off.
    def __init__(self, device: Switchable):
        self.device = device

    def press(self):
        if self.device.state == State.ON:
            self.device.turn_off()
        else:
            self.device.turn_on()



if __name__ == '__main__':
    lightbulb = LightBulb()
    lightbulb1 = LightBulb()
    pc = PowerController(lightbulb)
    pc1 = PowerController(lightbulb1)
    print(pc.device.state)
    print(pc1.device.state)
    pc.press()
    print(pc.device.state)
    print(pc1.device.state)
    pc.press()
    print(pc.device.state)
    print(pc1.device.state)
    pc.press()
    pc.press()
    pc1.press()
    pc1.press()
    pc1.press()
    pc1.press()
