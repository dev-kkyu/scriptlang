from tkinter import *

window = Tk() # Create a window
window.title("Connect Four") # Set title


class Cell(Canvas):
    def __init__(self, parent, row, col):
        Canvas.__init__(self, parent, width = 20, height = 20, bg = "blue", borderwidth = 2)
        self.color = "white"
        self.row = row
        self.col = col
        # https://tkdocs.com/shipman/canvas.html
        # https://tkdocs.com/shipman/create_oval.html
        self.create_oval(4, 4, 20, 20, fill = "white", tags="oval")
        self.bind("<Button-1>", self.clicked)

    def clicked(self, event): # red 또는 yellow 돌 놓기.
        nextcolor = "red" if self.color != "red" else "yellow"
        self.setColor(nextcolor)

    def setColor(self, color):
        self.delete("oval") # https://pythonguides.com/python-tkinter-canvas/
        self.color = color
        self.create_oval(4, 4, 20, 20, fill = self.color, tags="oval")


frame1 = Frame(window)
frame2 = Frame(window)
frame1.pack()
frame2.pack()

cells = []

for i in range(7): #i는 열
    cells.append([])
    for j in range(6): #j는 행
        cells[i].append(Cell(frame1, 5-j, i))
        cells[i][j].grid(row = 5-j, column = i)





window.mainloop() # Create an event loop