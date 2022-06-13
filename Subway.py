from modules.loadapi import *
from tkinter import *
from tkinter import messagebox


class mainWindow:
   def __init__(self):
      self.window = Tk()  # Gui 생성
      self.window.title("Subway")  # 창이름설정
      self.window.geometry("990x630+100+100")  # 창사이즈설정
      self.window.resizable(False, True)  # 사이즈 변경 허용

      self.Line = 1  #현재 출력되고 있는 호선 번호

      frameside = Frame(self.window, relief="flat", bd=6, bg="#00B050") # 테두리 전용 프레임
      Main = Frame(frameside, bd=0, bg = "#FFFFFF") # 메인창

      frameside.pack(fill = "both", expand=True) 
      Main.pack(fill = "both", expand=True)

      emptyframe0 = Label(Main, bd=0, height = 0, bg = "#FFFFFF") #위쪽 여백 둠
      emptyframe0.pack(fill = "both")

      frame1 = Frame(Main, bd=0) #제목과 검색창이 위치한 프레임
      frame1.pack(fill="both")

      frame1left = Frame(frame1, bd=0) #제목용 프레임
      frame1left.pack(fill="both", side="left")

      frame1right = Frame(frame1, bd=0, bg = "#FFFFFF")  #검색창용 프레임
      frame1right.pack(fill="both", expand = True, side="left")

      Title = Label(frame1left, text="언제타 지하철", font = ("맑은 고딕",44, "bold"), bg = "#FFFFFF", height=1, width=13) #프로그램 이름 표시
      Title.pack(fill = "both")

      textframe = Frame(frame1right, relief = "flat", bd=3, bg = "#64C044")   #검색창을 위한 작은 프레임
      textframe.pack(side = "left", padx = 20)

      textEntry = StringVar() # 검색창 안에 미리 채워넣기
      textEntry.set("호선 선택 후 입력해 주세요")

      self.input_text = Entry(textframe, textvariable = textEntry, width=30, font = ("맑은 고딕",15), fg = 'grey')
      self.input_text.pack(fill = "both", side = "left")

      self.input_text.bind('<Button-1>', self.event_for_entry) #검색창 안 클릭하면 자동으로 텍스트 지워주기


      button = Button(textframe, text="검색", command = self.commandoutputSchedule, font = ("맑은 고딕",15), height= 1, width = 7, bg = "#92D050", padx = 10)
      button.pack( side = "left")   #검색버튼 생성

      frame2 = Frame(Main, bg = "#FFFFFF")   #1~9호선 버튼이랑 이미지 들어가는 프레임
      frame2.pack(fill="both", padx = 20)

      subwayLineButton = []
      
      for i in range(9):   #1~9호선 버튼 생성
         subwayLineButton.append(Button(frame2, text = (str(i+1)+"호선"), command = lambda row=i+1:self.onClick(row), font = ("맑은 고딕", 15, "bold"), width = 6, height = 1, fg = "white", bg = "#92D050"))
         subwayLineButton[i].pack(side = "left", padx = 5, pady = 13)

      self.lineimage = PhotoImage(file = "./image/1.png").subsample(16,16) #이미지 생성. 기본값 1호선
      self.linephoto = Label(frame2, image = self.lineimage, bg = "#FFFFFF", padx = 20)

      self.linephoto.pack(fill = "both", side = "right")

      frame3 = Frame(Main) #리스트박스 3개 들어가는 프레임(역목록, 상행, 하행 시간표)
      frame3.pack(fill="both", expand = True)

      frame3label = Label(frame3, width = 0, bg = "#FFFFFF")   #왼쪽 여백 준다.
      frame3label.pack(fill = "both", side = "left")

      frame3leftout = Frame(frame3, bd=3, bg = "#FFFFFF")   #테두리 만들기 위하여 왼쪽 오른쪽 바깥프레임 만들어줌
      frame3rightout = Frame(frame3, bd=3, bg = "#FFFFFF")
      frame3leftout.pack(fill="both", side = "left")
      frame3rightout.pack(fill="both", side = "left", expand = True)

      frame3label2 = Label(frame3, width = 0, bg = "#FFFFFF")  #오른쪽 여백 준다.
      frame3label2.pack(fill = "both", side = "right")

      frame3left = Frame(frame3leftout, bd=3, bg = "#64C044")  #역목록 리스트박스 프레임
      frame3right = Frame(frame3rightout, bd=3, bg = "#64C044")   #상행 하행 시간표 리스트박스 프레임
      frame3left.pack(fill="both", expand = True)
      frame3right.pack(fill="both", expand = True)

      self.subwaylist = Label(frame3left, text = "호선별 역 목록", font = ("맑은 고딕", 15, "bold"), width = 38, height = 1, bd=0, bg = "#64C044") #역목록 제목
      self.subwaytime = Label(frame3right, text = "역 열차 시간표", font = ("맑은 고딕", 15, "bold"), height = 1, bd=0, bg = "#64C044")   #역 시간표 제목

      self.subwaylist.pack(fill = "both")
      self.subwaytime.pack(fill = "both")

      frame3rightup = Frame(frame3right, bd=0)  #상행 표시하는 프레임
      frame3rightdown = Frame(frame3right, bd=0)   #하행 표시하는 프레임
      frame3rightup.pack(fill="both", side = "left")
      frame3rightdown.pack(fill="both", side = "left", expand = True)

      uplabel = Label(frame3rightup, text = '상행, 내선', height = 1)   #상행 적고
      downlabel = Label(frame3rightdown, text = '하행, 외선', height = 1)  #하행 적는다.
      uplabel.pack(fill = "both")
      downlabel.pack(fill = "both")

      frame3leftin = Frame(frame3left, bd=0) #역목록 리스트박스 출력하는 프레임
      frame3leftin.pack(fill = "both", expand=True)

      listscroll1 = Scrollbar(frame3leftin)  #역목록, 상행, 하행 리스트박스에 연결할 스크롤바
      listscroll2 = Scrollbar(frame3rightup)
      listscroll3 = Scrollbar(frame3rightdown)

      listscroll1.pack(fill = "y", side = "right")
      listscroll2.pack(fill = "y", side = "right")
      listscroll3.pack(fill = "y", side = "right")

      self.listbox1=Listbox(frame3leftin, yscrollcommand = listscroll1.set, font = ('맑은 고딕', 20), height = 1) #리스트박스 생성
      self.listbox1.pack(side="left", fill = "both", expand = True)

      listscroll1["command"]=self.listbox1.yview   #리스트박스에 스크롤 연결

      self.listbox1.bind('<<ListboxSelect>>', self.event_for_listbox)   #역목록 리스트박스 항목 클릭하면 우측에 시간표 출력

      self.listbox2=Listbox(frame3rightup, yscrollcommand = listscroll2.set, font = ('맑은 고딕', 20), width = 15, height = 1)   #상행 리스트박스 생성
      self.listbox2.pack(side="left", fill = "both", expand = True)

      listscroll2["command"]=self.listbox2.yview   #상행 리스트박스에 스크롤 연결

      self.listbox3=Listbox(frame3rightdown, yscrollcommand = listscroll3.set, font = ('맑은 고딕', 20), width = 1, height = 1)  #하행 리스트박스 생성
      self.listbox3.pack(side="left", fill = "both", expand = True)

      listscroll3["command"]=self.listbox3.yview   #하행 리스트박스에 스크롤 연결

      frame4 = Frame(Main, bd=0, bg = "#FFFFFF")   #불러오기, 그래프, 이메일, 지도 버튼 들어갈 프레임
      frame4.pack(fill="both", side = "bottom")

      emptyframe4 = Frame(frame4, bd=0, width = 415, height = 135, bg = "#FFFFFF")  #좌측 빈칸 채워줄 프레임
      emptyframe4.pack(fill = "both", side = "left")

      
      loadphoto = PhotoImage(file = "./image/restore.png").subsample(5, 5) #이미지 4개 셋팅
      graphphoto = PhotoImage(file = "./image/graph.png").subsample(5, 5)
      emailphoto = PhotoImage(file = "./image/email.png").subsample(5, 5)
      mapphoto = PhotoImage(file = "./image/map.png").subsample(5, 5)

      loadb = Button(frame4, command = self.loadfile, width = 115, image = loadphoto, bg = "#FFFFFF")    #불러오기버튼
      graph = Button(frame4, command = self.showGraph, width = 115, image = graphphoto, bg = "#FFFFFF")  #그래프버튼
      email = Button(frame4, command = self.MakeWindow, width = 115, image = emailphoto, bg = "#FFFFFF") #이메일버튼
      kakaomap = Button(frame4, command = self.showMap, image = mapphoto, bg = "#FFFFFF")                #지도버튼

      loadb.pack(fill = "both", side = "left", padx = 10, pady = 10)
      graph.pack(fill = "both", side = "left", padx = 10, pady = 10)
      email.pack(fill = "both", side = "left", padx = 10, pady = 10)
      kakaomap.pack(fill = "both", side = "left", expand = True, padx = 10, pady = 10)

      self.window.mainloop()

   
   def savefile(self, STATION_NM):  #시간표 출력할 때마다 선택한 값들 파일로 저장
      write = open("data.txt", 'w')
      data = str(self.Line) + ' ' + STATION_NM
      write.write(data)
      write.close()

   def loadfile(self):  #불러오기 버튼 클릭하면 파일 불러와서 불러오는 함수
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

   def showGraph(self):    #그래프 표시
      from modules.graph import drawGraph
      drawGraph(str(self.Line) + '호선', self.input_text.get())

   def MakeWindow(self):   #이메일 전송창 표시
      self.subWindow()

   def showMap(self):      #지도 창 표시
      from modules.map_show import mapview
      mapview(self.input_text.get() + '역')

   def commandoutputSchedule(self):    #검색버튼 클릭하면 실행
      self.outputSchedule(self.input_text.get())

   def outputSchedule(self, STATION_NM):  #해당 호선, 역의 시간표를 우측에 표시하는 함수
      if STATION_NM == '':          #들어온 데이터가 없으면 실행안함
         return
      data = LoadSubwayTimetable(STATION_NM, self.Line, 0)     #지하철 시간표 데이터 받아옴

      msg = "해당 데이터가 없습니다."  #미리 셋팅

      if(data['info'] == False): #데이터 정보가 거짓이면
         if('data' in data):     #데이터에 데이터가 들어있을 때
            if data['data'] != False:  #데이터의 데이터가 거짓이면
               temp = []
               for i in data['data']:
                  if i['STATION_NM'] == STATION_NM:   #다른 호선에 존재하는지 검색 후
                     temp.append(i['LINE_NUM'])       #존재하면 추가
               if temp != []:                         #추가가 됐으면 존재한다고 문장 추가
                  msg += '\n'
                  msg += ', '.join(temp)
                  msg += "에 " + STATION_NM + " 역이 존재합니다."

         messagebox.showinfo("알림", msg)             #메세지박스 출력
         print("알림메시지")
         return

      self.listbox2.delete(0, END)     #기존에 있던 시간표 삭제
      self.listbox3.delete(0, END)
      for i, x in enumerate(data['data']['Schedule']['1']):    #시간표 넣어주기
         self.listbox2.insert(i, x)
      for i, x in enumerate(data['data']['Schedule']['2']):
         self.listbox3.insert(i, x)

      self.subwaytime.config(text = data['data']['STATION_NM']+"역 열차 시간표")    #제목 변경
      self.savefile(STATION_NM)

   def event_for_entry(self, event):      #검색칸 누르면 글자 삭제하고 색 블랙으로 변경
      self.input_text.delete(0, END)
      self.input_text.config(fg = 'black')

   def event_for_listbox(self, event):    #역목록 리스트박스 선택시 수행할 이벤트
      try:
         print(self.listbox1.get(self.listbox1.curselection()[0]))
         self.input_text.delete(0, END)
         self.input_text.insert(0, self.listbox1.get(self.listbox1.curselection()[0]))
         self.outputSchedule(self.listbox1.get(self.listbox1.curselection()[0]))
      except:
         pass

    
   def onClick(self, linenum):      #버튼 클릭시 수행할 함수
     
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


   def subWindow(self):          #이메일버튼 클릭시 띄우는 새창
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
      addbutton.pack(fill = "both", side = "left") #보낼 이메일주소 추가버튼

      bottomframe = Frame(newframe, bg = "#64C044", bd = 3)
      bottomframe.pack(fill = "both", expand=True)

      listframe = Frame(bottomframe)
      listframe.pack(fill = "both", expand=True)

      listscrol = Scrollbar(listframe)       #리스트박스 스크롤
      listscrol.pack(fill = "y", side = "right")
      self.listbx=Listbox(listframe, yscrollcommand = listscrol.set, font = ('맑은 고딕', 20), height = 1, bd = 0)
      self.listbx.pack(side="left", fill = "both", expand = True)    #리스트박스 생성

      listscrol["command"]=self.listbx.yview    #리스트박스 스크롤 연결

      sendframe = Frame(bottomframe, bg = "#FFFFFF", bd = 0)
      sendframe.pack(fill = "both")

      sendbutton = Button(sendframe, text = "보내기", command = self.sendEmail, font = ("맑은 고딕",12, 'bold'), bg = "#92D050", height=1)
      sendbutton.pack(fill = 'both', expand=True)

      self.SendList = []
   
   def addEmail(self):     #이메일추가버튼
      self.listbx.insert(0, self.addemailx.get())     #리스트박스에 추가
      self.SendList.append(self.listbx.get(0))        #데이터 추가

   def sendEmail(self):
      from modules.email_send import sendMail

      for i in self.SendList:
         sendMail('jjaeunjj@gmail.com', i, LoadSubwayTimetable(self.input_text.get(), self.Line, 1))
      
if __name__ == '__main__':
   mainWindow()   #프로그램 실행시 객체 생성

