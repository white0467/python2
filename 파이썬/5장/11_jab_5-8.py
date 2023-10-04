'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395034 한유진    
    설명 : 별을 그리시오.
'''
import turtle as t  #터틀 모듈을 사용하기 위한 준비
                    #turtle 클래스 객체를 t로 생성. (별명)


t.shape('turtle')

t.speed()          #속도
i = 0
while i < 5:
    t.forward(150)     #200픽셀 만큼 이동.
    t.left(144)       #왼쪽으로회전.
    i = i + 1          
t.mainloop()        #그림판 사라지지 않음.
