
"""
Principle: Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable
with objects of its subclasses without breaking the application.

Rule: What we want is to have the objects of our subclasses
behaving the same way as the objects of our superclass.

Example: SlackSender send_message method violates this principle by implementing different parameter in compare to
super class method.
"""

from abc import ABC, abstractmethod


class BaseMessageSender(ABC):

    @abstractmethod
    def send_message(self, message_content, recipient):
        raise NotImplementedError("Method is not implemented")


class EmailSender(BaseMessageSender):
    def send_message(self, message_content, recipient):
        print(f"Email: '{message_content}' has been sent to {recipient}.")


class SlackSender(BaseMessageSender):
    def send_message(self, message_content, slack_channel):
        print(f"Slack message: '{message_content}' has been sent to {slack_channel}.")
