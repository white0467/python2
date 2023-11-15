'''
    작성일 : 2023년 11월 15일
    작성자 : 컴퓨터공학부 202395034 한유진    
    설명 : 문자열
'''
# 문자열 슬라이딩
s = 'Happy Day!'
print(s[0])         # 0번지를 짤라 출력
print(s[6:9])       # 6번지부터 9번지까지 
print(s[:-2])       # 시작부터 맨 뒤에서 2번째까지

#문자열 분리    :split()
s='Welcome to Python'
print(s.split())    # 공백을 기준으로 분리

s = '2023.11.15'
print(s.split('.')) # 분리 기준은 . 이다

s = 'Hello, World!'
print(s.split(',')) #분리 기준은 , 이다

s = 'Hello, World!'
print(s.split(', '))    # 분리 기준은 ,  이다

# 공백 제거     : strip()
s = 'Welcome, to , Python, and , bla, bla       '
print(s.strip())    
print([x.strip() for x in s.split(',')])

print(list('Hello, World!'))


# 문자열 연결 : join()
print(','.join(['apple','grape','banana']))     # 쉼표를 붙여서 연결.
print('-'.join('010.1234.5678'.split('.')))     # .으로 구분된 번호를 -로 고침

# .을 -로 바꾸기
print('0101.1234.5678'.replace('.','-'))        # .으로 구분된 번호를 -로 고침

s = 'Hello, World!'
print(s)
# s에 저장된 문자열을 리스트로 분자열 분리 시켜 slist에 저장
slist = list(s)
print(slist)

# 분리된 문자를 다시 합치기
print(''.join(slist))

# 줄바꿈과 탭이 포함된 문자열 그대로 출력
a_String = 'Today as well, \n\t Have a Happy Day'
print(a_String)

# 문자열 자르기 word_list에 저장.
word_list = a_String.split()
print(word_list)

# 다시 합치기 : 문자열을 자르고 다시 합치면 줄바꿈과 탭이 삭제됨.
refined_string = " ".join(word_list)
print(refined_string)

# 대소문자 변환과 문자열 삭제
s = 'Hello, World!'
print(s)
print(s.lower())        # 모두 소문자로 바꿈
print(s.upper())        # 모두 대문자로 바꿈

# 공백 제거     strip()
s = '      Hello, World!       '
print(s.split())    # 왼쪽, 오른쪽 모든 공백 제거
print(s.lstrip())   # 왼쪽 공백 제거
print(s.rstrip())   # 오른쪽 공백 제거

s = '#######Hello, World!#########'
print(s)
print(s.strip('#'))
print(s.lstrip('#'))


# 문자열 찾기 
s = 'www.silla.ac.kr'   # 리스트  .index (주소)
# .kr 찾기
print(s.find('.kr'))    # 12번지를 출력
# x 찾기
print(s.find('x'))      # -1 (a 문자열이 없다)

# . 이 몇개인가?
print(s.count('.'))
