from tkinter import * #tkinter 모듈에 있는 모든 함수 포함


window = Tk() #Gui 생성

window.title("Tic-Tac-Toe") #창이름설정
window.geometry("250x270+100+100") #창사이즈설정
window.resizable(False, False) #사이즈 변경 허용

img_empty=PhotoImage(file="./image/empty.gif")
img_x=PhotoImage(file="./image/x.gif")
img_o=PhotoImage(file="./image/o.gif")

img_empty=img_empty.zoom(2, 2)
img_x=img_x.zoom(2, 2)
img_o=img_o.zoom(2, 2)



count=0

ButtonIndex = [0,0,0,0,0,0,0,0,0]
GameEnd = 0

numcases = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

FrameObject = []
for i in range(4):
    FrameObject.append(Frame(window, padx=0, pady=0))
for i in range(3):
    FrameObject[i].pack(fill="both", expand=True)

FrameObject[3].pack(side="bottom", fill="both", expand=True)



def changebutton(num):
    global count
    global ButtonIndex
    global GameEnd
    global numcases

    if GameEnd != 0:
        return

    if ButtonIndex[num-1] != 0:
        return

    count +=1

    if count%2==0:
        output = printtext[0]
    else:
        output = printtext[1]

    label.config(text=output)


    
    if count%2==1:
        ButtonObject[num-1].config(image=img_x)
        
        ButtonIndex[num-1] = 1

    elif count%2==0:
        
        ButtonObject[num-1].config(image=img_o)
        
        ButtonIndex[num-1] = 2
    

    AllcheckEndcases(numcases)

    drawcheck = 0
    for i in ButtonIndex:
        if i != 0:
            drawcheck += 1
    if drawcheck == 9 and GameEnd ==0:
        GameEnd = 3
        label.config(text = printtext[2])





def checkEndcases(numcase):
    global GameEnd
    if ButtonIndex[numcase[0]]==ButtonIndex[numcase[1]]==ButtonIndex[numcase[2]] and ButtonIndex[numcase[0]]!=0:
        if ButtonIndex[numcase[0]] == 1:
            label.config(text = printtext[3])
            GameEnd = 1
        elif ButtonIndex[numcase[0]] == 2:
            label.config(text = printtext[4])
            GameEnd = 2

def AllcheckEndcases(numcases):
    for i in numcases:
        checkEndcases(i)


ButtonObject = [
    Button(FrameObject[0], image=img_empty, bd=0,  width=80, height=80, command=lambda: changebutton(1), repeatdelay=1000, repeatinterval=100),
    Button(FrameObject[0], image=img_empty, bd=0,  width=80, height=80, command=lambda: changebutton(2), repeatdelay=1000, repeatinterval=100),
    Button(FrameObject[0], image=img_empty, bd=0,  width=80, height=80, command=lambda: changebutton(3), repeatdelay=1000, repeatinterval=100),
    Button(FrameObject[1], image=img_empty, bd=0,  width=80, height=80, command=lambda: changebutton(4), repeatdelay=1000, repeatinterval=100),
    Button(FrameObject[1], image=img_empty, bd=0,  width=80, height=80, command=lambda: changebutton(5), repeatdelay=1000, repeatinterval=100),
    Button(FrameObject[1], image=img_empty, bd=0,  width=80, height=80, command=lambda: changebutton(6), repeatdelay=1000, repeatinterval=100),
    Button(FrameObject[2], image=img_empty, bd=0,  width=80, height=80, command=lambda: changebutton(7), repeatdelay=1000, repeatinterval=100),
    Button(FrameObject[2], image=img_empty, bd=0,  width=80, height=80, command=lambda: changebutton(8), repeatdelay=1000, repeatinterval=100),
    Button(FrameObject[2], image=img_empty, bd=0,  width=80, height=80, command=lambda: changebutton(9), repeatdelay=1000, repeatinterval=100)
]




for i in ButtonObject:
    i.pack(side="left",expand=True, fill="both")

printtext = ["X 차례", "O 차례", "비김! 게임이 끝났습니다",  "X 승리! 게임이 끝났습니다", "O 승리! 게임이 끝났습니다"]



label=Label(FrameObject[3], text=printtext[0], width=100, height=1)
label.pack(fill="both", expand=True)
        

window.mainloop()
