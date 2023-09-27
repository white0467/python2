'''
    작성일 : 2023년 9월 27일
    작성자 : 컴퓨터공학부 202395034 한유진    
    설명 : 점수를 입력 받아 학점을 출력.
            90~100 : A학점
            80~90  : B학점
            70~80  : C학점
            60~70  : D학점
            ~59    : F학점

    알고리즘 : 1. 점수를 입력 받는다.
                2. 판단하여 출력한다.
'''

#점수를 입력 받는다.
score = int(input("점수 입력 : "))
            
#판단.
#이 코드는 논리 오류가 발생한다. - 300점 입력하면 A학점으로 나온다.
print("::: 첫 번째 성정처리:::")

if score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
elif score >= 60:
    print("D학점")
else:
    print("F학점")

print()

#정확한 범위를 지정하자. - 성적의 범위를 벗어나면 잘못된 점수 입력됩니다.
print("::: 두 번째 성정처리:::")
if (90 <= score <= 100) :
    print("A학점")
elif (score >= 80 and score <= 89):     #score >= 80 && score <= 89
    print("B학점")
elif (70 <= score <= 79) :
    print("C학점")
elif (60 <= score <= 69) :
    print("D학점")
elif (0 <= score <= 69) :
    print("F학점")
else:
    print("점수를 잘못 입력하셨습니다.")

print()

#점수는 무조건 0 ~ 100 점 사이입니다. - 아니면 잘못된 입력입니다.
print("::: 세 번째 성정처리:::")
if 0<= score <= 100:
    if (90 <= score <= 100) :
        print("A학점")
    elif (score >= 80 and score <= 89):     #score >= 80 && score <= 89
        print("B학점")
    elif (70 <= score <= 79) :
        print("C학점")
    elif (60 <= score <= 69) :
        print("D학점")
    else:   #A,B,C,D 학점이 아니면
        print("F학점")
else:   # 0 ~ 100 사이의 점수가 아니면
    print("점수를 잘못 입력하셨습니다.")
