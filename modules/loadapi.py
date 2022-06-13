import requests

# 역이름 입력받고 해당 코드로 변환(API)된 코드로 시간표 받기(API)
def LoadSubwayTimetable(subway, line, flag):

    #역명별 지하철역 정보(역코드,호선)

    url="http://openapi.seoul.go.kr:8088/7a65564f5264646f3131327078794f70/json/SearchSTNBySubwayLineInfo/1/1000/ /"+subway+"/"+str(line)


    res = requests.get(url)
    data = res.json()

    if 'RESULT' in data:
        url="http://openapi.seoul.go.kr:8088/7a65564f5264646f3131327078794f70/json/SearchSTNBySubwayLineInfo/1/1000/ /"+subway


        res = requests.get(url)
        data = res.json()

        

        if 'RESULT' in data:
            return dict(info=False)
        linedata=[]
        for i in data['SearchSTNBySubwayLineInfo']['row']:
            linedata.append(dict(STATION_NM = i['STATION_NM'], LINE_NUM=i['LINE_NUM']))
        
        return dict(info=False, data=linedata)
    

    code = data['SearchSTNBySubwayLineInfo']['row'][0]['STATION_CD']

    # 코드만 얻고 싶으면
    if flag == 1:
        return code

    data=Code2Timetable(code)
    if data == False:
        return dict(info=False, data=data)

    return dict(info=True, data=data)


def Code2Timetable(code):
    data ={}
    time =[]
    time_data={}


    url="http://openAPI.seoul.go.kr:8088/515a78647a64646f313134534b664274/json/SearchSTNTimeTableByIDService/1/1000/"+str(code)+"/1/1/"

    res = requests.get(url)
    res_data = res.json()

    if 'RESULT' in res_data:
        return False

    a = res_data['SearchSTNTimeTableByIDService']['row']


    for i in a:
        time.append(i['LEFTTIME'])
    time_data['1']=time

    time =[]
    url="http://openAPI.seoul.go.kr:8088/515a78647a64646f313134534b664274/json/SearchSTNTimeTableByIDService/1/1000/"+str(code)+"/1/2/"

    res = requests.get(url)
    res_data = res.json()

    if 'RESULT' in res_data:
        return False

    a = res_data['SearchSTNTimeTableByIDService']['row']

    for i in a:
        time.append(i['LEFTTIME'])
    time_data['2']=time

    data['Schedule']=time_data
    data['STATION_NM']=a[0]['STATION_NM']
    data['LINE_NUM']=a[0]['LINE_NUM']

    return data


def LoadSubwaystationtable(line):

    url = "http://openapi.seoul.go.kr:8088/515a78647a64646f313134534b664274/json/SearchSTNBySubwayLineInfo/1/1000/ / /"+line+"호선/"
    res = requests.get(url)
    data = res.json()


    code = data['SearchSTNBySubwayLineInfo']['row']

    station = []
    for i in code:
        station.append(i['STATION_NM'])

    return station


def LoadSubwayTimetable2(subway):
    url="http://openapi.seoul.go.kr:8088/7a65564f5264646f3131327078794f70/json/SearchSTNBySubwayLineInfo/1/1000/ /"+subway


    res = requests.get(url)
    data = res.json()

    if 'RESULT' in data:
        return False

    code = []
    for i in data['SearchSTNBySubwayLineInfo']['row']:
        code.append(i['STATION_CD'])


    data = []
    for i in code:
        data.append(Code2Timetable(i))
    
    line = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    data2 = []
    for i in data:
        if i != False:
            if int(i['LINE_NUM'][1]) in line:
                data2.append(i)

    return data2
