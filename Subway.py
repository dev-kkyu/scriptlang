from modules.loadapi import *
from tkinter import *
from tkinter import messagebox


class mainWindow:
   def __init__(self):
      self.window = Tk()  # Gui 생성
      self.window.title("Subway")  # 창이름설정
      self.window.geometry("990x630+100+100")  # 창사이즈설정
      self.window.resizable(False, True)  # 사이즈 변경 허용

      self.Line = 1

      frameside = Frame(self.window, relief="flat", bd=6, bg="#00B050") # 테두리 전용 프레임
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

      self.input_text = Entry(textframe, textvariable = textEntry, width=30, font = ("맑은 고딕",15), fg = 'grey')
      self.input_text.pack(fill = "both", side = "left")

      self.input_text.bind('<Button-1>', self.event_for_entry)


      button = Button(textframe, text="검색", command = self.commandoutputSchedule, font = ("맑은 고딕",15), height= 1, width = 7, bg = "#92D050", padx = 10)
      button.pack( side = "left")

      frame2 = Frame(Main, bg = "#FFFFFF")
      frame2.pack(fill="both", padx = 20)

      subwayLineButton = []
      
      for i in range(9):
         subwayLineButton.append(Button(frame2, text = (str(i+1)+"호선"), command = lambda row=i+1:self.onClick(row), font = ("맑은 고딕", 15, "bold"), width = 6, height = 1, fg = "white", bg = "#92D050"))
         subwayLineButton[i].pack(side = "left", padx = 5, pady = 13)

      self.lineimage = PhotoImage(file = "./image/1.png").subsample(16,16)
      self.linephoto = Label(frame2, image = self.lineimage, bg = "#FFFFFF", padx = 20)

      self.linephoto.pack(fill = "both", side = "right")

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

      self.subwaylist = Label(frame3left, text = "호선별 역 목록", font = ("맑은 고딕", 15, "bold"), width = 38, height = 1, bd=0, bg = "#64C044")
      self.subwaytime = Label(frame3right, text = "역 열차 시간표", font = ("맑은 고딕", 15, "bold"), height = 1, bd=0, bg = "#64C044")

      self.subwaylist.pack(fill = "both")
      self.subwaytime.pack(fill = "both")

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

      self.listbox1=Listbox(frame3leftin, yscrollcommand = listscroll1.set, font = ('맑은 고딕', 20), height = 1)
      self.listbox1.pack(side="left", fill = "both", expand = True)

      listscroll1["command"]=self.listbox1.yview

      self.listbox1.bind('<<ListboxSelect>>', self.event_for_listbox)

      self.listbox2=Listbox(frame3rightup, yscrollcommand = listscroll2.set, font = ('맑은 고딕', 20), width = 15, height = 1)
      self.listbox2.pack(side="left", fill = "both", expand = True)

      listscroll2["command"]=self.listbox2.yview

      self.listbox3=Listbox(frame3rightdown, yscrollcommand = listscroll3.set, font = ('맑은 고딕', 20), width = 1, height = 1)
      self.listbox3.pack(side="left", fill = "both", expand = True)

      listscroll3["command"]=self.listbox3.yview

      frame4 = Frame(Main, bd=0, bg = "#FFFFFF")
      frame4.pack(fill="both", side = "bottom")

      emptyframe4 = Frame(frame4, bd=0, width = 415, height = 135, bg = "#FFFFFF")
      emptyframe4.pack(fill = "both", side = "left")

      
      loadphoto = PhotoImage(file = "./image/restore.png").subsample(5, 5)
      graphphoto = PhotoImage(file = "./image/graph.png").subsample(5, 5)
      emailphoto = PhotoImage(file = "./image/email.png").subsample(5, 5)
      mapphoto = PhotoImage(file = "./image/map.png").subsample(5, 5)

      loadb = Button(frame4, command = self.loadfile, width = 115, image = loadphoto, bg = "#FFFFFF")
      graph = Button(frame4, command = self.showGraph, width = 115, image = graphphoto, bg = "#FFFFFF")
      email = Button(frame4, command = self.MakeWindow, width = 115, image = emailphoto, bg = "#FFFFFF")
      kakaomap = Button(frame4, command = self.showMap, image = mapphoto, bg = "#FFFFFF")

      loadb.pack(fill = "both", side = "left", padx = 10, pady = 10)
      graph.pack(fill = "both", side = "left", padx = 10, pady = 10)
      email.pack(fill = "both", side = "left", padx = 10, pady = 10)
      kakaomap.pack(fill = "both", side = "left", expand = True, padx = 10, pady = 10)

      self.window.mainloop()

   
   def savefile(self, STATION_NM):
      write = open("data.txt", 'w')
      data = str(self.Line) + ' ' + STATION_NM
      write.write(data)
      write.close()

   def loadfile(self):
      try:
         read = open("data.txt", 'r')
      except:
         messagebox.showinfo('알림', '저장된 데이터가 없습니다.')
         return
      line = read.readline()
      data = line.split(' ')
      self.onClick(int(data[0]))
      self.outputSchedule(data[1])
      read.close()

   def showGraph(self):
      from modules.graph import drawGraph
      drawGraph(str(self.Line) + '호선', self.input_text.get())

   def MakeWindow(self):
      self.subWindow()

   def showMap(self):
      from modules.map_show import mapview
      mapview(self.input_text.get() + '역')

   def commandoutputSchedule(self):
      self.outputSchedule(self.input_text.get())

   def outputSchedule(self, STATION_NM):
      if STATION_NM == '':
         return
      data = LoadSubwayTimetable(STATION_NM, self.Line, 0)

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
         print("알림메시지")
         return

      self.listbox2.delete(0, END)
      self.listbox3.delete(0, END)
      for i, x in enumerate(data['data']['Schedule']['1']):
         self.listbox2.insert(i, x)
      for i, x in enumerate(data['data']['Schedule']['2']):
         self.listbox3.insert(i, x)

      self.subwaytime.config(text = data['data']['STATION_NM']+"역 열차 시간표")
      self.savefile(STATION_NM)

   def event_for_entry(self, event):
      self.input_text.delete(0, END)
      self.input_text.config(fg = 'black')

   def event_for_listbox(self, event):
      try:
         print(self.listbox1.get(self.listbox1.curselection()[0]))
         self.input_text.delete(0, END)
         self.input_text.insert(0, self.listbox1.get(self.listbox1.curselection()[0]))
         self.outputSchedule(self.listbox1.get(self.listbox1.curselection()[0]))
      except:
         pass

    
   def onClick(self, linenum):
     
      self.linenum = linenum
      self.Line = self.linenum

      data = LoadSubwaystationtable(str(self.linenum))
      self.listbox1.delete(0, END)
      self.listbox2.delete(0, END)
      self.listbox3.delete(0, END)
      self.subwaytime.config(text = "역 열차 시간표")
      
      for i, x in enumerate(data):
         self.listbox1.insert(i, x)

      self.subwaylist.config(text = str(self.linenum) + "호선 역 목록")

      self.lineimage = PhotoImage(file = "./image/"+str(self.linenum)+".png").subsample(16, 16)
      self.linephoto.config(image = self.lineimage)


   def subWindow(self):
      newWindow = Toplevel(self.window, bd = 6, bg = "#00B050")
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

      sendframe = Frame(bottomframe, bg = "#FFFFFF", bd = 0)
      sendframe.pack(fill = "both")

      sendbutton = Button(sendframe, text = "보내기", command = self.sendEmail, font = ("맑은 고딕",12, 'bold'), bg = "#92D050", height=1)
      sendbutton.pack(fill = 'both', expand=True)

      self.SendList = []
   
   def addEmail(self):
      self.listbx.insert(0, self.addemailx.get())
      self.SendList.append(self.listbx.get(0))

   def sendEmail(self):
      from modules.email_send import sendMail

      for i in self.SendList:
         sendMail('jjaeunjj@gmail.com', i, LoadSubwayTimetable(self.input_text.get(), self.Line, 1))
      
if __name__ == '__main__':
   mainWindow()

