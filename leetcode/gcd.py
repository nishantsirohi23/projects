def hcnaive(x,y):
    if(y==0):
        return abs(x)
    else:
        return hcnaive(y,x%y)



a = [2,5,6,9,10]
temp = hcnaive(a[0],a[1])
for i in range(2,len(a)-1):
    temp = hcnaive(temp,a[i])

print(temp)

