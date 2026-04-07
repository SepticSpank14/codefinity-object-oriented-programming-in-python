from abc import ABC, abstractmethod

# Define the abstract base class
class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Define the EmailNotifier subclass
class EmailNotifier(Notifier):
    def send(self, message):
        return f"Email sent: {message}"

# Define the SMSNotifier subclass
class SMSNotifier(Notifier):
    def send(self, message):
        return f"SMS sent: {message}"

# Define the notify_user function
def notify_user(notifier, message):
    return notifier.send(message)

# Example usage:
email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()
print(notify_user(email_notifier, "Welcome!"))
print(notify_user(sms_notifier, "Your code is 1234."))