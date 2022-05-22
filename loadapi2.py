import requests

subway = input("검색할역 또는 호선: ")


#url="http://openAPI.seoul.go.kr:8088/7a65564f5264646f3131327078794f70/json/SearchInfoBySubwayNameService/1/5/"+subway+"/"
# url="http://openapi.seoul.go.kr:8088/7a65564f5264646f3131327078794f70/json/SearchSTNBySubwayLineInfo/1/5//"+subway
url="http://openapi.seoul.go.kr:8088/7a65564f5264646f3131327078794f70/json/SearchSTNBySubwayLineInfo/1/1000///"+subway

res = requests.get(url)

data = res.json()

#print(data)

code = data['SearchSTNBySubwayLineInfo']['row']

#print(code)

for i in code:
    print(i['STATION_CD'])
    print(i['STATION_NM'])
    # url="http://openAPI.seoul.go.kr:8088/515a78647a64646f313134534b664274/json/SearchSTNTimeTableByIDService/1/5/"+i['STATION_CD']+"/1/1/"

    # res = requests.get(url)
    # data = res.json()

    # a = data['SearchSTNTimeTableByIDService']['row']

    # for i in a:
    #     print('호선:',i['LINE_NUM'],'역명:',i['STATION_NM'],'출발시간:',i['LEFTTIME'],'상하행선:',i['INOUT_TAG'])

    