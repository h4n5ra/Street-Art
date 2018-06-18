from tkinter import *
from tkinter.filedialog import askopenfilename

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
        imageloc = Entry(top)
        upload = Button(top, text="Upload Image", command=lambda:self.selectImage(imageloc))
        nameLabel.grid(row=0)
        locationLabel.grid(row=1)
        nameInput.grid(row=0, column=1)
        locationInput.grid(row=1, column=1)
        imageloc.grid(row=2, column=1)
        upload.grid(row=2, column=2)
        createbutton = Button(bottom, text="Create, Sign and Send",
                              command=lambda: self.user.signArt(
                                  self.user.createArt(nameInput.get(), locationInput.get(), imageloc.get()), self.user.showPrivate()
                              ))
        createbutton.pack()

    def selectImage(self, entry):
        imageInput = askopenfilename()
        entry.insert(0, imageInput)