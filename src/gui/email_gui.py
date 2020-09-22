import tkinter
import os
import smtplib
from tkinter import *

# Define functions and properties here

DEFAULT_SMTP_PORT = 587
EMAIL_SMTP_SERVERS = {
    "gmail.com": "smtp.gmail.com",
    "outlook.com": "smtp.office365.com",
    "hotmail.com": "smtp.office365.com"
}

email_provider_list = [
    "gmail.com",
    "outlook.com",
    "hotmail.com"
]

def service_login():
    email = str(email_address_form.get())
    password = str(password_form.get())
    subject = str(subject_form.get())
    body = str(body_form.get("1.0",END))
    receiver = str(receiver_form.get())
    split_email = email.split("@")
    if split_email[1] == email_provider_list[0]:
        split_email = EMAIL_SMTP_SERVERS["gmail.com"]
    elif split_email[1] == email_provider_list[1]:
        split_email = EMAIL_SMTP_SERVERS["outlook.com"]
    elif split_email[1] == email_provider_list[2]:
        split_email = EMAIL_SMTP_SERVERS["hotmail.com"]
    with smtplib.SMTP(split_email, DEFAULT_SMTP_PORT) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email, password)

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(email, receiver, msg)

# initalize master window
gui = tkinter.Tk()
gui.title("email client")
gui.resizable()
gui.geometry("700x200")
gui.configure(bg='#2b2d42')

# widgets
title = Label(gui, text="email client by celebi",)
email_label = Label(gui, text="email")
email_address_form = Entry(gui)
password_label = Label(gui, text="password")
password_form = Entry(gui, show="*")
subject_label = Label(gui, text="add a subject to your email")
subject_form = Entry(gui)
body_label = Label(gui, text="type your email here")
body_form = Text(gui)
receiver_label = Label(gui, text="receiver")
receiver_form = Entry(gui)
send_button = Button(gui, text="send email", pady=5, padx=30, command=service_login)

# locating the widget
title.pack()
email_label.pack()
email_address_form.pack()
password_label.pack()
password_form.pack()
subject_label.pack()
subject_form.pack()
body_label.pack()
body_form.pack()
receiver_label.pack()
receiver_form.pack()
send_button.pack()

# loop the master window
gui.mainloop()
