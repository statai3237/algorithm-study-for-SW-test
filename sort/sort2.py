# 성적이 낮은 순서로 학생 출력하기 
# N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다. 각 학생의 이름과 성적 정보가 주어졌을때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오. 
n = int(input())

array = []
for i in range(n) :
    input_data = input().split()
    array.append([input_data[0],int(input_data[1])])

# key를 이용하여 점수를 기준으로 정렬 
array = sorted(array, key = lambda student : student[1]) # 비교함수는 lambda로 해도 되고, 별도로 정의해도 됨, 비교할 아이템의 요소가 복수 개일 경우, 튜플로 그 순서를 내보내주면 됨. 

# 정렬이 수행된 결과를 출력 
for student in array :
    print(student[0],end = ' ')
