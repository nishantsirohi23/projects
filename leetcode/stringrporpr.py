A = [7,3,12,17,21,18]
cost = 0


#function to return the adjacent pair of elements that have the smallest sum of any two elements and the index of the pair 
def adjacentElementsSumIndex(inputArray):
    #initialize the min sum to the first two elements
    min_sum = inputArray[0] + inputArray[1]
    #initialize the index to the first pair
    index = 0
    #loop through the array
    for i in range(len(inputArray)-1):
        #compare the current sum to the min sum
        if inputArray[i] + inputArray[i+1] < min_sum:
            #if the current sum is less than the min sum, set the min sum to the current sum
            min_sum = inputArray[i] + inputArray[i+1]
            #set the index to the current index
            index = i 


    
    return min_sum , index
if len(A) == 1:
    cost = 0
    exit()
if len(A) == 2:
    cost = A[0] + A[1]
    exit()


for i in range(len(A)-1):
    if(len(A) == 1):
        break
    if(len(A) == 2):
        cost += A[0] + A[1]
        break
    else:
        val ,index = adjacentElementsSumIndex(A)
        del A[index]
        del A[index]
        cost += val
        A.insert(index,val)
        print(cost,A)
        
        




print(cost)