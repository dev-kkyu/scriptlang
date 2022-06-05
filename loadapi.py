import requests

# 역이름 입력받고 해당 코드로 변환(API)된 코드로 시간표 받기(API)
def LoadSubwayTimetable(subway,line):

    #역명별 지하철역 정보(역코드,호선)

    url="http://openapi.seoul.go.kr:8088/7a65564f5264646f3131327078794f70/json/SearchSTNBySubwayLineInfo/1/1000/ /"+subway+"/"+str(line)


    res = requests.get(url)
    data = res.json()

    
    # if data['SearchSTNBySubwayLineInfo']['RESULT']['CODE'] == 'INFO-200':
    #     return False

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
        #print(linedata)
    

    code = data['SearchSTNBySubwayLineInfo']['row'][0]['STATION_CD']
    #print(code)

    #print(code[0]['STATION_CD'])

    #{'LINE_NUM' : '4호선', 'Schedule' : {'1' :  ['00:05:51', '00:05:59'], '2' : ['00:05:53', '00:06:01']} }
    #data['Schedule']=
    #print(Code2Timetable(code))

    data=Code2Timetable(code)
    if data == False:
        return dict(info=False, data=data)

    return dict(info=True, data=data)


def Code2Timetable(code):
    data ={}
    time =[]
    time_data={}
    #for i in code:

    url="http://openAPI.seoul.go.kr:8088/515a78647a64646f313134534b664274/json/SearchSTNTimeTableByIDService/1/1000/"+str(code)+"/1/1/"

    res = requests.get(url)
    res_data = res.json()

    if 'RESULT' in res_data:
        return False

    a = res_data['SearchSTNTimeTableByIDService']['row']

    # data['LINE_NUM']=a[0]['LINE_NUM']

    for i in a:
       # print('호선:',i['LINE_NUM'],'출발시간:',i['LEFTTIME'],'상하행선:',i['INOUT_TAG'])
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
        #print('호선:',i['LINE_NUM'],'출발시간:',i['LEFTTIME'],'상하행선:',i['INOUT_TAG'])
        time.append(i['LEFTTIME'])
    time_data['2']=time

    data['Schedule']=time_data
    data['STATION_NM']=a[0]['STATION_NM']

    # print(data)


    return data



#line = input('호선 입력:')

def LoadSubwaystationtable(line):

    url = "http://openapi.seoul.go.kr:8088/515a78647a64646f313134534b664274/json/SearchSTNBySubwayLineInfo/1/1000/ / /"+line+"호선/"
    res = requests.get(url)
    data = res.json()

    #print(data)

    code = data['SearchSTNBySubwayLineInfo']['row']
    #print(code)

    station = []
    for i in code:
        #print(i['SUB_STA_NM'])
        station.append(i['STATION_NM'])

    #print(station)
    return station
