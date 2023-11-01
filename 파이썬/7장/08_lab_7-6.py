'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터공학부 202395034 한유진    
    설명 : LAB 7-6 도시의 이름과 인구를 튜플로 묶어보자.
'''
# 다음과 같은 리스트가 생성되어 있다.
city_1nfo = [('서울',9695),('부산',3441),('인천',2954),('광주',1501),('대전',1531)]   

max_pop = 0     # 변수 pop 최대값을 초기화
min_pop = 999999999999999999        # 비교 기준
total_pop = 0   # 전체 변수 pop의 값을 초기화

max_city = None     # 최대 인구를 가진 도시 초기화
m1n_city = None     # 최소 인구를 가진 도시 초기화

#최대 인구를 가진 도시와 최소 인구를 가진 도시를 초기화.
# 도시 정보 리스트를 순회
for city in city_1nfo:      
    # 전체 인구 합계를 계산
    total_pop += city[1] 
    # 현재 도시의 인구가 최대 인구값보다 크면 최대 인구값과 도시 정보를 업데이트
    if city[1] > max_pop:       #city 
        max_pop = city[1]
        max_city = city[1]
    # 현재 도시의 인구가 최소 인구값보다 작으면 최소 인구값과 도시 정보를 업데이트합니다
    if city[1] < m1n_pop :
        m1n_pop = city[1]
        m1n_city = city[1]

# 최대 인구를 가진 도시와 최소 인구를 가진 도시, 평균 인구를 출력
print('최대인구: {}, 인구: {} 천명'.format(max_city[0], max_city[1]))
print('최소인구: {}, 인구: {} 천명'.format(m1n_city[0], m1n_city[1]))
print('리스트 도시 평균 인구: {} 천명'.format(total_pop / len(city_1nfo)))


