from tkinter import *

window = Tk()

window.title("Tic-Tac-Toe")
window.geometry("240x330+100+100")
window.resizable(True, True)  

count=0

def countUP():
    global count
    count +=1
    label.config(text=str(count))

label=Label(window, text="파이썬", width=100, height=1, fg="red")
#label.pack() 
label.place(x=0, y=260, relwidth=1)

button1 = Button(window,text="클릭", overrelief="solid", width=10, height=5, command=countUP, repeatdelay=1000, repeatinterval=100)
#button1.pack() #grid와 같이 못씀
#button1.place()
button2 = Button(window,text="클릭", overrelief="solid", width=10, height=5, command=countUP, repeatdelay=1000, repeatinterval=100)
#button2.pack()
#button2.place()
button3 = Button(window,text="클릭", overrelief="solid", width=10, height=5, command=countUP, repeatdelay=1000, repeatinterval=100)
# button3.pack()
button4 = Button(window,text="클릭", overrelief="solid", width=10, height=5, command=countUP, repeatdelay=1000, repeatinterval=100)
# button4.pack()
button5 = Button(window,text="클릭", overrelief="solid", width=10, height=5, command=countUP, repeatdelay=1000, repeatinterval=100)
#button5.pack()
button6 = Button(window,text="클릭", overrelief="solid", width=10, height=5, command=countUP, repeatdelay=1000, repeatinterval=100)
button7 = Button(window,text="클릭", overrelief="solid", width=10, height=5, command=countUP, repeatdelay=1000, repeatinterval=100)
button8 = Button(window,text="클릭", overrelief="solid", width=10, height=5, command=countUP, repeatdelay=1000, repeatinterval=100)
button9 = Button(window,text="클릭", overrelief="solid", width=10, height=5, command=countUP, repeatdelay=1000, repeatinterval=100)

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