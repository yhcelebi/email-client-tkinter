import smtplib
import os


class Service:
    global DEFAULT_SMTP_PORT
    DEFAULT_SMTP_PORT = 587
    global EMAIL_SMTP_SERVERS
    EMAIL_SMTP_SERVERS = {
        "gmail.com": "smtp.gmail.com",
        "outlook.com": "smtp.office365.com",
        "hotmail.com": "smtp.office365.com"
    }

    def __init__(self):
        pass

    @staticmethod
    def get_smtp_provider(SMTP_PROVIDER):
        if SMTP_PROVIDER == "gmail.com":
            return EMAIL_SMTP_SERVERS["gmail.com"]
        elif SMTP_PROVIDER == "outlook.com":
            return EMAIL_SMTP_SERVERS["outlook.com"]
        elif SMTP_PROVIDER == "hotmail.com":
            return EMAIL_SMTP_SERVERS["hotmail.com"]

    @staticmethod
    def account_login(EMAIL_ADDRESS, EMAIL_PASSWORD, ALIAS):
        return ALIAS.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
