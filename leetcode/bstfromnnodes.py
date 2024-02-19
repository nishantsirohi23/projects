
#function to fin d factorial of a number
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    

print(fact(5))


n = int(input("Enter the number of nodes: "))
upper = fact(2*n)
lower = fact(n+1)*fact(n)

print(upper//lower)