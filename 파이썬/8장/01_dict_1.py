'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터공학부 202395034 한유진    
    설명 : 8.1 키와 값을 가지는 딕서너리

    튜플 = () 리스트 = [] 딕셔너리 = {}
'''
# 빈 딕셔너리 생성
phone_book1 = {}

# 딕셔너리에 값 저장. key, value    [key] 0 value
phone_book1['한유진'] = '010-6479-1848'

print('phone_book1 : ', phone_book1)    # {'한유진'} : '010-6479-1848'

# 딕셔너리에 값 저장. 2. {key : value}
phone_book2 = {'홍길동' : '010-7899-4545', '한유진' : '010-6479-1848'}
print('phone_book2 : ', phone_book2)    # {'한유진'} : '010-6479-1848'

phone_book3 = {}
phone_book3['한유진'] = '010-6479-1848'
phone_book3['홍길동'] = '010-3109-2123'
phone_book3['김만덕'] = '010-7123-9006'
phone_book3['홍서진'] = '010-3853-4154'
phone_book3['이유나'] = '010-2092-3154'

print('phone_book3 :', phone_book3)

print()
print(":: 전화번호 phone_book3 출력 ::")

# 모든 key 출력
print(phone_book3.keys())

# 모든 value 출력
print(phone_book3.values())

# 모든 key, value 출력
print(phone_book3.items())

print()
print(":: 전화번호 phone_book3 items() 출력 ::")
for name, phone_num in phone_book3.items() :
    print(name, ':', phone_num)

print()

print(":: 전화번호 phone_book3[keys] 출력 ::")
for key in phone_book3.keys() :
    print(key, ":", phone_book3[key])

print()

print("딕셔너리 작성 시 : (콜론)을 기준으로 key:value 작성")
person_dict = {'name':'한유진','age':19,'class':'1학년'}

print('name :', person_dict['name'])    # 딕셔너리의 'name' 키로 값을 초기화하여 출력
print('name :', person_dict['age'])    # 딕셔너리의 'age' 키로 값을 초기화하여 출력

print()

print(":: 정렬 ::")
# phone_book3 를 정렬
# 딕셔너를 키를 기준으로 정렬하여 리스트로 반환
print(sorted(phone_book3))

print(':: 키를 기준으로 전체 정렬 ::')
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[0])
print(sort_phone_book3)

print(':: 값를 기준으로 전체 정렬 ::')
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[1])
print(sort_phone_book3)

print()

print(":: 항목 전체 ::")
del phone_book3['한유진']
print(phone_book3)

print(":: 전체 삭제 ::")
phone_book3.clear()
print(phone_book3)