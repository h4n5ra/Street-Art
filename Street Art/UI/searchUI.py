from tkinter import *
import queries as q
import ipfsapi

class searchUI:

    def __init__(self, level):
        self.api = ipfsapi.connect("127.0.0.1", 5001)
        tframe = Frame(level, padx=20, pady=10)
        bframe = Frame(level, padx=20, pady=10)
        tframe.pack()
        bframe.pack()
        query = Entry(tframe)
        search = Button(tframe, text="Search", command=lambda: self.showResultsFancy(query.get(), bframe))
        query.pack()
        search.pack()

    def showResults(self, search, bottom):
        results = q.queries.searchtag(search)
        view = Text(bottom, width=100, height=100)
        view.insert("1.0", results)
        view.pack()

    def showResultsFancy(self, search, bottom):
        results = q.queries.searchtag(search)
        for r in results:
            try:
                frame = Frame(bottom, pady=10)
                namelabel = Label(frame, text="Name: ")
                locationlabel = Label(frame, text="Location: ")
                name = Entry(frame)
                location = Entry(frame)
                name.insert(0, r["data"]["name"])
                location.insert(0, r["data"]["location"])
                #photo = PhotoImage(file=self.getImage(r)+".png")
                #imagelabel = Label(frame, image=photo)
                namelabel.grid(row=0, column=0)
                name.grid(row=0, column=1)
                locationlabel.grid(row=1, column=0)
                location.grid(row=1, column=1)
                #imagelabel.pack()
                frame.pack()
            except:
                None

    def getImage(self, result):
        self.api.get(result["data"]["image hash"])
        return result["data"]["image hash"]
