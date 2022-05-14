from tkinter import *

window = Tk() # Create a window
window.title("Connect Four") # Set title

_MAXROW = 6
_MAXCOL = 7

Turn = ("red", "yellow", None) #: 다음 놓을 차례, None(게임끝일때)
turnNum = 0

restart_text = ("새로 시작", "red 승리!", "yellow 승리!")



def restart(): #함수 : process_button의 command 함수
    global cells
    if process_button.text == restart_text[0]:
        for i in range(_MAXROW): 
            for j in range(_MAXCOL):
                cells[i][j].setColor("white")
    elif process_button.text == restart_text[1] or process_button.text == restart_text[2]:
        process_button.text = restart_text[0]
        process_button.config(text = restart_text[0])


class Cell(Canvas):
    def __init__(self, parent, row, col):
        Canvas.__init__(self, parent, width = 20, height = 20, bg = "blue", borderwidth = 2)
        self.color = "white"
        self.row = row
        self.col = col
        self.create_oval(4, 4, 20, 20, fill = "white", tags="oval")
        self.bind("<Button-1>", self.clicked)
    
    def clicked(self, event): # red 또는 yellow 돌 놓기.
        global turnNum
        global cells
        if self.color == "white": #비어있는 셀이면 바꾸기
            if self.row == _MAXROW - 1 or cells[self.row + 1][self.col].color != "white": #가장 밑에 있는 셀이면
                self.setColor(Turn[turnNum])
                turnNum = (turnNum + 1) % 2

    def setColor(self, color):
        self.delete("oval")
        self.color = color
        self.create_oval(4, 4, 20, 20, fill = self.color, tags="oval")



class pButton(Button):
    def __init__(self, container):
        self.text = restart_text[0]
        Button.__init__(self, container, command=restart, text=self.text)



frame1 = Frame(window)
frame2 = Frame(window)
frame1.pack()
frame2.pack()

cells = []

for i in range(_MAXROW): #i는 행
    cells.append([])
    for j in range(_MAXCOL): #j는 열
        cells[i].append(Cell(frame1, i, j))
        cells[i][j].grid(row = i, column = j)


process_button = pButton(frame2) #: 하단의 버튼
process_button.pack()



window.mainloop() # Create an event loop