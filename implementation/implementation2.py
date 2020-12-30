# 왕실의 나이트 실전 문제
"""
왕실의 정원은 8*8 좌표 평면, 그 중 특정한 한 칸에 나이트가 서 있다.
나이트는 가지의 경우로만 이동할 수 있다.
1. 수평으로 두 칸 이동 후 수직으로 한 칸 이동
2. 수직으로 두 칸 이동 후 수평으로 한 칸 이동
이처럼 8*8좌표 평면 상에서 나이트의 위치가 주어졌을때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.
- 입력 예시
a1
- 출력 예시
2
"""

# 현재 난이트의 위치 입력 받기
input_data = input()
row = int(input_data[1])
columns = int(ord(input_data[0])) - int(ord('a')) + 1 # ord는 ASCII code를 출력함

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# 8가지 방향에 대해 각 위치로 이동이 가능한지 확인
result = 0
for step in steps :
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_columns = columns + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_columns >= 1 and next_columns <= 8 : # 나이트는 정원 밖으로 나갈 수 없음
            result += 1

print(result)
