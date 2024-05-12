"""
Principle: Open-Closed Principle

Rule: Objects or entities should be open for extension but closed for modification

Example: In this example we have two methods with similar context but different behaviour.
In more complicated implementations it would introduce additional conditions and make code hard to read.
"""


class MessageSender:

    def send_email(self, message_content, recipient):
        print(f"Email: '{message_content}' has been sent to {recipient}.")

    def send_slack_notification(self, message_content, recipient):
        print(f"Slack message: '{message_content}' has been sent to {recipient}.")