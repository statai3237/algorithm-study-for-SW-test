# 게임 개발 실전 문제 (-> 전형적인 '시뮬레이션' 문제) ## 다시 문제 읽고, 공부하기 ! 
"""
개발자는 게임 캐릭터가 맵 안에서 움직이는 시스템을 개발 중임
캐릭터가 있는 장소는 1X1 크기의 정사각형으로 이뤄진 NXM 크기의 직사각형으로, 각각의 칸은 육지 또는 바다임
캐릭터는 동서남북 중 한 곳을 바라봄
맵의 각 칸은 (A,B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수임
캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없음
캐릭터는 아래의 매뉴얼을 따름
1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정함
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진함
3. 만약 네 방향이 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
   단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

개발자는 위 과정을 반복적으로 수행하면서 캐릭터의 움직임에 이상이 있는지 테스트하려고 함
매뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.

"""

# N,M을 공백으로 구분하여 입력받기
n,m = map(int,input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화 (리스트 컴프리헨션 이라고 함)
d = [[0] *m for _ in range(n)] # ex. n이 3인 경우 [0,0,0],[0,0,0],[0,0,0]
# 현재 캐릭터의 X좌표, Y좌표, 방향을 입력 받기
x,y,direction = map(int,input().split())
d[x][y] = 1 # 현재 좌표 방문 처리
# 전체 맵 정보를 입력 받기
array = []
for i in range(n) :
    array.append(list(map(int,input().split())))

# 헷갈리면 방향은 무조건 먼저 손으로 쓰기
# 동,서,남,북 방향 정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽으로 회전
def turn_left() :
    global direction
    direction -= 1
    if direction == -1 :
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True :
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0 :
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else :
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4 :
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있으면 뒤로 이동
        if array[nx][ny] == 0 :
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else :
            break
        turn_time = 0

print(count)
