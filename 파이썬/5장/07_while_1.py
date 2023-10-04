'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395034 한유진    
    설명 : 조건에 따라 반복하는 while 문
            교재 127 페이지
'''
# while 조건식 : => : 반드식 사용.
#   들여쓰기로 반복하면서 할일 작성.

under_construction = True   # 공사중.

#True 일 동안 계속 반복.
while under_construction :          # while = 반복문 under_construction = 조건
    response = input("공사가 완료 되었습니까?")
    if response == "예":
        under_construction = False  # 공사 완료     False = break

print("루프 탈출!!!")