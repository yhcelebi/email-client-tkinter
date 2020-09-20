import smtplib
import os

with smtplib.SMTP(SMTP_PROVIDER, SMTP_PORT) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()