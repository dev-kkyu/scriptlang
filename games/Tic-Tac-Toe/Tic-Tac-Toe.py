from tkinter import * #tkinter 모듈에 있는 모든 함수 포함

window = Tk() #Gui 생성

window.title("Tic-Tac-Toe") #창이름설정
window.geometry("300x330+100+100") #창사이즈설정
window.resizable(True, True) #사이즈 변경 허용

img_empty=PhotoImage(file="./image/empty.gif")
img_x=PhotoImage(file="./image/x.gif")
img_o=PhotoImage(file="./image/o.gif")

label_empty=Button(window, image=img_empty)
label_x=Button(window, image=img_x)
label_o=Button(window, image=img_o)

label_empty.pack()#side="top")
label_x.pack()#side="bottom")
label_o.pack()#side="right")


window.mainloop() #윈도우 실행

