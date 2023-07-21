import requests
from pprint import pprint


def get_deposit_products():
    # 금융감독원 API에서 json 데이터를 받는 함수이다.

    # 필수 요청 정보
    api_key = "a438e87af1b7346978755b03b975ea1b"
    sevice_name = 'depositProductsSearch'
    res_type = 'json'
    topFinGrpNo = '020000'
    pageNo = 1
    
    # URL 생성
    url = f'http://finlife.fss.or.kr/finlifeapi/{sevice_name}.{res_type}?auth={api_key}&topFinGrpNo={topFinGrpNo}&pageNo={pageNo}'
    
    # json 데이터 반환
    result = requests.get(url).json()    
    return result



### json 파일 response 변수 에 저장
response = get_deposit_products()



# baseList와 optionList 따로 생성
result = response['result']
baseList = result['baseList']
optionList = result['optionList']



# optionList 데이터 파싱
new_optionList = []
for i in range(len(optionList)):
    temp_dict = {}
    temp_dict['금융상품코드'] = optionList[i]['fin_prdt_cd']
    temp_dict['저축 금리'] = optionList[i]['intr_rate']
    temp_dict['저축 기간'] = optionList[i]['save_trm']
    temp_dict['저축금리유형'] = optionList[i]['intr_rate_type']
    temp_dict['저축금리유형명'] = optionList[i]['intr_rate_type_nm']
    temp_dict['최고 우대금리'] = optionList[i]['intr_rate2']
    new_optionList.append(temp_dict)



# 데이터를 가공하여 새로운 데이터 리스트에 보관
new_data = []

for index_1 in range(len(baseList)):
    temp_dict_1 = {}
    temp_list_1 = []
    
    for index_2 in range(len(new_optionList)):
        if baseList[index_1]['fin_prdt_cd'] == new_optionList[index_2]['금융상품코드']:
            temp_option_dict = dict(new_optionList[index_2])
            del temp_option_dict['금융상품코드']

            temp_list_1.append(temp_option_dict)

    temp_dict_1['금리정보'] = temp_list_1
    temp_dict_1['금융상품명'] = baseList[index_1]['fin_prdt_nm']
    temp_dict_1['금융회사명'] = baseList[index_1]['kor_co_nm']  

    new_data.append(temp_dict_1)



# 결과
pprint(new_data)