from tkinter import *

class keysUI:

    def __init__(self, level, user):
        self.user = user
        tframe = Frame(level, padx=20, pady=10)
        bframe = Frame(level, padx=20, pady=10)
        tframe.pack()
        bframe.pack()
        label1 = Label(tframe, text="Enter your private key:")
        private = Entry(tframe, width=60)
        ok = Button(bframe, text="Sign")
