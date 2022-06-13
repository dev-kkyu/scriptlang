import requests
from tkinter import * 
import modules.spam

def drawGraph(line, subway):
    canvasWidth = 1000
    canvasHeight = 330


    graphwindow = Toplevel()
    graphwindow.title(line+' '+subway+'역 시간대별 승차 인원 그래프') 
    graphwindow.geometry("1000x330+200+100") 
    w = Canvas(graphwindow, width = canvasWidth, height=canvasHeight) 
    w.place(relx=.5, rely=.5,anchor= CENTER) # 한가운데 위치. 

    url = "http://openapi.seoul.go.kr:8088/7a65564f5264646f3131327078794f70/json/CardSubwayTime/1/1000/202111/"+line+"/"+subway+"/"
    res = requests.get(url)
    data = res.json()

    passengers =[]
    ride_num = data['CardSubwayTime']['row'][0]
    passengers.append(ride_num['FOUR_RIDE_NUM'])
    passengers.append(ride_num['FIVE_RIDE_NUM'])
    passengers.append(ride_num['SIX_RIDE_NUM'])
    passengers.append(ride_num['SEVEN_RIDE_NUM'])
    passengers.append(ride_num['EIGHT_RIDE_NUM'])
    passengers.append(ride_num['NINE_RIDE_NUM'])
    passengers.append(ride_num['TEN_RIDE_NUM'])
    passengers.append(ride_num['ELEVEN_RIDE_NUM'])
    passengers.append(ride_num['TWELVE_RIDE_NUM'])
    passengers.append(ride_num['THIRTEEN_RIDE_NUM'])
    passengers.append(ride_num['FOURTEEN_RIDE_NUM'])
    passengers.append(ride_num['FIFTEEN_RIDE_NUM'])
    passengers.append(ride_num['SIXTEEN_RIDE_NUM'])
    passengers.append(ride_num['SEVENTEEN_RIDE_NUM'])
    passengers.append(ride_num['EIGHTEEN_RIDE_NUM'])
    passengers.append(ride_num['NINETEEN_RIDE_NUM'])
    passengers.append(ride_num['TWENTY_RIDE_NUM'])
    passengers.append(ride_num['TWENTY_ONE_RIDE_NUM'])
    passengers.append(ride_num['TWENTY_TWO_RIDE_NUM'])
    passengers.append(ride_num['TWENTY_THREE_RIDE_NUM'])
    passengers.append(ride_num['MIDNIGHT_RIDE_NUM'])
    


    w.delete("grim") # 기존 그림 지우기
    if not len(passengers): # 데이터 없으면 return
        w.create_text(canvasWidth/2,(canvasHeight/2), text="No Data", tags="grim") 
        return

    nData = len(passengers) # 데이터 개수, 최대값, 최소값 얻어 놓기
    nMax = max(passengers) 

    # background 그리기
    w.create_rectangle(0, 0, canvasWidth, canvasHeight, fill='white', tag="grim")

    if nMax == 0: # devide by zero 방지
        nMax=1 

    rectWidth = (canvasWidth // nData) # 데이터 1개의 폭. 
    bottom = canvasHeight - 20 # bar의 bottom 위치 
    maxheight = canvasHeight - 50 # bar의 최대 높이.(위/아래 각각 20씩 여유.)

    for i in range(nData): # 각 데이터에 대해..
        if nMax == passengers[i]: 
            color="#35B62C"   # max인 경우는 특별한 색으로
        else: color="#92D050" 

        curHeight = maxheight * passengers[i] / nMax # 최대값에 대한 비율 반영
        top = bottom - curHeight # bar의 top 위치
        left = i * rectWidth # bar의 left 위치
        right = (i + 1) * rectWidth # bar의 right 위치
        w.create_rectangle(left, top, right, bottom, fill=color, tag="grim", activefill='#FFFFA1')
# 위에 값, 아래에 번호. 
        w.create_text((left+right)//2, top-15, text=modules.spam.stradd(str(passengers[i])), tags="grim") #승차인원수
        w.create_text((left+right)//2, bottom+10, text=i+4, tags="grim") #시간

