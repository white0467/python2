'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터공학부 202395034 한유진    
    설명 : 한번 생성하면 그 값을 고칠 수 없는 자료형 : 튜플
'''
# 리스트 생성
color_list=['aqua','sky','blue','light_blue']
# 튜플 생성
color =('aqua','sky','blue','light_blue')

# 튜플 출력
print(f"color : {color}")

# color에 black 추가하기
# AttributeError: 'tuple' object has no attribute 'append'
# 튜플은 추가, 삭제가 안된다.
# color.append('black')

# 인덱싱과 슬라이싱은 문자열이나 리스트와 동일하게 동작한다.
print('color 튜플 : ', color)
print('color 튜플 중 2, 3, 4 번은? ', color[1:4])   # 1번부터 4번 전까지
print('color 튜플 중 1, 2, 3 번은? ', color[:3])    # 3번 전까지
print('color 튜플 중 3번 ~ 끝은? ', color[2:])      # 2 초과에서 끝까지
print('color 튜플 중 1, 2, 3 번은? ', color[::2])   # 홀수로 출력
print('color 튜플을 거꾸로 출력? ', color[::-1])    # 거꾸로 출력

# 튜플 까지의 결합 => + 연산자. 반복 => * 연산자.
colors = color + color
print('color 튜플 : ', colors)
print('color 튜플을 10번 반복 : ', color * 10)