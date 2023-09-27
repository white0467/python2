'''
    작성일 : 2023년 9월 27일
    작성자 : 컴퓨터공학부 202395034 한유진    
    설명 : range() 함수
'''
for i in range(3):      # i 변수에 0 ~ 2의 값이 저장 됨.
    print(i, end='.')       #end=' ' 로 지정하면 줄바꿈 하지 않는다.
    print("안녕하세요.")
    print("     한유진입니다.")


# range(시작값, 숫자 앞까지, 증가값(감소값))
# C언어 - for(초기값; 조건식; 증감식)
for i in range(1, 6):   # range(1, 6, 1)
    print(i, end=' ')

print()#빈줄 출력

# 10 ~ 1 까지 출려
for i in range(10, 0, -1):      # 1씩 감소
    print(i, end=' ')
