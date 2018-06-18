from tkinter import *

class keysUI:

    def __init__(self, level, user):
        tframe = Frame(level, padx=20, pady=10)
        bframe = Frame(level, padx=20, pady=10)
        tframe.pack()
        bframe.pack()
        label1 = Label(tframe, text="Your public key:")
        publickey = Entry(tframe, width=60)
        label2 = Label(bframe, text="Your private key:")
        privatekey = Entry(bframe, width=60)
        publickey.insert(0, user.showPublic())
        privatekey.insert(0, user.showPrivate())
        label1.pack()
        publickey.pack()
        label2.pack()
        privatekey.pack()
