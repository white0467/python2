'''
    작성일 : 2023년 9월 20일
    작성자 : 컴퓨터공학부 202395034 한유진    
    설명 : 선택문 if~else
            random 을 이용한 가위바위보 게임.

            random 함수로 생성된 정수를 가지고 게임을 진행합니다.
            0 => 가위
            1 => 바위
            2 => 보

            두 명의 플레이어의 이름을 입력 받아 가위바위보 게임을 진행합니다.
'''
import random  # random 함수 가져오기. (포함 시키기)

print(":: 가위바위보 게임 시작 ::")

player1 = input("player1의 이름 : ")
player2 = input("player2의 이름 : ")

print(player1, " : ", end='')
# 가위 바위 보
num1 = random.randrange(3)
if num1 == 0:
    print("가위")
elif num1 == 1:
    print("바위")
else:
    print("보")

print(player2, " : ", end='')
# 가위 바위 보
num2 = random.randrange(3)
if num2 == 0:
    print("가위")
elif num2 == 1:
    print("바위")
else:
    print("보")

# 가위바위보 승자 결정
if num1 == num2:
    print("비겼습니다")
elif (num1 == 0 and num2 == 2) or (num1 == 1 and num2 == 0) or (num1 == 2 and num2 == 1):
    print(player1, "이 이겼습니다")
else:
    print(player2, "이 이겼습니다!")



