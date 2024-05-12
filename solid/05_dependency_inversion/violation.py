"""
Principle: Dependency Inversion

Rule: High-level modules should depend on abstractions rather than concrete implementations.

Example: PowerController class should not rely on concrete class, because in case of extending usage
to other switchable devices we would need to modify PowerController for each new device.

In other words:
- avoid multiple inheritance
- rely on stable abstractions
- don't refer to volatile concrete classes - refer to abstract interfaces instead
"""


class LightBulb:
    """
    Light bulb that can be turned on and off
    """
    def turn_on(self):
        print("Lightbulb: turned on")

    def turn_off(self):
        print("Lightbulb: turned off")


class PowerController:
    """
    This class controls device power management. Turning power on and off with press of a button.
    """
    # Here we are passing concrete class instead of abstraction.
    # In case you want to use other device there will be issues.
    def __init__(self, lightbulb: LightBulb):
        self.lightbulb = lightbulb
        self.on = False

    def press(self):
        if self.on:
            self.lightbulb.turn_off()
        else:
            self.lightbulb.turn_on()
            self.on = True