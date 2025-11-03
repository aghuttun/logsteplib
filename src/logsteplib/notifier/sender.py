"""
Send email.
"""

import base64
import os
import requests


class EmailSender:
    def __init__(self, client_id: str, client_secret: str, tenant_id: str, sender_email: str) -> None:
        self._client_id = client_id
        self._client_secret = client_secret
        self._tenant_id = tenant_id
        self._sender_email = sender_email
        self._token = self._authenticate()

    def _authenticate(self) -> str:

        # Authenticate and get access token
        url = f"https://login.microsoftonline.com/{self._tenant_id}/oauth2/v2.0/token"

        # Headers for the token request
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        # Data for the token request
        data = {
            "grant_type": "client_credentials",
            "client_id": self._client_id,
            "client_secret": self._client_secret,
            "scope": "https://graph.microsoft.com/.default",
        }

        # Make the token request
        response = requests.post(url=url, headers=headers, data=data)
        # response.raise_for_status()

        # Extract the access token from the response
        self._token = response.json()["access_token"]

        return self._token

    def renew_token(self) -> None:
        """
        This method forces a re-authentication to obtain a new access token.

        The new token is stored in the _token attribute and returned.
        """
        self._token = self._authenticate()

    def send_email(self, recipients: list, subject: str, message: str, attachments: None | list = None) -> int:
        # Endpoint
        url = f"https://graph.microsoft.com/v1.0/users/{self._sender_email}/sendMail"

        # Headers
        headers = {
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json",
        }

        # Email message payload
        payload = {
            "message": {
                "subject": subject,
                "body": {"contentType": "HTML", "content": message},
                "toRecipients": [{"emailAddress": {"address": r}} for r in recipients],
            },
            "saveToSentItems": "true",
        }

        # Handle attachments if provided
        if attachments:
            payload["message"]["attachments"] = []

            for file_path in attachments:
                # Read and encode the file content
                with open(file_path, "rb") as f:
                    content_bytes = base64.b64encode(f.read()).decode("utf-8")

                # Append attachment to the message
                payload["message"]["attachments"].append(
                    {
                        "@odata.type": "#microsoft.graph.fileAttachment",
                        "name": os.path.basename(file_path),
                        "contentBytes": content_bytes,
                    }
                )

        # Send the email (202 Accepted)
        response = requests.post(url, headers=headers, json=message)
        # response.raise_for_status()

        return response.status_code


# eof
