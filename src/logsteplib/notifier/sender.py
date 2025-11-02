"""
Send email notifications using SMTP.

This module provides the EmailNotifier class for sending plain text email messages
via an SMTP server. Use this class to automate email alerts or notifications
from Python code.

Classes
-------
EmailNotifier
    Send plain text emails using SMTP authentication.

Examples
--------
>>> notifier = EmailNotifier(
...     smtp_server="smtp.example.com",
...     smtp_port=587,
...     username="user",
...     password="pass",
...     sender_email="sender@example.com"
... )
>>> notifier.send_email(
...     recipient_email="recipient@example.com",
...     subject="Test Email",
...     message_body="This is a test."
... )
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailNotifier:
    """
    Send plain text email notifications via SMTP.

    Establish a connection to an SMTP server and send email messages with authentication.
    Use this class to automate email alerts or notifications from Python code.

    Parameters
    ----------
    smtp_server : str
        Address of the SMTP server.
    smtp_port : int
        Port number for the SMTP server.
    username : str
        Username for SMTP authentication.
    password : str
        Password for SMTP authentication.
    sender_email : str
        Email address of the sender.

    Methods
    -------
    send_email(recipient_email, subject, message_body)
        Send a plain text email to the specified recipient.
    """
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str, sender_email: str) -> None:
        """
        Initialize the EmailNotifier with SMTP server details and credentials.

        Set up the SMTP server address, port, authentication credentials, and sender email
        for sending notifications.

        Parameters
        ----------
        smtp_server : str
            Specify the address of the SMTP server.
        smtp_port : int
            Specify the port number for the SMTP server.
        username : str
            Provide the username for SMTP authentication.
        password : str
            Provide the password for SMTP authentication.
        sender_email : str
            Specify the email address of the sender.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        self.sender_email = sender_email

    def send_email(self, recipient_email: str, subject: str, message_body: str) -> None:
        """
        Send a plain text email to a recipient.

        Compose and transmit an email message using SMTP authentication.
        Attach the message body as plain text and set the subject and recipient fields.

        Parameters
        ----------
        recipient_email : str
            Specify the email address of the recipient.
        subject : str
            Specify the subject line of the email.
        message_body : str
            Provide the plain text content of the email message.

        Raises
        ------
        Exception
            Raise an exception if the email fails to send due to SMTP errors or connection issues.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg["From"] = self.sender_email
            msg["To"] = recipient_email
            msg["Subject"] = subject

            msg.attach(MIMEText(message_body, "plain"))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(host=self.smtp_server, port=self.smtp_port) as server:
                server.starttls()
                server.login(user=self.username, password=self.password)
                server.send_message(msg=msg)

            print(f"Email sent to {recipient_email}")
        except Exception as e:
            print(f"Failed to send email: {e}")

# eof
