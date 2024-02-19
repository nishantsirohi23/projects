def count_ones(x):
    return bin(x).count('1')
def countSetBits(n):
    # write your code here
    # Return an integer denoting the answer to the required problem 
    total = 0
    for i in range(1,n+1):
        total += count_ones(i)

    ans = total % 1000000007
    return ans
    pass



print(countSetBits(5))