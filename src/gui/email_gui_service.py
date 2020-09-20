import tkinter as tk
import os
import smtplib
from tkinter import *

class Gui:
    def __init__(self):
        pass

    @staticmethod
    def get_input_from_form(email, password):
        form_email = email.get()
        form_password = password.get()
        print(form_email, form_password)