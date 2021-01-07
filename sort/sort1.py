# 위에서 아래로 
# 하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 있다. 이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다. 수열을 내림차순으로 정렬하는 프로그램을 ㅁ나드시오. 
n = int(input())

# N개의 정수를 입력받아 리스트에 저장 
array = []
for i in range(n) :
    array.append(int(input()))
    
# python  기본 정렬 라이브러리를 이용하여 정렬
array = sorted(array,reverse=True)
# 출력 예시  : 27 15 12
for i in array :
    print(i,end=' ')
