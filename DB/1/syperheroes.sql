-- SQL 문 작성 시 주의사항
-- 세미콜론(;) 기준으로 하나의 SQL문 판별

-- 새로운 테이블을 생성
-- id, 이름, 직업, 능력, 국적, 소속회사, 나이
-- 필드명, 타입, 제약조건 순으로 작성
-- NOT NULL : 이 필드는 NULL 값일 수 없다는 제약조건
CREATE TABLE superheroes(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  이름 TEXT NOT NULL,
  직업 TEXT NOT NULL,
  능력 TEXT,
  국적 TEXT,
  소속회사 TEXT,
  나이 INTEGER,
  가입날짜 DATE
);

-- 테이블 이름 변경
-- ALTER TABLE superheroes
-- RENAME to superhero;

-- ALTER TABLE superhero
-- ADD COLUMN 가입날짜 DATE;

-- 컬럼 추가
-- ALTER TABLE superhero
-- ADD COLUMN 임시 TEXT;

-- 컬럼 이름 변경
-- ALTER TABLE superhero
-- RENAME COLUMN 임시 TO 곧삭제;

-- 컬럼 삭제(버전이슈로 에러)
-- ALTER TABLE superhero
-- DROP COLUMN 곧삭제;

-- 테이블 삭제
-- DROP TABLE superhero;

-- 테이블에 CSV 파일 등록
-- .mode csv
-- .import superheroes.csv superhero

---------------------- 0. csv 파일 sqlite 로 읽기

-- 1. sqlite3 파일 열기
-- $ sqlite3 superhero.sqlite3

-- 2. csv 모드로 변경하기
-- $ sqlite> .mode csv

-- 3. 파일 read 하기
-- // 명령어: .import <파일명> <테이블명>
-- $ sqlite> .import superheroes.csv superhero

-- 4. 확인하기
-- $ sqlite> select * from superhero;

---------------------- 1. 전체 조회

-- 1.1 전체 필드 조회
SELECT * FROM superhero;

-- 1.2 특정 필드 조회(이름, 소속회사)
SELECT 이름, 소속회사 FROM superhero;

-- 1.3 없는 필드: no such column 이라는 에러
-- 필드 이름을 아무거나 넣고 select 해보세요.
SELECT anything FROM superhero;

-- 1.4 별칭 지어주기(이름 -> 활동명)
SELECT 이름 AS 활동명 FROM superhero;

-- 1.5 콤마로 구분 지어서 여러 개 별칭 짓기(이름 -> 활동명, 소속회사 -> 팀)
SELECT 이름 AS 활동명, 소속회사 AS 팀 FROM superhero;

-- 1.6 나이가 적은순으로 정렬하여 출력(내림차순 정렬)
SELECT 이름 FROM superhero
ORDER BY 나이 ASC;

-- 1.7 문자열도 정렬 가능(이름으로 정렬해보세요)
SELECT * FROM superhero
ORDER BY 이름 ASC;

-- 1.8 나이가 많은순으로 조회하기(내림차순 정렬)
SELECT * FROM superhero
ORDER BY 나이 DESC;

-- 1.9 여러 필드로 정렬하기
-- 소속회사 별, 나이가 많은 순으로 조회하기
SELECT * FROM superhero
ORDER BY 소속회사, 나이 DESC;


---------------------- 2. 중복 제거하기

-- 2.1 소속회사 중복을 제거하여 출력
SELECT DISTINCT 소속회사 FROM superhero;

-- 2.2 여러 필드를 사용하면, 모두 동일한 데이터를 삭제(직업, 소속회사 중복 제거)
SELECT DISTINCT 직업, 소속회사 FROM superhero;

-- 2.3 나이, 소속회사가 겹치지 않는 사람들 중
-- 소속회사, 나이 순으로 정렬
SELECT DISTINCT 직업, 소속회사 FROM superhero
ORDER BY 소속회사, 나이;

---------------------- 3. 조건문(WHERE)

-- 3.1 직업이 악당인 사람들만 조회
SELECT * FROM superhero
WHERE 직업 = '악당';

-- 비교연산자 사용하기
-- 3.2 나이가 50살이 넘는 사람들만 조회
SELECT * FROM superhero
WHERE 나이 > 50;

-- 3.3 가입날짜가 2000년 1월 1일 이전인 사람 조회(DATE 필드)
SELECT * FROM superhero
WHERE 가입날짜 < '2000-01-01';

-- 3.4 소속회사가 마블이고 직업이 영웅인 사람들만 조회
SELECT * FROM superhero
WHERE 소속회사 = '마블' AND 직업 = '영웅';

-- 3.5 국적이 미국이거나 러시아인 사람들만 조회
SELECT * FROM superhero
WHERE 국적 = '미국' OR 국적 = '러시아';

----------------------

-- 특정 패턴에 만족하는 데이터를 조회
-- EX) 2글자인 데이터, ~~맨 으로 끝나는 데이터

-- Like Operator

-- %(percent): 글자 수 제한 없이 패턴을 만족하면 조회
-- 3.6 이름이 ~~맨 으로 끝나는 사람들 조회
SELECT * FROM superhero
WHERE 이름 LIKE '%맨';

-- _(underscore): 개수 만큼 글자 수 제한하여 패턴을 만족하면 조회
-- 3.7 이름이 두 글자인 사람들만 조회
SELECT * FROM superhero
WHERE 이름 LIKE '__';

-- 특정 데이터에 포함여부(IN)
-- 3.8 마블, DC 소속의 사람들을 조회
SELECT * FROM superhero
WHERE 소속회사 IN ('마블', 'DC');

----------------------

-- 특정 조건 사이에 존재하는 데이터 조회(BETWEEN ... AND ... )

-- 3.9 나이가 100~500살 사이의 사람들을 조회
SELECT * FROM superhero
WHERE 나이 BETWEEN 100 AND 500;
-- WHERE 나이 <= 500 AND 100 <= 나이;

---------------------- 4. 집계함수

-- 원하는 행 개수만큼만 조회(LIMIT)
SELECT * FROM superhero LIMIT 1;

-- 4.1 나이가 가장 적은 사람 1명
SELECT * FROM superhero 
ORDER BY 나이 LIMIT 1;

-- 4.2 소속회사가 마블인 사람 중 나이가 가장 적은 1명
SELECT * FROM superhero 
WHERE 소속회사 = '마블'
ORDER BY 나이 LIMIT 1;

-- 4.3 나이가 많은 10명
SELECT * FROM superhero 
ORDER BY 나이 DESC 
LIMIT 10;

-- N 번째 데이터부터 조회 - 기준점을 변경(OFFSET)
-- 4.4 나이가 10번째로 많은 사람
SELECT * FROM superhero 
ORDER BY 나이 DESC 
LIMIT 9, 1;

-- 4.5 나이가 10번째 ~ 15번째 사람들
SELECT * FROM superhero 
ORDER BY 나이 DESC 
LIMIT 6 OFFSET 9;

----------------------

-- 데이터 수 구하기(COUNT)

-- 4.6 전체 데이터 수를 구하여라
SELECT COUNT(*) FROM superhero;

-- 조건문과 함께 활용하기
-- 4.7 직업이 악당인 사람의 수
SELECT COUNT(*) FROM superhero
WHERE 직업 = '악당';

-- 평균 구하기(AVG)

-- 4.8 마블의 영웅들의 평균 나이를 구하여라.
SELECT AVG(나이) AS 영웅평균나이 FROM superhero
WHERE 직업 = '영웅';

-- 다른 데이터타입은 에러는 나지 않고, 다른 값을 출력
SELECT AVG(능력) AS 영웅평균능력 FROM superhero
WHERE 직업 = '영웅';

-- 그룹 별 계산(GROUP BY)
-- 4.9 각 소속회사의 평균 나이를 구하여라
SELECT 소속회사, AVG(나이) AS 평균나이 FROM superhero
GROUP BY 소속회사;

-- 4.10 소속회사 별로 그룹화 하여, 40살 이상인 데이터만 조회하여라.
SELECT 소속회사, AVG(나이) AS 평균나이 FROM superhero
WHERE 나이 >= 40
GROUP BY 소속회사;

-- 그룹화 후에 조건주기(HAVING)
-- 4.11 각 소속회사 별 40세 이상인 사람들의 평균 나이를 구하여라
SELECT 소속회사, AVG(나이) AS 평균나이 FROM superhero
GROUP BY 소속회사
HAVING AVG(나이) >= 40;

