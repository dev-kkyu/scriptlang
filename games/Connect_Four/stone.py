from tkinter import *

window = Tk() # Create a window
window.title("Connect Four") # Set title

_MAXROW = 6
_MAXCOL = 7

Turn = ("red", "yellow", None) #: 다음 놓을 차례, None(게임끝일때)
turnNum = 0

restart_text = dict(start = "새로 시작", red = "red 승리!", yellow = "yellow 승리!")



def restart(): #함수 : process_button의 command 함수
    if process_button.text == restart_text['start']:
        global turnNum
        for i in range(_MAXROW): 
            for j in range(_MAXCOL):
                cells[i][j].setColor("white")
                cells[i][j].setBgColor("blue")
        turnNum = 0
    else:
        process_button.setText(restart_text['start'])

def Winner():
    pass

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
        if process_button.text != restart_text['start']:
            return
        if self.color == "white": #비어있는 셀이면 바꾸기
            if self.row == _MAXROW - 1 or cells[self.row + 1][self.col].color != "white": #가장 밑에 있는 셀이면
                self.setColor(Turn[turnNum])
                turnNum = (turnNum + 1) % 2
                self.__checkVertical(1)
                self.__checkHorizontal()

    def setColor(self, color):
        self.delete("oval")
        self.color = color
        self.create_oval(4, 4, 20, 20, fill = self.color, tags="oval")
    
    def setBgColor(self, color):
        self.config(bg = color)
    

    def __checkVertical(self, count): # : 열 방향 확인.
        if count == 4:
            for i in range(4):
                cells[self.row+i][self.col].setBgColor(self.color)
            process_button.setText(restart_text[self.color])
            return
        if self.row + count > 5:
            return
        if self.color == cells[self.row + count][self.col].color:
            self.__checkVertical(count + 1)
        

    def __checkHorizontal(self): # : 행 방향 확인.
        for i in range(4):
            if cells[self.row][i].color == cells[self.row][i+1].color == cells[self.row][i+2].color == cells[self.row][i+3].color == self.color != "white":
                for j in range(4):
                    cells[self.row][i+j].setBgColor(self.color)
                process_button.setText(restart_text[self.color])



    def __checkDiag1(self, count): # : / 방향 대각선 확인.
        pass


    def __checkDiag2(self, count): # : \ 방향 대각선 확인.
        pass




class pButton(Button):
    def __init__(self, container):
        self.text = restart_text['start']
        Button.__init__(self, container, command=restart, text=self.text)
    

    def setText(self, text):
        self.text = text
        self.config(text = text)




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