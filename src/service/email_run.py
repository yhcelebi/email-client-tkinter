import smtplib
import src.gui.email_gui
import src.service.email_service

email_service = src.service.email_service.Service()
SMTP_PROVIDER = email_service.get_smtp_provider(src.gui.email_gui.split_get_submit[1])

with smtplib.SMTP(SMTP_PROVIDER, src.service.email_service.Service.DEFAULT_SMTP_PORT) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    subject = ""
