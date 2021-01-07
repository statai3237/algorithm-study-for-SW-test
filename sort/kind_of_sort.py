# 선택 정렬 
array = [7,5,9,0,3,1,6,2,4,8]
print(array)
for i in range(len(array)) :
    min_index = i
    for j in range(i+1,len(array)) : # 1~9 
        if array[min_index] > array[j] :
            min_index = j
    array[i],array[min_index] = array[min_index],array[i] #  swape : 특정한 리스트가 주어졌을때 두 변수의 위치를 변경하는 작업

print(array)


# 삽입 정렬
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(array)) : # 0번째(즉, 첫번째) 인덱스에 있는 수는 이미 정렬이 된 것이라고 판단함
    for j in range(i,0,-1) : # index i부터 1까지 감소하며 반복하는 문법   ## range(start,end,step)
        if array[j] < array[j-1] : # 한칸씩 왼쪽으로 이동 
            array[j],array[j-1] = array[j-1],array[j] 
        else : # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤 
            break
print(array)

# 퀵 정렬
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array) :
    if len(array) <= 1 :
        return array
    
    pivot = array[0] # hoare partition 일때 리스트에서 가장 왼쪽이 피벗이 됨
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side) # recursive function\

print(quick_sort(array))

# 계수 정렬
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2] # 모든 원수의 값이 0보다 크거나 같다고 가정
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0]*(max(array)+1)

for i in range(len(array)) :
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가 

for i in range(len(count)) :
    for j in range(count[i]) :
        print(i,end=' ')
