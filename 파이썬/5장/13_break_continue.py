'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395034 한유진    
    설명 : 반복을 제어하는 break, continue
            교재 137 페이지
        
    test word : programming
'''

word = input("단어 입력 : ")        # 단어 입력
print(":: break ::")        
for i in word :     # hello
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':        # 모음을 만나면 반복 중지
        break   #포함된 반복이 종료
    else:
        print(i, end='')    # programming 중 a e i o u 를 만나면 프로그램이 종료됨 # 결과는 pr

print()

print(":: break ::")    
for i in word :     
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:        # 모음을 만나면 반복 중지
        break   #반복을 중단한다. 반복을 빠져 나간다.
    else:
        print(i, end='')    #결과는 pr 

print()

print(":: continue ::")
for i in word :     
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:        # 모음이 있으면 반복문을 초기값으로 변형 후 출력 pr(o)gr(a)mm(i)ng 괄호 제외 출력
        continue    # 반복의 시작(처음)으로 돌아감. (계속 반복) # 아래 문장을 만날 수 없다
    print(i, end='')    #결과 값은 prgrmmng