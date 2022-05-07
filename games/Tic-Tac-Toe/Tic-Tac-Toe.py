from tkinter import * #tkinter 모듈에 있는 모든 함수 포함

window = Tk() #Gui 생성

window.title("Tic-Tac-Toe") #창이름설정
window.geometry("260x330+100+100") #창사이즈설정
window.resizable(True, False) #사이즈 변경 허용

img_empty=PhotoImage(file="./image/empty.gif")
img_x=PhotoImage(file="./image/x.gif")
img_o=PhotoImage(file="./image/o.gif")

# label_empty=Button(window, image=img_empty)
# label_x=Button(window, image=img_x)
# label_o=Button(window, image=img_o)

# label_empty.pack()#side="top")
# label_x.pack()#side="bottom")
# label_o.pack()#side="right")

count=0

def changebutton(num):
    global count
    count +=1
    label.config(text=str(count))
    if count%2==1:
        if num==1:
            button1.config(image=img_x)
        if num==2:
            button2.config(image=img_x)
        if num==3:
            button3.config(image=img_x)
        if num==4:
            button4.config(image=img_x)
        if num==5:
            button5.config(image=img_x)
        if num==6:
            button6.config(image=img_x)
        if num==7:
            button7.config(image=img_x)
        if num==8:
            button8.config(image=img_x)
        if num==9:
            button9.config(image=img_x)
    elif count%2==0:
        if num==1:
            button1.config(image=img_o)
        if num==2:
            button2.config(image=img_o)
        if num==3:
            button3.config(image=img_o)
        if num==4:
            button4.config(image=img_o)
        if num==5:
            button5.config(image=img_o)
        if num==6:
            button6.config(image=img_o)
        if num==7:
            button7.config(image=img_o)
        if num==8:
            button8.config(image=img_o)
        if num==9:
            button9.config(image=img_o)


# def changeButton1:
#     pass

# def changeButton2:
#     pass




label=Label(window, text="파이썬", width=100, height=1, fg="red")
#label.pack() 
label.place(x=0, y=260, relwidth=1)

button1 = Button(window,image=img_empty, overrelief="solid", width=30, height=30, command=lambda: changebutton(1), repeatdelay=1000, repeatinterval=100)
#button1.pack() #grid와 같이 못씀
#button1.place()
button2 = Button(window,image=img_empty, overrelief="solid", width=30, height=30, command=lambda: changebutton(2), repeatdelay=1000, repeatinterval=100)
#button2.pack()
#button2.place()
button3 = Button(window,image=img_empty, overrelief="solid", width=30, height=30, command=lambda: changebutton(3), repeatdelay=1000, repeatinterval=100)
# button3.pack()
button4 = Button(window,image=img_empty, overrelief="solid", width=30, height=30, command=lambda: changebutton(4), repeatdelay=1000, repeatinterval=100)
# button4.pack()
button5 = Button(window,image=img_empty, overrelief="solid", width=30, height=30, command=lambda: changebutton(5), repeatdelay=1000, repeatinterval=100)
#button5.pack()
button6 = Button(window,image=img_empty, overrelief="solid", width=30, height=30, command=lambda: changebutton(6), repeatdelay=1000, repeatinterval=100)
button7 = Button(window,image=img_empty, overrelief="solid", width=30, height=30, command=lambda: changebutton(7), repeatdelay=1000, repeatinterval=100)
button8 = Button(window,image=img_empty, overrelief="solid", width=30, height=30, command=lambda: changebutton(8), repeatdelay=1000, repeatinterval=100)
button9 = Button(window,image=img_empty, overrelief="solid", width=30, height=30, command=lambda: changebutton(9), repeatdelay=1000, repeatinterval=100)

button1.grid(row=0, column=0) #버튼 위치 지정
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

# text=Text(window)

# text.insert(CURRENT,"안녕하세요.\n")



# #text.pack()

window.mainloop()
