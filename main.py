from tkinter import *

window = Tk()  # Gui 생성
window.title("Subway")  # 창이름설정
window.geometry("1000x600+100+100")  # 창사이즈설정
window.resizable(True,True)  # 사이즈 변경 허용

frameside = Frame(window, relief="flat", bd=6, bg="#00B050")
frame = Frame(frameside, bd=0)

frameside.pack(fill = "both", expand=True)
frame.pack(fill = "both", expand=True)

Title = Label(frame, text="지하철 시간표 API", font = ("맑은 고딕",30), width = 30, height = 5)
Title.pack()

window.mainloop()
