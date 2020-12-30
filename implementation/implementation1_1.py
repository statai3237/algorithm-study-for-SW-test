# 상하좌우 예제 문제 -> simulation문제로 분류됨
"""
여행가 A가 N*N 크기의 정사각형 공간 위에 서 있다.
이 공간의 1*1 크기의 정사각형으로 나누어져 있다. 가장 위 좌표는 (1,1), 가장 오른쪽 아래 좌표는 (N,N)
L,R,U,D : 왼,오,위,아래
계획서에 R->R->R->U->D->D 라고 할 때, 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오.
- 입력 예시
5
R R R U D D
- 출력 예시
3 4
"""
# N을 입력 받기
n = int(input()) # 정수를 입력으로 받을땐 int()안에 넣는 거 잊지 말기
x,y = 1,1 # 가장 위 좌표가 1,1이므로
plans = input().split()

# L,R,U,D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']
## dx,dy에 대한 설명을 덧붙이자면, L일때 좌표가 (0,-1), R일때 (0,+1), U일때 (-1,0), D일때 (+1,0)이어야 하니까 dx,dy를 저렇게 설정하여 좌표값으로 사용할 수 있도록 함.

# 이동 계획을 하나씩 확인
for plan in plans :
    # 이동 후 좌표 구하기
    for i in range(len(move_types)) :
        if plan == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나는 경우는 무시
    if nx <1 or ny <1 or nx >n or ny >n :
            continue
    x,y = nx, ny

print(x,y)
