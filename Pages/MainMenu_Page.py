from tkinter import *
from tkinter import ttk
import tkinter
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk as objTTK
from functools import partial
import tkinter as tk
import subprocess
import os
import tkinter as objTK
import datetime as objDateTime
import customtkinter

# Main Menu Page Class
class MainMenu(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        customtkinter.CTkFrame.__init__(self, master )
        self.controller = controller

        # Slicing the page
        left_frame = customtkinter.CTkFrame(master=self, width=640, height=720, corner_radius=0)
        left_frame.place(relx=0.5, rely=0.5, anchor=tkinter.E)

        right_frame = customtkinter.CTkFrame(master=self, width=640, height=720, corner_radius=0)
        right_frame.place(relx=1, rely=0.5, anchor=tkinter.E)

        # Corner Picture (logo)
        logo_img = ImageTk.PhotoImage(file="assets/images/WVU_Logo.png")
        logo_widget = customtkinter.CTkLabel(left_frame, image=logo_img )
        logo_widget.image = logo_img
        logo_widget.place(x=0, y=20)

        # Picture on left side
        Welcome_img = ImageTk.PhotoImage(file="assets/images/WVU_Welcome.png")
        Welcome_widget = customtkinter.CTkLabel(left_frame, image=Welcome_img )
        Welcome_widget.image = Welcome_img
        Welcome_widget.place(relx=1, rely=0.5, anchor=tkinter.E)

        label_1 = customtkinter.CTkLabel(right_frame, text='Main Menu', text_font=("TkMenutext_font", 50))
        label_1.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        button_1 = customtkinter.CTkButton(right_frame, text="List of Items", text_font=("TkHeadingtext_font", 25) , cursor="hand2",
                                            width = 350, command=lambda:controller.show_frame("ItemsList"))
        button_1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        button_2 = customtkinter.CTkButton(right_frame, text="Recipe Suggestions", text_font=("TkHeadingtext_font", 25) , cursor="hand2",
                                            width = 350, command=lambda:controller.show_frame("RecipeSuggestions"))
        button_2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        button_3 = customtkinter.CTkButton(right_frame, text="Shopping List", text_font=("TkHeadingtext_font", 25) , cursor="hand2",
                                            width = 350, command=lambda:controller.show_frame("SuggestedShopping"))
        button_3.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        button_4 = customtkinter.CTkButton(right_frame, text="Settings", text_font=("TkHeadingtext_font", 25) , cursor="hand2",
                                            width = 350, command=lambda:controller.show_frame("Settings"))
        button_4.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)