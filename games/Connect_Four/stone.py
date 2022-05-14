from tkinter import *

window = Tk() # Create a window
window.title("Connect Four") # Set title



_MAXROW = 6
_MAXCOL = 7

Turn = ("red", "yellow", None) #: 다음 놓을 차례 None(게임끝일때)
turnNum = 0

process_button = None #: 하단의 버튼

restart_text ="새로 시작"
# : process_button[“text”]로 사용.
# : “새로 시작”인지 “~ 승리”인지 구분에 사용.

def restart(): #함수 : process_button의 command 함수
    pass


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
        global turnNum
        if(self.color == "white"):
            self.setColor(Turn[turnNum])
            turnNum = (turnNum + 1) % 2

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