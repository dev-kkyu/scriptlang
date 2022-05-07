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

def changebutton(num):
    global count
    global ButtonIndex
    global GameEnd

    if GameEnd != 0:
        return

    if ButtonIndex[num-1] != 0:
        return

    count +=1

    if count%2==0:
        output = playerx
    else:
        output = playero

    label.config(text=output)


    
    if count%2==1:
        if num==1:
            button1.config(image=img_x)
        elif num==2:
            button2.config(image=img_x)
        elif num==3:
            button3.config(image=img_x)
        elif num==4:
            button4.config(image=img_x)
        elif num==5:
            button5.config(image=img_x)
        elif num==6:
            button6.config(image=img_x)
        elif num==7:
            button7.config(image=img_x)
        elif num==8:
            button8.config(image=img_x)
        elif num==9:
            button9.config(image=img_x)
        
        ButtonIndex[num-1] = 1

    elif count%2==0:
        if num==1:
            button1.config(image=img_o)
        elif num==2:
            button2.config(image=img_o)
        elif num==3:
            button3.config(image=img_o)
        elif num==4:
            button4.config(image=img_o)
        elif num==5:
            button5.config(image=img_o)
        elif num==6:
            button6.config(image=img_o)
        elif num==7:
            button7.config(image=img_o)
        elif num==8:
            button8.config(image=img_o)
        elif num==9:
            button9.config(image=img_o)
        
        ButtonIndex[num-1] = 2
    

    
    if ButtonIndex[0]==ButtonIndex[1]==ButtonIndex[2]and ButtonIndex[0]!=0:
        if ButtonIndex[0] == 1:
            label.config(text = xwin)
            GameEnd = 1
        elif ButtonIndex[0] == 2:
            label.config(text = owin)
            GameEnd = 2
    elif ButtonIndex[3]==ButtonIndex[4]==ButtonIndex[5]and ButtonIndex[3]!=0:
        if ButtonIndex[3] == 1:
            label.config(text = xwin)
            GameEnd = 1
        elif ButtonIndex[3] == 2:
            label.config(text = owin)
            GameEnd = 2
    elif ButtonIndex[6]==ButtonIndex[7]==ButtonIndex[8]and ButtonIndex[6]!=0:
        if ButtonIndex[6] == 1:
            label.config(text = xwin)
            GameEnd = 1
        elif ButtonIndex[6] == 2:
            label.config(text = owin)
            GameEnd = 2
    elif ButtonIndex[0]==ButtonIndex[3]==ButtonIndex[6]and ButtonIndex[0]!=0:
        if ButtonIndex[0] == 1:
            label.config(text = xwin)
            GameEnd = 1
        elif ButtonIndex[0] == 2:
            label.config(text = owin)
            GameEnd = 2
    elif ButtonIndex[1]==ButtonIndex[4]==ButtonIndex[7]and ButtonIndex[1]!=0:
        if ButtonIndex[1] == 1:
            label.config(text = xwin)
            GameEnd = 1
        elif ButtonIndex[1] == 2:
            label.config(text = owin)
            GameEnd = 2
    elif ButtonIndex[2]==ButtonIndex[5]==ButtonIndex[8]and ButtonIndex[2]!=0:
        if ButtonIndex[2] == 1:
            label.config(text = xwin)
            GameEnd = 1
        elif ButtonIndex[2] == 2:
            label.config(text = owin)
            GameEnd = 2
    elif ButtonIndex[0]==ButtonIndex[4]==ButtonIndex[8]and ButtonIndex[0]!=0:
        if ButtonIndex[0] == 1:
            label.config(text = xwin)
            GameEnd = 1
        elif ButtonIndex[0] == 2:
            label.config(text = owin)
            GameEnd = 2
    elif ButtonIndex[2]==ButtonIndex[4]==ButtonIndex[6]and ButtonIndex[2]!=0:
        if ButtonIndex[2] == 1:
            label.config(text = xwin)
            GameEnd = 1
        elif ButtonIndex[2] == 2:
            label.config(text = owin)
            GameEnd = 2

    drawcheck = 0
    for i in ButtonIndex:
        if i != 0:
            drawcheck += 1
    if drawcheck == 9 and GameEnd ==0:
        GameEnd = 3
        label.config(text = draw)



frame1=Frame(window, padx=0, pady=0)
frame2=Frame(window, padx=0, pady=0)
frame3=Frame(window, padx=0, pady=0)
frame1.pack(fill="both", expand=True)
frame2.pack(fill="both", expand=True)
frame3.pack(fill="both", expand=True)

frame4=Frame(padx=0, pady=0)
frame4.pack(side="bottom", fill="both", expand=True)


button1 = Button(frame1, image=img_empty, bd=0,  width=80, height=80, command=lambda: changebutton(1), repeatdelay=1000, repeatinterval=100)
button2 = Button(frame1, image=img_empty, bd=0,  width=80, height=80, command=lambda: changebutton(2), repeatdelay=1000, repeatinterval=100)
button3 = Button(frame1, image=img_empty, bd=0,  width=80, height=80, command=lambda: changebutton(3), repeatdelay=1000, repeatinterval=100)
button4 = Button(frame2, image=img_empty, bd=0,  width=80, height=80, command=lambda: changebutton(4), repeatdelay=1000, repeatinterval=100)
button5 = Button(frame2, image=img_empty, bd=0,  width=80, height=80, command=lambda: changebutton(5), repeatdelay=1000, repeatinterval=100)
button6 = Button(frame2, image=img_empty, bd=0,  width=80, height=80, command=lambda: changebutton(6), repeatdelay=1000, repeatinterval=100)
button7 = Button(frame3, image=img_empty, bd=0,  width=80, height=80, command=lambda: changebutton(7), repeatdelay=1000, repeatinterval=100)
button8 = Button(frame3, image=img_empty, bd=0,  width=80, height=80, command=lambda: changebutton(8), repeatdelay=1000, repeatinterval=100)
button9 = Button(frame3, image=img_empty, bd=0,  width=80, height=80, command=lambda: changebutton(9), repeatdelay=1000, repeatinterval=100)



button1.pack(side="left",expand=True, fill="both")
button2.pack(side="left",expand=True, fill="both")
button3.pack(side="left",expand=True, fill="both")
button4.pack(side="left",expand=True, fill="both")
button5.pack(side="left",expand=True, fill="both")
button6.pack(side="left",expand=True, fill="both")
button7.pack(side="left",expand=True, fill="both")
button8.pack(side="left",expand=True, fill="both")
button9.pack(side="left",expand=True, fill="both")



playerx = "x 차례"
playero = "o 차례"
draw = "비김! 게임이 끝났습니다"
xwin = "X 승리! 게임이 끝났습니다"
owin = "O 승리! 게임이 끝났습니다"




label=Label(frame4, text=playerx, width=100, height=1)
label.pack(fill="both", expand=True)




        

window.mainloop()
