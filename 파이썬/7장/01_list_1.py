'''
    작성일 : 2023년 10월 18일
    작성자 : 컴퓨터공학부 202395034 한유진    
    설명 : 리스트 만들기
'''
# 과일 리스트 만들기
fruits = ['딸기', '바나나', '사과']
print('과일 목록 : ', fruits)

# 수박 추가(이외 추가 가능) => append() 메소드 사용 (마지막에 추가)
fruits.append('수박')
print('과일 목록(수박 추가) : ', fruits)
fruits.append('망고')
print('과일 목록(망고 추가) : ', fruits)

# 포도 추가 => + 연산자 사용 : 연결 연산자
fruits = fruits + ['포도']      #포도를 더해서 fruits에 저장 num = num + 1
print('과일 목록(포도 추가) : ', fruits)

# 리스트에서 +는 연결이다
num = [1,2,3] + [4,5,6]
print("숫자 리스트 :", num)

# * 연산자 => 리스트를 n번 반복한다
num = [1,2,3] * 3
print("숫자 리스트 * 3 :", num)

# in 연산자 => 포함되는가?
print("과일 목록에 망고가 있나요? ", '망고' in fruits)

'''
    인덱스를 사용하여 리스트의 항목에 접근하기
'''
# 과일 리스트에 있는 과일의 개수?
print("과일 리스트에 있는 과일 개수 : ", len(fruits))
# 과일 리스트 중 제일 첫번째 과일은? 
print("과일 중 제일 좋아하는 과일은? ", fruits[0])

# 과일 리스트 중 제일 마지막 과일은? 
print("과일 중 제일 마지막 과일은? ", fruits[-1])
 
# 과일 중 가장 큰 과일은?
print("과일 중 가장 큰 과일은?(사전식 순서) ", max(fruits))      # 사전식 숫자로 제일 큼

# 과일 중 가장 작은 과일은?
print("과일 중 가장 큰 과일은?(사전식 순서) ", min(fruits))      # 사전식 숫자로 제일 작음

# 정렬
fruits.sort()   # 오름차순
print("오름차순 정렬", fruits)
fruits.sort(reverse=True)   # 내림차순
print("내림차순 정렬", fruits)


'''
    리스트를 원하는 모양으로 자르느 슬라이딩
'''
print("과일 리스트 중 2,3,4번 과일은? ", fruits[1:4])   # 1번지 ~ 4번지 앞까지
print("과일 리스트 중 1~3번 과일은? ", fruits[1:3])   # 0번지 ~ 2번지 앞까지
print("과일 리스트 중 1~3번 과일은? ", fruits[:3])   # 0번지 ~ 2번지 앞까지
print("과일 리스트 중 3번 과일부터 마지막 과일은? ", fruits[2:])   # 2번지 ~ 5번지 앞까지

# 처음부터 끝까지 리스트 중에서 2씩 증가하면서...
print("과일 리스트 중 1,3,5번 과일은? ", fruits[::2]) 
print("과일 거꾸로 출력", fruits[::-1])     # reverse와 같다 / 역순으로 정렬

'''
    리스트의 원소 값을 자유롭게 조작해 보자.
'''
print()
print("과일 목록 :", fruits)

# 원하는 위치에 '두리안' 추가 => insert() 메소드
fruits.insert(3, '두리안')
print("과일 목록(3번지에 두리안 추가) : ", fruits)

# 위치 찾기 => index() 메소드
print("사과의 위치는? ", fruits.index('사과'))

# 사과 마지막에 추가
fruits.append('사과')
print("과일 목록(사과 마지막에 추가) : ", fruits)

# 사과의 개수 => count() 메소드
print("사과의 개수 : ",fruits.count('사과'))


'''
    리스트의 항목 삭제
'''
print()

# 사과 삭제 => remove() 메소드 : 삭제할 항목 지정.
fruits.remove('사과')   #처음 만나는 사과만 삭제
print("과일 목록(사과 삭제 후) : ",fruits)

# 항목 삭제 => pop() 메소드
fruits.pop()        # 마지막 항목 삭제 (무조건 마지막 항목 삭제)
print("과일 목록 : ", fruits)

# del() 키워드 => 포도 삭제
del fruits[0]   # 0번지 항목 삭제
print("과일 목록(포도(0번지) 삭제)", fruits)
