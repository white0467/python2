'''
    작성일 : 2023년 9월 27일
    작성자 : 컴퓨터공학부 202395034 한유진    
    설명 : 반복문으로 펙토리얼 구하기
            오늘의 마지막 문제!
'''
#사용자로부터 임의의 정수 n을 입력받은 뒤에 for 문을 이용하여 펙토리얼을 계산
#팩토리얼 n은 1부터 n까지의 정수를 모두 곱한 것을 의미
n = int(input("정수를 입력 : "))
fact=1
for i in range(1, n+1):
    fact=fact*i

print(n, "!은", fact, "이다.")