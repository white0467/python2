'''
    작성일 : 2023년 11월 15일
    작성자 : 컴퓨터공학부 202395034 한유진    
    설명 : LAB 9-2 : 트위터 메세지 처리의 단어 추출
        띄어쓰기로 문자열을 분리하고, 단어의 개수를 찾아라
'''

text = "There's a reason some people are working to make \
    it harder to vote, especially for people of color. \
    It’s because when we show up, things change."

# 띄어쓰기로 문자열을  분리하고 단어의 개수를 찾아라.
text2 = text.split()
print(text2)
print("단어 개수 : ",len(text2))

# 도전문제 9-1
# 회사 이름은 **로 표시
# KT, Samsung, LG, SKT
text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG U+ Mystic Pink 30%, SKT Mystic Blue not disclosed) '

company = ['SKT','KT', 'Samsung', 'LG']
# 모든 문자를 소문자로 변환
so = text.lower()

# 소문자로 바뀐 단어들을 공백으로 구분
print(so.split())


# 구분된 단어를 검사. (판단) => 단어가 kt 또는 samsung 또는 lg 또는 skt 인가?
# 검사하는 단어가 회사명이면 **로 바꾼다.
for c in company:
    text = text.replace(c, '**')

print(text)

# 아니면 그 단어는 그대로 리스트에 저장
# 분리된 단어들을 합침

# 결과 출력


print('')