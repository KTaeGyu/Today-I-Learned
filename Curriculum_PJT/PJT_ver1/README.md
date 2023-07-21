## 목차

# 금융 상품 비교 앱 만들기 프로젝트

## 1. 프로젝트 설명


### 앱을 만들게 된 계기


### 앱을 만들면서 새롭게 배운 것
#### 외부 API를 사용하여 데이터를 받아오고, 데이터를 원하는 형태로 가공하는 방법을 공부함.

<br>

- OPEN API 이용 방법
    1. OPEN API를 제공하는 사이트에서 인증키를 발급받는다.
    2. 인증키와 사용하려는 API의 URL을 받아 데이터를 json 형태로 받는다.
        ```python
        import requests
        response = requests.get(url).json()
        ```

<br>

- json 형태의 데이터 가공하기
    1. 불러온 데이터 형태 파악
        ```python
        print(response)
        # {"name": "KTG", "age": 28, "city": "seoul", ...}
        ```
        - pprint 를 이용하면 좀더 깔끔한 형태로 볼 수 있다.
        ```python
        from pprint import pprint
        print(response)
        """
        {"name": "KTG",
         "age": 28,
         "city": "seoul",
         ...}
        """
        ```
    2. 필요한 데이터 파싱 (Parsing)
        ```python
        my_data = {}
        my_data["이름"] = response["name"]
        my_data["나이"] = response["age"]
        print{my_data}
        """
        {"이름": KTG, "나이": 28}
        """
        ```

<br>

## 2. 앱 기능, 사용된 기술


## 3. 프로젝트 설치 및 실행 방법


## 4. 팀원 및 참고 자료


### 5. 단계별 프로젝트 진행도
---
#### 20230721. 파이썬과 OPEN API를 이용한 금융 데이터 수집
- 금융감독원 금융상품통합비교공시의 OPEN API를 이용하여 다음과 같이 금융상품별 금리 정보를 출력하였다.
```python
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
"""
[{'금리정보': [{'저축 금리': 3.67,
            '저축 기간': '6',
            '저축금리유형': 'S',
            '저축금리유형명': '단리',
            '최고 우대금리': 3.67},
           {'저축 금리': 3.73,
            '저축 기간': '12',
            '저축금리유형': 'S',
            '저축금리유형명': '단리',
            '최고 우대금리': 3.73},
           {'저축 금리': 3.36,
            '저축 기간': '24',
            '저축금리유형': 'S',
            '저축금리유형명': '단리',
            '최고 우대금리': 3.36},
           {'저축 금리': 3.33,
            '저축 기간': '36',
            '저축금리유형': 'S',
            '저축금리유형명': '단리',
            '최고 우대금리': 3.33}],
  '금융상품명': 'WON플러스예금',
  '금융회사명': '우리은행'},
 {'금리정보': [{'저축 금리': 3.7,
            '저축 기간': '6',
            '저축금리유형': 'S',
            '저축금리유형명': '단리',
            '최고 우대금리': 3.9},
           {'저축 금리': 3.9,
            '저축 기간': '12',
            '저축금리유형': 'S',
            '저축금리유형명': '단리',
            '최고 우대금리': 4.2}],
  '금융상품명': 'e-그린세이브예금',
  '금융회사명': '한국스탠다드차타드은행'},
...
{'금리정보': [{'저축 금리': 3.2,
            '저축 기간': '6',
            '저축금리유형': 'S',
            '저축금리유형명': '단리',
            '최고 우대금리': 3.2},
           {'저축 금리': 3.5,
            '저축 기간': '12',
            '저축금리유형': 'S',
            '저축금리유형명': '단리',
            '최고 우대금리': 3.5},
           {'저축 금리': 3.5,
            '저축 기간': '24',
            '저축금리유형': 'S',
            '저축금리유형명': '단리',
            '최고 우대금리': 3.5},
           {'저축 금리': 3.5,
            '저축 기간': '36',
            '저축금리유형': 'S',
            '저축금리유형명': '단리',
            '최고 우대금리': 3.5}],
  '금융상품명': '카카오뱅크 정기예금',
  '금융회사명': '주식회사 카카오뱅크'}
"""
```