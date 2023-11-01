'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터공학부 202395034 한유진    
    설명 : LAB 7 5 함수는 튜플을 돌려줄 수 있다.
        
        반지름을 입력받아 원의 넒이와 둘레를 계산하시오.
        넒이와 둘레를 계산하는 함수를 작성하시오.
        함수는 넒이와 둘레를 함께 돌려줍니다.(return)

        [함수]
            3. 반지름을 받아서 매개변수에 저장한다.
            4. 넒이와 둘레를 계산한다.
            5. 넒이와 둘레를 돌려준다.(함수를 호출한 곳으로)
        [메인]
            1. 반지름을 입력 받는다.
            2. 함수 호출 -> 반지름을 가지고 호출한다.
            6. 돌려받은 넒이와 둘레를 정장한다.
                (넒이, 둘레)
            7. 출력한다
'''
import math

def S(r):
    area=math.pi * r * r    # 넒이 계산
    C = 2 * math.pi * r     # 둘레 계산
    return area, C          # 넒이와 둘레의 값을 튜플로 변환 함

r=float(input("반지름을 입력 : "))
circle = S(r)
print(f"반지름 {r} 원의 넒이는 {circle[0]:.2f}이고 원의 둘레는 {circle[1]:.2f}이다.")

