from cmath import exp
from tkinter import messagebox
from loadapi import *
from tkinter import *

window = Tk()  # Gui 생성
window.title("Subway")  # 창이름설정
window.geometry("990x630+100+100")  # 창사이즈설정
window.resizable(False, True)  # 사이즈 변경 허용

Line = 1

class LineNumButton(Button):
   def __init__(self, container, text):
      Button.__init__(self, container, text = text, command = self.onClick, font = ("맑은 고딕", 15, "bold"), width = 6, height = 1, fg = "white", bg = "#92D050")
      self.linenum = text[0]
   
   def onClick(self):
      global lineimage
      global Line
      Line = self.linenum

      data = LoadSubwaystationtable(self.linenum)
      listbox1.delete(0, END)
      listbox2.delete(0, END)
      listbox3.delete(0, END)
      subwaytime.config(text = "역 열차 시간표")
      
      for i, x in enumerate(data):
         listbox1.insert(i, x)

      subwaylist.config(text = self.linenum + "호선 역 목록")

      lineimage = PhotoImage(file = "./image/"+self.linenum+".png").subsample(16, 16)
      linephoto.config(image = lineimage)



def commandoutputSchedule():
   outputSchedule(input_text.get())

def outputSchedule(STATION_NM):
   if STATION_NM == '':
      return
   data = LoadSubwayTimetable(STATION_NM, Line, 0)
   
   msg = "해당 데이터가 없습니다."

   if(data['info'] == False):
      if('data' in data):
         if data['data'] != False:
            temp = []
            for i in data['data']:
               if i['STATION_NM'] == STATION_NM:
                  temp.append(i['LINE_NUM'])
            if temp != []:
               msg += '\n'
               msg += ', '.join(temp)
               msg += "에 " + STATION_NM + " 역이 존재합니다."

      messagebox.showinfo("알림", msg)
      print("a")
      return

   listbox2.delete(0, END)
   listbox3.delete(0, END)
   for i, x in enumerate(data['data']['Schedule']['1']):
      listbox2.insert(i, x)
   for i, x in enumerate(data['data']['Schedule']['2']):
      listbox3.insert(i, x)
   
   subwaytime.config(text = data['data']['STATION_NM']+"역 열차 시간표")

class subWindow:
   def __init__(self):
      newWindow = Toplevel(window, bd = 6, bg = "#00B050")
      newWindow.title("Email")  # 창이름설정
      newWindow.geometry("450x500+200+200")  # 창사이즈설정
      newWindow.resizable(False, False)  # 사이즈 변경 허용

      midframe = Frame(newWindow, bg = "#FFFFFF", bd = 3)
      midframe.pack(fill = "both", expand = True)

      newframe = Frame(midframe, bg = "#64C044")
      newframe.pack(fill = "both", expand = True)

      newTitle = Label(newframe, text="E-Mail 보내기", font = ("맑은 고딕",15, "bold"), bg = "#64C044", height=1)
      newTitle.pack(fill = "both")

      addframe = Frame(newframe, bg = "#64C044", bd = 3)
      addframe.pack(fill = "both")

      self.addemailx = Entry(addframe, font = ("맑은 고딕",12))
      self.addemailx.pack(fill = "both", side = "left", expand = True)

      addbutton = Button(addframe, text = "추가", command = self.addEmail, font = ("맑은 고딕",12, 'bold'), bg = "#92D050", width=7, height=1)
      addbutton.pack(fill = "both", side = "left")

      bottomframe = Frame(newframe, bg = "#64C044", bd = 3)
      bottomframe.pack(fill = "both", expand=True)

      listframe = Frame(bottomframe)
      listframe.pack(fill = "both", expand=True)

      listscrol = Scrollbar(listframe)
      listscrol.pack(fill = "y", side = "right")
      self.listbx=Listbox(listframe, yscrollcommand = listscrol.set, font = ('맑은 고딕', 20), height = 1, bd = 0)
      self.listbx.pack(side="left", fill = "both", expand = True)

      listscrol["command"]=self.listbx.yview

      # for i in range(20):
      #    self.listbx.insert(i, i)

      sendframe = Frame(bottomframe, bg = "#FFFFFF", bd = 0)
      sendframe.pack(fill = "both")

      sendbutton = Button(sendframe, text = "보내기", command = self.sendEmail, font = ("맑은 고딕",12, 'bold'), bg = "#92D050", height=1)
      sendbutton.pack(fill = 'both', expand=True)

      self.SendList = []
   
   def addEmail(self):
      self.listbx.insert(0, self.addemailx.get())
      self.SendList.append(self.listbx.get(0))

   def sendEmail(self):
      from email_send import sendMail

      for i in self.SendList:
         sendMail('jjaeunjj@gmail.com', i, LoadSubwayTimetable(input_text.get(), Line, 1))
      # sendMail('jjaeunjj@gmail.com', "jaeun224@naver.com", 4114)

def MakeWindow():
   makewindow = subWindow()

frameside = Frame(window, relief="flat", bd=6, bg="#00B050") # 테두리 전용 프레임
Main = Frame(frameside, bd=0, bg = "#FFFFFF") # 메인창

frameside.pack(fill = "both", expand=True) 
Main.pack(fill = "both", expand=True)

emptyframe0 = Label(Main, bd=0, height = 0, bg = "#FFFFFF")
emptyframe0.pack(fill = "both")

frame1 = Frame(Main, bd=0)
frame1.pack(fill="both")

frame1left = Frame(frame1, bd=0)
frame1left.pack(fill="both", side="left")

frame1right = Frame(frame1, bd=0, bg = "#FFFFFF")
frame1right.pack(fill="both", expand = True, side="left")

Title = Label(frame1left, text="언제타 지하철", font = ("맑은 고딕",44, "bold"), bg = "#FFFFFF", height=1, width=13)
Title.pack(fill = "both")

textframe = Frame(frame1right, relief = "flat", bd=3, bg = "#64C044")
textframe.pack(side = "left", padx = 20)

textEntry = StringVar()
textEntry.set("호선 선택 후 입력해 주세요")

input_text = Entry(textframe, textvariable = textEntry, width=30, font = ("맑은 고딕",15), fg = 'grey')
input_text.pack(fill = "both", side = "left")

def event_for_entry(event):
   input_text.delete(0, END)
   input_text.config(fg = 'black')
input_text.bind('<Button-1>', event_for_entry)

button = Button(textframe, text="검색", command = commandoutputSchedule, font = ("맑은 고딕",15), height= 1, width = 7, bg = "#92D050", padx = 10)
button.pack( side = "left")

frame2 = Frame(Main, bg = "#FFFFFF")
frame2.pack(fill="both", padx = 20)

subwayLineButton = []
# for i in range(8):
#     subwayLineButton.append(Button(frame2, text=str(i+1)+"호선", font = ("맑은 고딕", 15, "bold"), width = 7, height = 1, fg = "white", bg = "#92D050"))
#     subwayLineButton[i].pack(side = "left", padx = 5, pady = 13)

for i in range(9):
   subwayLineButton.append(LineNumButton(frame2, text = str(i+1)+"호선"))
   subwayLineButton[i].pack(side = "left", padx = 5, pady = 13)

lineimage = PhotoImage(file = "./image/1.png").subsample(16,16)
linephoto = Label(frame2, image = lineimage, bg = "#FFFFFF", padx = 20)

linephoto.pack(fill = "both", side = "right")

frame3 = Frame(Main)
frame3.pack(fill="both", expand = True)

frame3label = Label(frame3, width = 0, bg = "#FFFFFF")
frame3label.pack(fill = "both", side = "left")

frame3leftout = Frame(frame3, bd=3, bg = "#FFFFFF")
frame3rightout = Frame(frame3, bd=3, bg = "#FFFFFF")
frame3leftout.pack(fill="both", side = "left")
frame3rightout.pack(fill="both", side = "left", expand = True)

frame3label2 = Label(frame3, width = 0, bg = "#FFFFFF")
frame3label2.pack(fill = "both", side = "right")

frame3left = Frame(frame3leftout, bd=3, bg = "#64C044")
frame3right = Frame(frame3rightout, bd=3, bg = "#64C044")
frame3left.pack(fill="both", expand = True)
frame3right.pack(fill="both", expand = True)

subwaylist = Label(frame3left, text = "호선별 역 목록", font = ("맑은 고딕", 15, "bold"), width = 38, height = 1, bd=0, bg = "#64C044")
subwaytime = Label(frame3right, text = "역 열차 시간표", font = ("맑은 고딕", 15, "bold"), height = 1, bd=0, bg = "#64C044")

subwaylist.pack(fill = "both")
subwaytime.pack(fill = "both")

frame3rightup = Frame(frame3right, bd=0)
frame3rightdown = Frame(frame3right, bd=0)
frame3rightup.pack(fill="both", side = "left")
frame3rightdown.pack(fill="both", side = "left", expand = True)

uplabel = Label(frame3rightup, text = '상행, 내선', height = 1)
downlabel = Label(frame3rightdown, text = '하행, 외선', height = 1)
uplabel.pack(fill = "both")
downlabel.pack(fill = "both")

frame3leftin = Frame(frame3left, bd=0)
frame3leftin.pack(fill = "both", expand=True)

listscroll1 = Scrollbar(frame3leftin)
listscroll2 = Scrollbar(frame3rightup)
listscroll3 = Scrollbar(frame3rightdown)

listscroll1.pack(fill = "y", side = "right")
listscroll2.pack(fill = "y", side = "right")
listscroll3.pack(fill = "y", side = "right")

listbox1=Listbox(frame3leftin, yscrollcommand = listscroll1.set, font = ('맑은 고딕', 20), height = 1)
listbox1.pack(side="left", fill = "both", expand = True)

listscroll1["command"]=listbox1.yview



def event_for_listbox(event):
   try:
      print(listbox1.get(listbox1.curselection()[0]))
      input_text.delete(0, END)
      input_text.insert(0, listbox1.get(listbox1.curselection()[0]))
      outputSchedule(listbox1.get(listbox1.curselection()[0]))
   except:
      pass

   #  print(listbox1.get(listbox1.curselection()[0]))

listbox1.bind('<<ListboxSelect>>', event_for_listbox)

listbox2=Listbox(frame3rightup, yscrollcommand = listscroll2.set, font = ('맑은 고딕', 20), width = 15, height = 1)
listbox2.pack(side="left", fill = "both", expand = True)

listscroll2["command"]=listbox2.yview

listbox3=Listbox(frame3rightdown, yscrollcommand = listscroll3.set, font = ('맑은 고딕', 20), width = 1, height = 1)
listbox3.pack(side="left", fill = "both", expand = True)

listscroll3["command"]=listbox3.yview

frame4 = Frame(Main, bd=0, bg = "#FFFFFF")
frame4.pack(fill="both", side = "bottom")

graphframe = Frame(frame4, bd=0, width = 696, height = 135, bg = "#FFFFFF")
graphframe.pack(fill = "both", side = "left")
emailphoto = PhotoImage(file = "./image/email.png").subsample(5, 5)
mapphoto = PhotoImage(file = "./image/map.png").subsample(5, 5)
email = Button(frame4, command = MakeWindow, width = 115, image = emailphoto, bg = "#FFFFFF")
kakaomap = Button(frame4, image = mapphoto, bg = "#FFFFFF")

email.pack(fill = "both", side = "left", padx = 10, pady = 10)
kakaomap.pack(fill = "both", side = "left", expand = True, padx = 10, pady = 10)

window.mainloop()

