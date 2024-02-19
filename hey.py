arr = [1,2,3,-3,1,1,1,4,2,-3]
K = 3
count = 0
for i in range(len(arr)):
    sum_arr = 0
    for j in range(i,len(arr)):
        sum_arr += arr[j]
        if sum_arr == K:
            count+=1
print(count)

