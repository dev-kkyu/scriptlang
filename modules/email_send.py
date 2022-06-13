from modules.loadapi import Code2Timetable
from email.mime.text import MIMEText # MIMEtexe 생성에 사용


def sendMail(fromAddr, toAddr, code):  #이메일 보냐는 함수
    import smtplib # 파이썬의 SMTP 모듈 # 메일 서버와 connect하고 통신 시작
    maildata = Code2Timetable(code)  #메일로 보낼 내용을 maildata에 저장

    datainfo = maildata['LINE_NUM'] + ' ' + maildata['STATION_NM'] + '역 검색 결과'   #메일 제목
    schedule1 = ''
    schedule2 = ''
    for i in maildata['Schedule']['1']:  #상행 데이터 저장
        schedule1 += (i + '\n') 
    
    for i in maildata['Schedule']['2']:  #하행 데이터 저장
        schedule2 += (i + '\n') 

  #html로 변환
    html = '''
<!DOCTYPE html>
<html>
    <head>
        <title>
            지하철 시간표
        </title>
    </head>
    <body>
        <h1>
            언제타 지하철
        </h1>
        <h2>
''' + datainfo + '''
        </h2>
        <h3>
            상행
        </h3>
        <h4>
''' + schedule1 + '''
        </h4>
        <h3>
            하행
        </h3>
        <h4>
''' + schedule2 + '''
        </h4>
    </body>
</html>
'''
    msg = MIMEText(html, 'html')

    msg['Subject'] = maildata['STATION_NM']+'역 시간표'  #메일 제목

    msg['From'] = fromAddr  #받는 메일 주소
    msg['To'] = toAddr  #보내는 메일 주소

    s = smtplib.SMTP("smtp.gmail.com", 587) # SMTP 서버와 연결
    s.starttls() # SMTP 연결을 TLS (Transport Layer Security) 모드로전환
   
    s.login('jjaeunjj@gmail.com', 'zkedcjmpqmhmiuav')  # 앱 password 이용
    s.sendmail(fromAddr , [toAddr], msg.as_string())    
    s.close() 
    