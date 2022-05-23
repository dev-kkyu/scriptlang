from loadapi import *
from tkinter import *

window = Tk()  # Gui 생성
window.title("Subway")  # 창이름설정
window.geometry("990x600+100+100")  # 창사이즈설정
window.resizable(False, True)  # 사이즈 변경 허용

# subwayLineButton = []
# for i in range(8):
#     subwayLineButton.append(Button(frame2, text=str(i+1)+"호선", font = ("맑은 고딕", 15, "bold"), width = 7, height = 1, fg = "white", bg = "#92D050"))
#     subwayLineButton[i].pack(side = "left", padx = 5, pady = 13)

class LineNumButton(Button):
   def __init__(self, container, text):
      Button.__init__(self, container, text = text, command = self.onClick, font = ("맑은 고딕", 15, "bold"), width = 7, height = 1, fg = "white", bg = "#92D050")
      self.linenum = text[0]
   
   def onClick(self):
      global lineimage
      data = LoadSubwaystationtable(self.linenum)
      listbox1.delete(0, END)
      for i, x in enumerate(data):
         listbox1.insert(i, x)

      lineimage = PhotoImage(file = "./image/"+self.linenum+".png").subsample(16, 16)
      linephoto.config(image = lineimage)



def commandoutputSchedule():
   outputSchedule(input_text.get())

def outputSchedule(STATION_NM):
   data = LoadSubwayTimetable(STATION_NM)
   listbox2.delete(0, END)
   listbox3.delete(0, END)
   for i, x in enumerate(data['Schedule']['1']):
      listbox2.insert(i, x)
   for i, x in enumerate(data['Schedule']['2']):
      listbox3.insert(i, x)
   
   subwaytime.config(text = input_text.get()+"역 열차 시간표")



frameside = Frame(window, relief="flat", bd=6, bg="#00B050") # 테두리 전용 프레임
Main = Frame(frameside, bd=0, bg = "#FFFFFF") # 메인창

frameside.pack(fill = "both", expand=True) 
Main.pack(fill = "both", expand=True)


frame1 = Frame(Main, relief="solid", bd=1)
frame1.pack(fill="both")

frame1left = Frame(frame1, relief="solid", bd=1)
frame1left.pack(fill="both", side="left")

frame1right = Frame(frame1, relief="solid", bd=1, bg = "#FFFFFF")
frame1right.pack(fill="both", expand = True, side="left")

Title = Label(frame1left, text="언제타 지하철", font = ("맑은 고딕",44, "bold"), bg = "#FFFFFF", height=1, width=13)
Title.pack(fill = "both")

textframe = Frame(frame1right, relief = "flat", bd=3, bg = "#64C044")
textframe.pack(side = "left", padx = 20)

input_text = Entry(textframe, width=30, font = ("맑은 고딕",15))
input_text.pack(fill = "both", side = "left")

button = Button(textframe, text="검색", command = commandoutputSchedule, font = ("맑은 고딕",15), height= 1, width = 7, bg = "#92D050", padx = 10)
button.pack( side = "left")

frame2 = Frame(Main, bg = "#FFFFFF")
frame2.pack(fill="both", padx = 20)

subwayLineButton = []
# for i in range(8):
#     subwayLineButton.append(Button(frame2, text=str(i+1)+"호선", font = ("맑은 고딕", 15, "bold"), width = 7, height = 1, fg = "white", bg = "#92D050"))
#     subwayLineButton[i].pack(side = "left", padx = 5, pady = 13)

for i in range(8):
   subwayLineButton.append(LineNumButton(frame2, text = str(i+1)+"호선"))
   subwayLineButton[i].pack(side = "left", padx = 5, pady = 13)

lineimage = PhotoImage(file = "./image/1.png").subsample(16,16)
linephoto = Label(frame2, image = lineimage, bg = "#FFFFFF", padx = 20)

linephoto.pack(fill = "both", side = "right")

frame3 = Frame(Main, relief = "solid", bd=1)
frame3.pack(fill="both", expand = True)

frame3left = Frame(frame3, relief = "solid", bd=1)
frame3right = Frame(frame3, relief = "solid", bd=1)
frame3left.pack(fill="both", side = "left")
frame3right.pack(fill="both", side = "left", expand = True)

subwaylist = Label(frame3left, text = "호선별 역 목록", font = ("맑은 고딕", 15, "bold"), width = 40, height = 1, relief = "solid", bd=1, bg = "#64C044")
subwaytime = Label(frame3right, text = "역 열차 시간표", font = ("맑은 고딕", 15, "bold"), height = 1, relief = "solid", bd=1, bg = "#64C044")

subwaylist.pack(fill = "both")
subwaytime.pack(fill = "both")

frame3rightup = Frame(frame3right, relief = "solid", bd=1)
frame3rightdown = Frame(frame3right, relief = "solid", bd=1)
frame3rightup.pack(fill="both", side = "left")
frame3rightdown.pack(fill="both", side = "left", expand = True)

uplabel = Label(frame3rightup, text = '상행, 내선', height = 1)
downlabel = Label(frame3rightdown, text = '하행, 외선', height = 1)
uplabel.pack(fill = "both")
downlabel.pack(fill = "both")

listscroll1 = Scrollbar(frame3left)
listscroll2 = Scrollbar(frame3rightup)
listscroll3 = Scrollbar(frame3rightdown)

listscroll1.pack(fill = "y", side = "right")
listscroll2.pack(fill = "y", side = "right")
listscroll3.pack(fill = "y", side = "right")

listbox1=Listbox(frame3left, yscrollcommand = listscroll1.set, font = ('맑은 고딕', 20), height = 1)
listbox1.pack(side="left", fill = "both", expand = True)

listscroll1["command"]=listbox1.yview

def event_for_listbox(event):
   input_text.delete(0, END)
   input_text.insert(0, listbox1.get(listbox1.curselection()[0]))
   outputSchedule(listbox1.get(listbox1.curselection()[0]))

   #  print(listbox1.get(listbox1.curselection()[0]))

listbox1.bind('<<ListboxSelect>>', event_for_listbox)

listbox2=Listbox(frame3rightup, yscrollcommand = listscroll2.set, font = ('맑은 고딕', 20), width = 15, height = 1)
listbox2.pack(side="left", fill = "both", expand = True)

listscroll2["command"]=listbox2.yview

listbox3=Listbox(frame3rightdown, yscrollcommand = listscroll3.set, font = ('맑은 고딕', 20), height = 1)
listbox3.pack(side="left", fill = "both", expand = True)

listscroll3["command"]=listbox3.yview

frame4 = Frame(Main, relief = "solid", bd=1, bg = "#FFFFFF")
frame4.pack(fill="both", side = "bottom")

graphframe = Frame(frame4, relief = "solid", bd=1, width = 685, height = 135, bg = "#FFFFFF")
graphframe.pack(fill = "both", side = "left")
emailphoto = PhotoImage(file = "./image/email.png").subsample(5, 5)
mapphoto = PhotoImage(file = "./image/map.png").subsample(5, 5)
email = Button(frame4, width = 115, image = emailphoto, bg = "#FFFFFF")
kakaomap = Button(frame4, image = mapphoto, bg = "#FFFFFF")

email.pack(fill = "both", side = "left", padx = 10, pady = 10)
kakaomap.pack(fill = "both", side = "left", expand = True, padx = 10, pady = 10)

window.mainloop()

