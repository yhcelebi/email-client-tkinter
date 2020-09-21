import tkinter
import os
import smtplib
from src.gui.email_gui_service import Gui
from tkinter import *

# initalize master window
gui = tkinter.Tk()
gui.title("email client")
gui.resizable()
gui.geometry("700x200")
gui_service = Gui()

# widgets
title = Label(gui, text="email client by celebi",)
email_address_form = Entry(gui)
password_form = Entry(gui)
submit_button = Button(gui, text="submit", pady=5, padx=30, command=lambda: gui_service.get_input())
subject_label = Label(gui, text="add a subject to your email")
subject_form = Entry(gui)
body_label = Label(gui, text="type your email here")
body_form = Text(gui)
receiver_form = Entry(gui)
sender_form = Entry(gui)
send_button = Button(gui, text="send email", pady=5, padx=30)
get_submit = str(submit_button)
split_get_submit = get_submit.split("@")

# locating the widget
title.pack()
email_address_form.pack()
password_form.pack()
submit_button.pack()
subject_label.pack()
subject_form.pack()
body_label.pack()
body_form.pack()
receiver_form.pack()
sender_form.pack()
send_button.pack()

# loop the master window
gui.mainloop()
