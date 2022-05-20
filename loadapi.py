import requests
import pprint

while True:
    subway = input("검색할역: ")

    url = 'http://openapi.seoul.go.kr:8088/586d64614a64657631313149706f4e59/json/SearchInfoBySubwayNameService/1/5/'+subway


    response = requests.get(url)
    data = response.json()

    # pp = pprint.PrettyPrinter()
    pprint.PrettyPrinter().pprint(data)

    # for i in data['SearchInfoBySubwayNameService']['row']:
    #     pp = pprint.PrettyPrinter()
    #     pp.pprint(i)

        # print(i['STATION_CD'], i['STATION_NM'], i['LINE_NUM'])

    # time = []

    # for i in data['SearchInfoBySubwayNameService']['row']:
    #     time.append(requests.get('http://openAPI.seoul.go.kr:8088/585977514d6465763131374e4f695744/json/SearchSTNTimeTableByIDService/1/5/' + i['STATION_CD'] + '/1/1/').json())

    # for i in time:
    #     for j in i['SearchSTNTimeTableByIDService']['row']:
    #         print(j['STATION_CD'], j['STATION_NM'], j['TRAIN_NO'], j['ARRIVETIME'], j['LEFTTIME'], j['INOUT_TAG'])
        # print(i['STATION_CD'], i['STATION_NM'], i['LINE_NUM'])

    # time = 'http://openAPI.seoul.go.kr:8088/585977514d6465763131374e4f695744/json/SearchSTNTimeTableByIDService/1/5/2561/1/1/'
