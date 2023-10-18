'''
    작성일 : 2023년 10월 18일
    작성자 : 컴퓨터공학부 202395034 한유진    
    설명 : 도시의 인구 자료에 대한 슬라이싱하기.
'''
population = ["Seoul", 9765, "Busan", 3441, "Incheon", 2954]

print("서울 인구", population[1])   #리스트에서 1번에 있는 값 출력
print("인천 인구", population[-1])  # 리스트에서 0번에 값 출력

cities = population[0::2]   #리스트 0번에서 2번까지
print("도시 리스트", cities)    #리스트 0번에서 2번까지의 값 출력
pops=population[1::2]       #리스트 1번부터 2씩 증가
print("인구의 합 : ", sum(pops))    #인구의 합 출력