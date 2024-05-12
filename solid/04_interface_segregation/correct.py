
"""
Principle: Interface segregation

Rule: Prevent classes or modules from depending on methods they don't need, which can lead to unnecessary coupling,
increased complexity, and potential issues during maintenance or extension of the codebase.

Example: Now we segregated interfaces by splitting them into BaseMessageSender and BaseAuthorizeSender. Now
EmailSender and SlackSender can be treated as BaseMessageSender.
"""
from typing import Protocol


class BaseMessageSender(Protocol):
    """
    Basic protocol class which includes send message functionality.
    """
    def send_message(self, message_content):
        ...


class BaseAuthorizeSender(Protocol):
    """
    Basic protocol class which includes user authorization method
    """
    def authorize_user(self):
        ...


class EmailSender:
    """
    Simplified email sender class
    """
    def __init__(self, recipient):
        self.recipient = recipient

    def send_message(self, message_content):
        print(f"Email: '{message_content}' has been sent to {self.recipient}.")


class SlackSender:
    """
    Simplified slack notification sender class
    """
    def __init__(self, slack_channel):
        self.slack_channel = slack_channel

    def send_message(self, message_content):
        print(f"Slack message: '{message_content}' has been sent to slack channel {self.slack_channel}.")

    def authorize_user(self, username):
        print(f"User {username} authorized.")


# Now EmailSender is treated as a child of BaseMessageSender and can be passed into the list without errors.
def send_message_multichannel(message_sender_list: list[BaseMessageSender], message_content):
    for message_sender in message_sender_list:
        message_sender.send_message(message_content)


email = EmailSender(recipient="example@example.com")
slack = SlackSender(slack_channel="SOLID tips & tricks")
content = "Correct interface segregation"
send_message_multichannel(message_sender_list=[email, slack], message_content=content)
