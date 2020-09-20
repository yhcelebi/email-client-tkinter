import os
import tkinter
import smtplib
import email_gui_service
from tkinter import *

# initalize master window
gui = tkinter.Tk()
gui.title("email client")
gui.resizable()
gui.geometry("700x200")
gui_service = Gui()

# widgets
email_address_form = Entry(gui, text="email address", height=5, width=15)
password_form = Entry(gui, text="email address", height=5, width=15)
submit_button = Button(gui, command=gui_service.get_input_from_form(email_address_form, password_form))

# locating the widget
email_address_form.pack()
password_form.pack()

# loop the master window
gui.mainloop()
