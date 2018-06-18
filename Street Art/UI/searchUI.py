from tkinter import *
import queries as q

class searchUI:

    def __init__(self, level):
        tframe = Frame(level, padx=20, pady=10)
        bframe = Frame(level, padx=20, pady=10)
        tframe.pack()
        bframe.pack()
        query = Entry(tframe)
        search = Button(tframe, text="Search", command=lambda: self.showResults(query.get(), bframe))
        query.pack()
        search.pack()

    def showResults(self, search, bottom):
        results = q.queries.searchtag(search)
        view = Text(bottom, width=100, height=100)
        view.insert("1.0", results)
        view.pack()