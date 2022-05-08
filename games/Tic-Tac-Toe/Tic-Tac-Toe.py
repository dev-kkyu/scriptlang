from tkinter import *  # tkinter 모듈에 있는 모든 함수 포함

window = Tk()  # Gui 생성
window.title("Tic-Tac-Toe")  # 창이름설정
window.geometry("250x270+100+100")  # 창사이즈설정
window.resizable(False, False)  # 사이즈 변경 허용

images = dict(Empty = PhotoImage(file="./image/empty.gif").zoom(2, 2), X= PhotoImage(file="./image/x.gif").zoom(2, 2), O = PhotoImage(file="./image/o.gif").zoom(2, 2))
currentToken = 'X'

printtext = ["X 차례", "O 차례", "비김! 게임이 끝났습니다", "X 승리! 게임이 끝났습니다", "O 승리! 게임이 끝났습니다"]

numcases = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

GameEnd = 0


class Cell(Button):
    def __init__(self, container):
        Button.__init__(self, container, image=images['Empty'], command=self.onClick, bd=0,  width=80, height=80, repeatdelay=1000, repeatinterval=100)
        self.token = 'Empty'

    def onClick(self):
        global currentToken

        if GameEnd != 0 or self.token != 'Empty': return
        
        self.config(image = images[currentToken])
        self.token = currentToken
        if currentToken == 'O':
            currentToken = 'X'
            label.config(text = printtext[0])
        else:
            currentToken = 'O'
            label.config(text = printtext[1])

        AllcheckEndcases(numcases)
        

    def getToken(self):
        return self.token



def drawCheck():
    global GameEnd

    count = 0
    for i in Cells:
        if i.getToken() != 'Empty':
            count += 1
    if count == 9 and GameEnd == 0:
        GameEnd = 3
        label.config(text = printtext[2])


def AllcheckEndcases(numcases):
    for i in numcases:
        checkEndcases(i)
    drawCheck()


def checkEndcases(numcase):
    global GameEnd
    if Cells[numcase[0]].getToken() == Cells[numcase[1]].getToken() == Cells[numcase[2]].getToken() and Cells[numcase[0]].getToken() != 'Empty':
        if Cells[numcase[0]].getToken() == 'X':
            label.config(text=printtext[3])
            GameEnd = 1
        elif Cells[numcase[0]].getToken() == 'O':
            label.config(text=printtext[4])
            GameEnd = 2


Frames = []
for i in range(4):
    Frames.append(Frame(window, padx=0, pady=0))
for i in range(3):
    Frames[i].pack(fill="both", expand=True)

Frames[3].pack(side="bottom", fill="both", expand=True)


Cells = []
for i in range(9):
    Cells.append(Cell(Frames[i // 3]))

for i in Cells:
    i.pack(side="left", expand=True, fill="both")

label = Label(Frames[3], text=printtext[0], width=100, height=1)
label.pack(fill="both", expand=True)


window.mainloop()

print("test")