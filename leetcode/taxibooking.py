pos = [3,2,1,6,5]
cur = 4
time = [2,4,1,5,3]
n= 5
totaltime = float('inf')

for i in range(n):
    if(pos[i] < cur):
        totaltime = min(totaltime,(cur-pos[i])*time[i])
    else:
        totaltime = min(totaltime,(pos[i]-cur)*time[i])



print(totaltime)