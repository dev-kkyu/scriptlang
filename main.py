from tkinter import *

window = Tk()  # Gui 생성
window.title("언제타 지하철")  # 창이름설정
window.geometry("1000x600+100+100")  # 창사이즈설정
window.resizable(True,True)  # 사이즈 변경 허용


frameside = Frame(window, relief="flat", bd=6, bg="#00B050")
frame1 = Frame(frameside, bd=0)
frame2 = Frame(frameside, bd=0)
frame3 = Frame(frameside, bd=0)
frame4 = Frame(frameside, bd=0)

frameside.pack(fill = "both", expand=True)
frame1.pack(fill = "both", expand=True)
frame2.pack(fill = "both", expand=True)
frame3.pack(fill = "both", expand=True)
frame4.pack(fill = "both", expand=True)

Title = Label(frame1, text="언제타 지하철", font = ("맑은 고딕",30), width = 30)
Title.grid(row=0, column=0)

input_text = Entry(frame1, width=30) 
input_text.grid(row=0, column=1) 

button = Button(frame1, text="확인") 
button.grid(row=0, column=2)



button1 = Button(frame2, text="1호선",width=12,height=4)
button2 = Button(frame2, text="2호선",width=12,height=4)
button3 = Button(frame2, text="3호선",width=12,height=4)
button4 = Button(frame2, text="4호선",width=12,height=4)
button5 = Button(frame2, text="5호선",width=12,height=4)
button6 = Button(frame2, text="6호선",width=12,height=4)
button7 = Button(frame2, text="7호선",width=12,height=4)
button8 = Button(frame2, text="8호선",width=12,height=4)
button9 = Button(frame2, text="9호선",width=12,height=4)
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=0, column=3)
button5.grid(row=0, column=4)
button6.grid(row=0, column=5)
button7.grid(row=0, column=6)
button8.grid(row=0, column=7)
button9.grid(row=0, column=8)

image=Label(frame2, text="N호선 사진",width=12,height=5,relief="solid")
image.grid(row=0, column=9)



label=Label(frame3, text="역목록", width=67, height=15,relief="solid")
label.grid(row=0, column=0)

label1=Label(frame3, text="시간표", width=67, height=15,relief="solid")
label1.grid(row=0, column=1)


graph=Label(frame4, text="그래프", width=100, height=7,relief="solid")
graph.grid(row=0, column=0)

email = Button(frame4, text="이메일",width=16,height=7)
map = Button(frame4, text="지도",width=16,height=7)

email.grid(row=0, column=1)
map.grid(row=0, column=2)

window.mainloop()
