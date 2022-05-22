from tkinter import *

window = Tk()  # Gui 생성
window.title("Subway")  # 창이름설정
window.geometry("980x600+100+100")  # 창사이즈설정
window.resizable(True,False)  # 사이즈 변경 허용

frameside = Frame(window, relief="flat", bd=6, bg="#00B050") # 테두리 전용 프레임
Main = Frame(frameside, bd=0) # 메인창

frameside.pack(fill = "both", expand=True) 
Main.pack(fill = "both", expand=True)


frame1 = Frame(Main, relief="solid", bd=1)
frame1.pack(fill="both")

frame1left = Frame(frame1, relief="solid", bd=1)
frame1left.pack(fill="both", side="left")

frame1right = Frame(frame1, relief="solid", bd=1)
frame1right.pack(fill="both", expand = True, side="left")

Title = Label(frame1left, text="언제타 지하철", font = ("맑은 고딕",44, "bold"), height=1, width=13)
Title.pack(fill = "both")

textframe = Frame(frame1right, relief = "flat", bd=3, bg = "#64C044")
textframe.pack(side = "left", padx = 20)

input_text = Entry(textframe, width=50)
input_text.pack(fill = "both", side = "left")

button = Button(textframe, text="검색", font = ("맑은 고딕",15), height= 1, width = 7, bg = "#92D050", padx = 10)
button.pack( side = "left")

frame2 = Frame(Main)
frame2.pack(fill="both", padx = 20)

subwayLineButton = []
for i in range(8):
    subwayLineButton.append(Button(frame2, text=str(i+1)+"호선", font = ("맑은 고딕", 15, "bold"), width = 7, height = 1, fg = "white", bg = "#92D050"))
    subwayLineButton[i].pack(side = "left", padx = 5, pady = 13)

frame3 = Frame(Main, relief = "solid", bd=1)
frame3.pack(fill="both")

frame3left = Frame(frame3, relief = "solid", bd=1)
frame3right = Frame(frame3, relief = "solid", bd=1)
frame3left.pack(fill="both", side = "left")
frame3right.pack(fill="both", side = "left", expand = True)

subwaylist = Label(frame3left, text = "호선별 역 목록", width = 68, height = 2, relief = "solid", bd=1, bg = "#64C044")
subwaytime = Label(frame3right, text = "역 열차 시간표", height = 2, relief = "solid", bd=1, bg = "#64C044")

subwaylist.pack(fill = "both")
subwaytime.pack(fill = "both")

test1label = Label(frame3left, text = "left",  height = 16) #나중에 지울거
test2label = Label(frame3right, text = "right")

test1label.pack(fill = "both")
test2label.pack(fill = "both")

frame4 = Frame(Main, relief = "solid", bd=1)
frame4.pack(fill="both", expand = True)

graphframe = Frame(frame4, relief = "solid", bd=1, width = 685)
graphframe.pack(fill = "both", side = "left")

email = Button(frame4, width = 16)
kakaomap = Button(frame4)

email.pack(fill = "both", side = "left", padx = 10, pady = 10)
kakaomap.pack(fill = "both", side = "left", expand = True, padx = 10, pady = 10)

window.mainloop()

