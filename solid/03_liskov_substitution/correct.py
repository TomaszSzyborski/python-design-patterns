"""
Principle: Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable
with objects of its subclasses without breaking the application.

Rule: What we want is to have the objects of our subclasses
behaving the same way as the objects of our superclass.

Example: Now the parameter which differs across subclasses is passed in constructor to keep the same parameters
of send_message method as in superclass.
"""
from abc import ABC, abstractmethod


class BaseMessageSender(ABC):

    @abstractmethod
    def send_message(self, message_content):
        raise NotImplementedError("Method is not implemented")


class EmailSender(BaseMessageSender):
    def __init__(self, recipient):
        self.recipient = recipient

    def send_message(self, message_content):
        print(f"Email: '{message_content}' has been sent to {self.recipient}.")


class SlackSender(BaseMessageSender):

    def __init__(self, slack_channel):
        self.slack_channel = slack_channel

    def send_message(self, message_content):
        print(f"Slack message: '{message_content}' has been sent to slack channel {self.slack_channel}.")