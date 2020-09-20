import smtplib
import os


class Service:

    DEFAULT_SMTP_PORT: 587
    EMAIL_SMTP_SERVERS = {
        "gmail": "smtp.gmail.com",
        "outlook": "smtp.office365.com",
        "hotmail": "smtp.office365.com"
    }

    def __init__(self):
        pass

    @staticmethod
    def get_smtp_provider(SMTP_PROVIDER, SMTP_PORT):
        if SMTP_PROVIDER == "gmail":
            return EMAIL_SMTP_SERVERS["gmail"]
        

    @staticmethod
    def account_login(EMAIL_ADDRESS, EMAIL_PASSWORD):
        return smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)


