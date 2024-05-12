"""
Principle: Dependency Inversion

Rule: High-level modules should depend on abstractions rather than concrete implementations.

Example: PowerController class rely on stable abstraction - Switchable abstract class

In other words:
- avoid multiple inheritance
- rely on stable abstractions
- don't refer to volatile concrete classes - refer to abstract interfaces instead
"""
from abc import ABC, abstractmethod


class Switchable(ABC):
    """
    This class is inherited by any device that can be switched on and off.
    """
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    """
    Light bulb that can be turned on and off
    """
    def turn_on(self):
        print("Lightbulb: turned on")

    def turn_off(self):
        print("Lightbulb: turned off")


class Vacuum(Switchable):
    """
    Simplified implementation of vacuum which turns on and off.
    """
    def turn_on(self):
        print("Vacuum: turned on")

    def turn_off(self):
        print("Vacuum: turned off")


class PowerController:
    """
    This class controls device power management. Turning power on and off with press of a button.
    """
    # Now we are passing ANY switchable device that can be switched on and off.
    def __init__(self, device: Switchable):
        self.device = device
        self.on = False

    def press(self):
        if self.on:
            self.device.turn_off()
        else:
            self.device.turn_on()
            self.on = True