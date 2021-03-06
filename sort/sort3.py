# 두 배열의 원소 교체 
# 두 개의 배열 A,B를 가지고 있을때 각 배열은 N개의 원소로 구성되어 있음 (배열의 원소는 모두 자연수).
# 최대 K번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말함. 
# 이 작업의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것임. 
# N,K, 그리고 배열 A,B의 정보가 주어졌을때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하시오. 
 
n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort() # 배열 A는 오름차순 정렬 
b.sort(reverse=True) # 배열 B는 내림차순 정렬 수행 

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k) :
    if a[i] < b[i] : # A의 원소가 B의 원소보다 작을 경우
        # 두 원소를 교체 
        a[i],b[i] = b[i],a[i]
    else :
        break
print(sum(a))
