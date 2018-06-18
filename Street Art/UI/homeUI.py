from tkinter import *
import user as u
from UI import keysUI as k
from UI import createUI as c
from UI import searchUI as s
import csv

class homeUI:

    def __init__(self):
        self.root = Tk()
        self.root.title("Street Art")
        self.root.geometry('500x200')
        self.root.config(menu=self.createMenu())
        self.buildUI()
        self.root.mainloop()

    def buildUI(self):
        tframe = Frame(self.root, pady=10)
        bframe = Frame(self.root, pady=20)
        tframe.pack(side=TOP)
        bframe.pack(side=BOTTOM)
        self.createWidgets(tframe, bframe)

    def createWidgets(self, top, bottom):
        username = Label(top, text="Enter username:")
        usernameInput = Entry(top)
        createUser = Button(bottom, text="Create a user", command=lambda:self.createNewUser(usernameInput.get()))
        search = Button(bottom, text="Search for Art", command=lambda: self.searchWindow())
        username.pack()
        usernameInput.pack()
        createUser.pack()
        search.pack()

    def createMenu(self):
        users = Menu(self.root)
        self.userlist = Menu(users)
        users.add_cascade(label="Users", menu=self.userlist)
        return users

    def createNewUser(self, username):
        newuser = u.user(username)
        self.userlist.add_command(label=username, command=lambda: self.selectUser(newuser))
        file = open("users.csv", "a")
        writer = csv.writer(file, lineterminator="\n")
        writer.writerows([[username, newuser.showPublic()]])
        file.close()
        win = Toplevel()
        dow = k.keysUI(win, newuser)

    def getUserList(self):
        _userlist = open("users.csv", "r")
        reader = csv.reader(_userlist)
        data = [r for r in reader]
        _userlist.close()
        return data

    def selectUser(self, user):
        win = Toplevel()
        win.geometry("400x200")
        dow = c.createUI(win, user)

    def searchWindow(self):
        win = Toplevel()
        win.geometry("400x400")
        down = s.searchUI(win)

ui = homeUI()