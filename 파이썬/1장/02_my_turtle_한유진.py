'''
    작성일 : 2023년 9월 13일
    작성자 : 컴퓨터공학부 202395034 한유진    
    설명 : 주석과 출력 함수 사용하기.
'''

import turtle as t  #터틀 모듈을 사용하기 위한 준비
                    #turtle 클래스 객체를 t로 생성. (별명)


t.shape('turtle')

t.speed(200)          #속도



#선그리기
#t.forward(200)      #200 픽셀 이동.

#삼각형 그리기  
#t.forward(200)      #200픽셀 만큼 이동.
#t.left(120)          #왼쪽으로 60도 회전.
#t.forward(200)      #200픽셀 만큼 이동.
#t.left(120)          #왼쪽으로 60도 회전.
#t.forward(200)      #200픽셀 만큼 이동.
#t.left(120)          #왼쪽으로 60도 회전.

#반복문으로 삼각형 그리기
# for i in range(9) :
#     t.forward(200)     #200픽셀 만큼 이동.
#     t.left(144)          #왼쪽으로회전.
for i in range(100) :
    t.forward(i)     #200픽셀 만큼 이동.
    t.left(312)          #왼쪽으로회전.
t.mainloop()        #그림판 사라지지 않음.