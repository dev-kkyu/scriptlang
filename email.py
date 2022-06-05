from loadapi import Code2Timetable
from email.mime.text import MIMEText # MIMEtexe 생성에 사용


def sendMail(fromAddr, toAddr, code):
    import smtplib # 파이썬의 SMTP 모듈# 메일 서버와 connect하고 통신 시작
    maildata = Code2Timetable(code)

    msg = MIMEText('상행, 내선 \n'+str(maildata['Schedule']['1'])+'\n하행, 외선\n'+ str(maildata['Schedule']['2'])) 
    msg['Subject'] = maildata['STATION_NM']+'역 시간표' 

    msg['From'] = fromAddr 
    msg['To'] = toAddr

    s = smtplib.SMTP("smtp.gmail.com", 587) # SMTP 서버와 연결
    s.starttls() # SMTP 연결을 TLS (Transport Layer Security) 모드로전환
   
    s.login('jjaeunjj@gmail.com ', 'zkedcjmpqmhmiuav')  # 앱 password 이용
    s.sendmail(fromAddr , toAddr, msg.as_string()) 
    s.close() 
    
    
#sendMail('jjaeunjj@gmail.com', "jaeun224@naver.com", 4114)
