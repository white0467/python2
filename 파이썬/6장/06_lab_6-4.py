'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 202395034 한유진    
    설명 : LAB 6-4 리시트에서 최대값, 최소값을 찾아 돌려주는 함수

    리스트에 10개의 값을 랜덤으로 생성하고,
    MAX 또는 MIN을 입력 받아 최대, 최소값을 찾아 돌려주는 함수.

    [알고리즘]
    (함수)
            5) 두 값을 전달 받아 매개 변수에 저장.
            6) 최대값, 최소값을 찾는다.
            7) 값을 돌려준다.
    (메인)
        1. 무한반복
            1) 랜덤으로 10~99까지 10개의 수를 리스트로 생성.
            2) 생성된 리스트를 출력.
            3) 사용자로부터 최대값을 알고 싶은지 최소값을 알고 싶은지 묻는다.
                사용자가 입력할 값은 MAX 또는 MIN.
            4) 입력받은 MAX 또는 MIN과 생성된 리스트를 가지고 함수 호출.
            8) 돌려받은 치ㅗ대값 또는 최소값을 출력한다.

'''

import random

# 함수: 최대값 또는 최소값을 찾아 돌려주는 함수
def find_max_or_min(random_numbers):
    n = min(random_numbers)
    x = max(random_numbers)
    return n, x

# 메인 프로그램
while True:
    # 10개의 랜덤 숫자 리스트 생성
    random_numbers = [random.randint(10, 99) for _ in range(10)]
    n, x = find_max_or_min(random_numbers)

    # 생성된 리스트 출력
    print("생성된 리스트:", random_numbers)

    # 사용자에게 MAX 또는 MIN 입력 요청
    mode = input("최대값을 알고 싶으면 'MAX', 최소값을 알고 싶으면 'MIN'을 입력하세요: ")

    if mode == "min":       #최소값
        print(n)
    if mode == "max":       #최대값
        print(x)


