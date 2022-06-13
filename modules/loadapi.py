import requests

# 역이름 입력받고 해당 코드로 변환(API)된 코드로 시간표 받기(API)
def LoadSubwayTimetable(subway, line, flag):  #시간표 데이터를 리턴하는 함수

    #역명별 지하철역 정보(역코드,호선)

    url="http://openapi.seoul.go.kr:8088/7a65564f5264646f3131327078794f70/json/SearchSTNBySubwayLineInfo/1/1000/ /"+subway+"/"+str(line)


    res = requests.get(url)  #url에서 데이터를 받아온다
    data = res.json()    #데이터를 json으로 변환

    if 'RESULT' in data:
        url="http://openapi.seoul.go.kr:8088/7a65564f5264646f3131327078794f70/json/SearchSTNBySubwayLineInfo/1/1000/ /"+subway


        res = requests.get(url) #url에서 데이터를 받아온다
        data = res.json()  #데이터를 json으로 변환

        

        if 'RESULT' in data:  #반환된 데이터가 없으면 False를 반환
            return dict(info=False)

        linedata=[]
        for i in data['SearchSTNBySubwayLineInfo']['row']: #반환된 데이터에서 SearchSTNBySubwayLineInfo의 row중 
            linedata.append(dict(STATION_NM = i['STATION_NM'], LINE_NUM=i['LINE_NUM']))   #역이름과 호선에 해당하는 데이터를 저장
        
        return dict(info=False, data=linedata) #데이터가 저장된 딕셔너리를 반환
    

    code = data['SearchSTNBySubwayLineInfo']['row'][0]['STATION_CD']   #code에 지하철역 코드를 저장

    # 코드만 얻고 싶으면
    if flag == 1:
        return code

    data=Code2Timetable(code)
    if data == False:
        return dict(info=False, data=data)

    return dict(info=True, data=data)


def Code2Timetable(code): #역코드로 역의 시간표 데이터를 반환하는 함수
    data ={}
    time =[]
    time_data={}

    #역코드로 상행 열차의 데이터를 가져옴
    url="http://openAPI.seoul.go.kr:8088/515a78647a64646f313134534b664274/json/SearchSTNTimeTableByIDService/1/1000/"+str(code)+"/1/1/"

    res = requests.get(url)      #url에서 데이터를 받아온다
    res_data = res.json()      #데이터를 json으로 변환

    if 'RESULT' in res_data: #반환된 데이터가 없으면 False를 반환
        return False

    a = res_data['SearchSTNTimeTableByIDService']['row']   #반환된 데이터의 row에 햐당하는 데이터만 저장


    for i in a: #저장한 데이터 중
        time.append(i['LEFTTIME'])  #열차가 떠나는 시간 데이터만 time리스트에 저장
    time_data['1']=time #time_data딕셔너리에 상행 데이터를 저장

    time =[] #time리스트 초기화
    
    #역코드로 상행 열차의 데이터를 가져옴
    url="http://openAPI.seoul.go.kr:8088/515a78647a64646f313134534b664274/json/SearchSTNTimeTableByIDService/1/1000/"+str(code)+"/1/2/"

    res = requests.get(url)      #url에서 데이터를 받아온다
    res_data = res.json()      #데이터를 json으로 변환

    if 'RESULT' in res_data: #반환된 데이터가 없으면 False를 반환
        return False

    a = res_data['SearchSTNTimeTableByIDService']['row']  #반환된 데이터의 row에 햐당하는 데이터만 저장

    for i in a: #저장한 데이터 중
        time.append(i['LEFTTIME'])  #열차가 떠나는 시간 데이터만 time리스트에 저장
    time_data['2']=time #time_data딕셔너리에 하행 데이터를 저장

    data['Schedule']=time_data  #data딕셔너리에 시간표를 저장
    data['STATION_NM']=a[0]['STATION_NM']  #data딕셔너리에 역이름을 저장
    data['LINE_NUM']=a[0]['LINE_NUM']  #data딕셔너리에 호선을 저장

    return data   #완성된 시간표 데이터 리턴


def LoadSubwaystationtable(line):   #호선별 역 목록을 반환하는 함수

    url = "http://openapi.seoul.go.kr:8088/515a78647a64646f313134534b664274/json/SearchSTNBySubwayLineInfo/1/1000/ / /"+line+"호선/"
    res = requests.get(url)    #url에서 데이터를 받아온다
    data = res.json()          #데이터를 json으로 변환

    code = data['SearchSTNBySubwayLineInfo']['row']

    station = []
    for i in code:  #반환된 데이터 중 역 이름만 저장
        station.append(i['STATION_NM'])

    return station  #저장한 호선별 역 목록 반환


def LoadSubwayTimetable2(subway):    #역 이름으로 역의 호선 정보를 반환하는 함수
    url="http://openapi.seoul.go.kr:8088/7a65564f5264646f3131327078794f70/json/SearchSTNBySubwayLineInfo/1/1000/ /"+subway

    res = requests.get(url)    #url에서 데이터를 받아온다
    data = res.json()          #데이터를 json으로 변환

    if 'RESULT' in data:  #반환된 데이터가 없으면 False를 반환
        return False

    code = []
    for i in data['SearchSTNBySubwayLineInfo']['row']:   #반환된 데이커 중 역 코드 데이터만 저장
        code.append(i['STATION_CD'])


    data = []
    for i in code:  #저장된 역 코드로 호선 정보를 반환하여 저장
        data.append(Code2Timetable(i))
    
    line = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    data2 = []
    for i in data:
        if i != False:  #반환된 데이터가 있으면 1호선에서 9호선 중 해당하는 호선 정보만 저장
            if int(i['LINE_NUM'][1]) in line:
                data2.append(i)

    return data2  #저장한 호선 정보 반환


def peoplePerTime(line, subway):  #시간대별 승하인원 데이터를 반환하는 함수
    url = "http://openapi.seoul.go.kr:8088/7a65564f5264646f3131327078794f70/json/CardSubwayTime/1/1000/202111/"+line+"/"+subway+"/"
    res = requests.get(url)    #url에서 데이터를 받아온다
    data = res.json()          #데이터를 json으로 변환

    if 'RESULT' in data:   #반환된 데이터가 없으면 False를 반환
        return False

    return data['CardSubwayTime']['row'][0]  #시간대별 승하인원 데이터를 반환