from tkinter import *
from UI import signUI
import user as u

class createUI:

    def __init__(self, _level, _user):
        self.user = _user
        self.level = _level
        self.buildUI(self.level)

    def buildUI(self, level):
        tframe = Frame(level, padx=20, pady=20)
        bframe = Frame(level, padx=20, pady=20)
        self.createWidgets(tframe, bframe)
        tframe.pack(side=TOP)
        bframe.pack(side=BOTTOM)

    def createWidgets(self, top, bottom):
        nameLabel = Label(top, text="Name:")
        locationLabel = Label(top, text="Location:")
        nameInput = Entry(top)
        locationInput = Entry(top)
        nameLabel.grid(row=0)
        locationLabel.grid(row=1)
        nameInput.grid(row=0, column=1)
        locationInput.grid(row=1, column=1)
        createbutton = Button(bottom, text="Create, Sign and Send", padx=5,
                              command=lambda: self.user.signArt(
                                  self.user.createArt(nameInput.get(), locationInput.get(), "No Image"), self.user.showPrivate()
                              ))
        # signButton = Button(bottom, text="Sign/Send", padx=5)
        createbutton.pack()
        # signButton.pack()
