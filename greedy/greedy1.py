"""
숫자 카드 게임은 여러 개의 숫자 카드 중 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
단, 게임의 룰을 지키며 카드를 뽑아야 함
룰 1. 숫자가 쓰인 카드들이 N*M 형태로 놓여있음. 이때 N은 행의 개수, M은 열의 개수를 의미함
룰 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택
룰 3. 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 함
룰 4. 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 함
"""
n,m = map(int,input().split())

answer = 0
row_min = []

for j in range(n):
        row = list(map(int,input().split()))
        row_min.append(min(row))

answer = max(row_min)

print(answer)
