#!/usr/bin/python
# coding=utf-8

import sys
import traceback
import time
import telepot
from pprint import pprint
from urllib.request import urlopen
import re
from datetime import date, datetime

from modules.loadapi import *

TOKEN = '5540751948:AAF8i8HTZ-eiHGmoekwh_JSeB9gc0VzHyXs'
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
    
    # sendMessage(user, data)

    if data == False:
        msg = STATION_NM + '역 데이터가 존재하지 않습니다.'
        sendMessage(user, msg)
        return
    # msg = list(str(data))

    for i in data:
        temptime1 = []
        temptime2 = []
        for j in i['Schedule']['1']:
            nowh = int(datetime.now().hour)
            if int(j[0:2]) == nowh or int(j[0:2]) == nowh - 1 or int(j[0:2]) == nowh + 1:
                temptime1.append(j)
        i['Schedule']['1']=temptime1
        for j in i['Schedule']['2']:
            nowh = int(datetime.now().hour)
            if int(j[0:2]) == nowh or int(j[0:2]) == nowh - 1 or int(j[0:2]) == nowh + 1:
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

    # sendmsg = []
    # for i, x in enumerate(msg):
    #     sendmsg.append(x)
    #     if (i+1) % 300 == 0:
    #         sendMessage(user, ''.join(sendmsg))
    #         # sendmsg.append('\n')
    #         sendmsg = []

    # sendMessage(user, ''.join(sendmsg))
    #         sendmsg = []
    # sendMessage(user, ''.join(sendmsg))

    # for i in data:
    #     sendMessage( user, i )



    # msg = '' 
    # for r in data: 
    #     # print( str(datetime.now()).split('.')[0], r )
    #     if len(r+msg)+1>300: 
    #         sendMessage( user, msg ) 
    #         msg = r+'\n' 
    #     else: 
    #         msg += r+'\n'
    # if msg: 
    #     sendMessage( user, msg ) 
    # else: 
    #     sendMessage( user, ' 기간에 해당하는 데이터가 없습니다.')

# # date_param: 날짜, user: 사용자ID, loc_param:지역코드
# def replyAptData(date_param, user, loc_param='11710'): 
#     print(user, date_param, loc_param) 
#     res_list = getData( loc_param, date_param )

#     # 하나씩 보내면 메세지 개수가 너무 많아지므로
#     # 300자까지는 하나의 메세지로 묶어서 보내기. 
#     msg = '' 
#     for r in res_list: 
#         print( str(datetime.now()).split('.')[0], r )
#         if len(r+msg)+1>MAX_MSG_LENGTH: 
#             sendMessage( user, msg ) 
#             msg = r+'\n' 
#         else: 
#             msg += r+'\n'
#     if msg: 
#         sendMessage( user, msg ) 
#     else: 
#         sendMessage( user, '%s 기간에 해당하는 데이터가 없습니다.'%date_param)

# def save( user, loc_param ): 
#     conn = sqlite3.connect('users.db') 
#     cursor = conn.cursor() 
#     cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )') 
#     try: 
#         cursor.execute('INSERT INTO users(user, location) VALUES ("%s", "%s")' % (user, loc_param)) 
#     except sqlite3.IntegrityError: 
#         sendMessage( user, '이미 해당 정보가 저장되어 있습니다.' ) 
#         return
#     else: 
#         sendMessage( user, '저장되었습니다.' ) 
#         conn.commit()

# def check( user ): 
#     conn = sqlite3.connect('users.db') 
#     cursor = conn.cursor() 
#     cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, locationTEXT, PRIMARY KEY(user, location) )') 
#     cursor.execute('SELECT * from users WHERE user="%s"' % user)
#     for data in cursor.fetchall(): 
#         row = 'id:' + str(data[0]) + ', location:' + data[1] 
#         sendMessage( user, row )

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
        # replyAptData( args[1], chat_id, args[2] ) 
    # elif text.startswith('지역') and len(args)>1: 
    #     print('try to 지역', args[1]) 
    #     replyAptData( '202205', chat_id, args[1] ) 
    # elif text.startswith('저장') and len(args)>1: 
    #     print('try to 저장', args[1]) 
    #     save( chat_id, args[1] ) 
    # elif text.startswith('확인'): 
    #     print('try to 확인') 
    #     check( chat_id ) 
    else: 
        sendMessage(chat_id, '''존재하지 않는 역입니다.''')

today = date.today() 
current_month = today.strftime('%Y%m')

print( '[',today,']received token :', TOKEN )

pprint( bot.getMe() )

bot.message_loop(handle)

print('Listening...') 


while 1: 
    time.sleep(10)


