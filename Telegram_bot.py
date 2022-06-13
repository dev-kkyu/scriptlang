import sys
import traceback
import time
import telepot
from pprint import pprint
from datetime import date, datetime

from modules.loadapi import *

#봇 id : @subway_schedule_skje_bot
TOKEN = '5491253716:AAEAFc0tygOCxJm0N86Q48m04ChyckqdThk'    #봇 토큰
bot = telepot.Bot(TOKEN)                                    #토큰에 접속

def sendMessage(user, msg): 
    try:
        bot.sendMessage(user, msg) 
    except: 
        # 예외 정보와 스택 트레이스 항목을 인쇄. 
        traceback.print_exception(*sys.exc_info(), file=sys.stdout)

def schedule2Telebot(user, STATION_NM):

    if STATION_NM[-1] == '역':              #*역으로 검색해도 나오도록 처리
        temp = []
        for i in range(len(STATION_NM)-1):
            temp.append(STATION_NM[i])
        STATION_NM = ''.join(temp)
    
    data = LoadSubwayTimetable2(STATION_NM)     #데이터 받아오기

    print(user, STATION_NM)
    

    if data == False:           #검색한 역으로 조회가 안되면 오류메시지 보내기
        msg = STATION_NM + '역 데이터가 존재하지 않습니다.'
        sendMessage(user, msg)
        return

    for i in data:              #현재시간 시 기준으로 전후 한시간만 필터링
        temptime1 = []
        temptime2 = []
        for j in i['Schedule']['1']:
            nowh = int(datetime.now().hour)
            if int(j[0:2]) in (nowh - 1, nowh, nowh + 1):
                temptime1.append(j)
        i['Schedule']['1']=temptime1
        for j in i['Schedule']['2']:
            nowh = int(datetime.now().hour)
            if int(j[0:2]) in (nowh - 1, nowh, nowh + 1):
                temptime2.append(j)
        i['Schedule']['2']=temptime2

    for i in data:              #보낼 메세지 상행, 하행 구분해서 따로 보내기
        msg = i['STATION_NM'] + '역 '
        msg += i['LINE_NUM'] + '\n상행\n'
        msg += str(i['Schedule']['1'])
        sendMessage(user, msg)
        msg = i['STATION_NM'] + '역 '
        msg += i['LINE_NUM'] + '\n하행\n'
        msg += str(i['Schedule']['2'])
        sendMessage(user, msg)
  

def handle(msg):                #사용자가 입력하면 반환할 메세지 정의
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text': 
        sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.') 
        return
    text = msg['text'] 
    args = text.split(' ')
    if text.startswith('시간표') and len(args)>1: 
        print('try to 시간표', args[1]) 
        schedule2Telebot(chat_id, args[1])
    else: 
        print('try to help')    #정해진 규칙 이외로 질문이 들어오면 도움말 출력
        sendMessage(chat_id, '''
언제타 지하철\n
해당 봇은 원하는 역의 시간표를 현재 시간 시를 기준으로 전후 한시간의 시간표를 알려줍니다.\n
사용 방법 :\n시간표 + 역이름''')

today = date.today()            #오늘 날짜 받아서 출력하기 위해
current_month = today.strftime('%Y%m')

print( '[',today,']received token :', TOKEN )

pprint( bot.getMe() )

bot.message_loop(handle)

print('Listening...') 


while 1: 
    time.sleep(10)



