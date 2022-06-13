import sys
import traceback
import time
import telepot
from pprint import pprint
from datetime import date, datetime

from modules.loadapi import *

#봇 id : @subway_schedule_skje_bot
TOKEN = '5491253716:AAEAFc0tygOCxJm0N86Q48m04ChyckqdThk'
bot = telepot.Bot(TOKEN)

def sendMessage(user, msg): 
    try:
        bot.sendMessage(user, msg) 
    except: 
        # 예외 정보와 스택 트레이스 항목을 인쇄. 
        traceback.print_exception(*sys.exc_info(), file=sys.stdout)

def schedule2Telebot(user, STATION_NM):

    if STATION_NM[-1] == '역':
        temp = []
        for i in range(len(STATION_NM)-1):
            temp.append(STATION_NM[i])
        STATION_NM = ''.join(temp)
    
    data = LoadSubwayTimetable2(STATION_NM)

    print(user, STATION_NM)
    

    if data == False:
        msg = STATION_NM + '역 데이터가 존재하지 않습니다.'
        sendMessage(user, msg)
        return

    for i in data:
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

    for i in data:
        msg = i['STATION_NM'] + '역 '
        msg += i['LINE_NUM'] + '\n상행\n'
        msg += str(i['Schedule']['1'])
        sendMessage(user, msg)
        msg = i['STATION_NM'] + '역 '
        msg += i['LINE_NUM'] + '\n하행\n'
        msg += str(i['Schedule']['2'])
        sendMessage(user, msg)
  

def handle(msg): 
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
        print('try to help')
        sendMessage(chat_id, '''
언제타 지하철\n
해당 봇은 원하는 역의 시간표를 현재 시간 시를 기준으로 전후 한시간의 시간표를 알려줍니다.\n
사용 방법 :\n시간표 + 역이름''')

today = date.today() 
current_month = today.strftime('%Y%m')

print( '[',today,']received token :', TOKEN )

pprint( bot.getMe() )

bot.message_loop(handle)

print('Listening...') 


while 1: 
    time.sleep(10)



