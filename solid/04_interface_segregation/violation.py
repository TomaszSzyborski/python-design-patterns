"""
Principle: Interface segregation

Rule: Prevent classes or modules from depending on methods they don't need, which can lead to unnecessary coupling,
increased complexity, and potential issues during maintenance or extension of the codebase.

Example: BaseMessageSender implements 'authorize_user' method which is not implemented by EmailSender, thus it is not
considered as BaseMessageSender.
"""
from typing import Protocol


class BaseMessageSender(Protocol):
    """
    Basic protocol class which includes send message functionality.
    """
    def send_message(self, message_content):
        ...

    def authorize_user(self, username):
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


# When we pass EmailSender into 'message_sender_list' parameter we get an error because it doesn't have 'authorize_user'
# method implemented
def send_message_multichannel(message_sender_list: list[BaseMessageSender], message_content):
    for message_sender in message_sender_list:
        message_sender.send_message(message_content)


email = EmailSender(recipient="example@example.com")
slack = SlackSender(slack_channel="SOLID tips & tricks")
content = "Violating interface segregation"
send_message_multichannel(message_sender_list=[slack, email], message_content=content)