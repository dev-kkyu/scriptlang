# scriptlang

## Development Environment
Python Ver. 3.9.10

Windows 10-Pro 64bit

Visual Studio Code Ver 1.67.0

## Info
github 주소 : https://github.com/devkkyu/scriptlang
GUI 프로그램의 메인모듈 이름 : Subway.py
텔레그램 서비스 프로그램의 메인모듈 이름 : Telegram_bot.py
텔레그램 봇의 username(name이 아닙니다) : @subway_schedule_skje_bot

## Description
### Subway.py
#### mainWindow 클래스
객체 생성 시 메인 GUI 창을 출력하고 각 기능 정의
### Telegram_bot.py
텔레그램에 반응할 이벤트 정의
### loadapi.py
#### LoadSubwayTimetable(subway, line, flag)
flag가 1이면 지하철역의 코드 반환
이외의 경우 해당 지하철역의 시간표 반환
#### Code2Timetable(code)
해당 역코드의 시간표 반환
#### LoadSubwaystationtable(line)
해당 호선의 역목록 출력
#### LoadSubwayTimetable2(subway)
해당 지하철역 명이 존재하는 모든 호선의 해당역의 시간표를 반환
#### peoplePerTime(line, subway)
해당 역의 시간대별 승차인원 반환
### email_send.py
#### sendMail(fromAddr, toAddr, code)
메일 전송
### graph.py
#### drawGraph(line, subway)
그래프 창 출력
### map_show.py
#### mapview(subway)
지도 창 출력
### spam.pyd
#### stradd(text)
text + '\n' + 'people' 반환