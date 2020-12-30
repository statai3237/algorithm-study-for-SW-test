# 시각 예제 문제 -> 완전 탐색 유형으로 분류됨
"""
정수 N이 입력되면 00시 00분 00부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
예를 들어, 1을 입력했을 때 1시 59분 59초까지의 시간 중 3이 하나라도 포함되어 있으면 세야 한다.
- 입력 예시
5
- 출력 예시
11475
다음 소스코드는 매 시각을 문자열로 바꾼 다음 문자열에 3이 포함됐는지 검사함
다시 말해, 00시 00분 00초부터 N시 59분 59초까지 1초씩 늘리며 시,분,초를 문자열 자료형으로 변환하여 합침.
ex) 03시 20분 35초일 때를 확인한다면, 이를 '032035'로 만들어서 '3'이 '032035'에 포함되어 있는지를 체크하는 방식을 이용하는 것임.
"""

# 시각 H를 입력으로 받기
h = int(input())

count = 0
for i in range(h+1) : # h가 아니라 h+1
    for j in range(60) :
        for k in range(60) :
            # 매 시각 안에 3이 포함되어 있으면 카운트 증가
            if '3' in str(i) + str(j) + str(k) :
                count += 1

print(count)


