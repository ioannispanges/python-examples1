class Email:
    def __init__(self, sender, recipient, subject, message):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.message = message
        self.is_send = False

    def send(self):
        if not self.is_send:
            self.is_send = True
            return f"Email send from {self.sender} to {self.recipient}. Subject: {self.subject}. Body {self.message}"
        else:
            return "This email has already been sent"


my_email = Email("doe@example.com", "john@example.com", "Hello", "Just saying hi")

print(my_email.send())
print(my_email.send())
