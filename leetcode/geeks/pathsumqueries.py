#fincd the number of path form 1,1 to n,m can only move down and right
#check if there exists a path from 1,1 to n,m can only move down and right with exactly k sum
grid = [[2,-2,-2,-2],[-2,2,2,-2],[2,2,2,-2]]
n = len(grid)
m = len(grid[0])
k  = 4
def path(grid,n,m,k):
    if n == 1 and m == 1:
        if k == grid[n-1][m-1]:
            return True
        else:
            return False
    elif n == 1:
        return path(grid,n,m-1,k-grid[n-1][m-1])
    elif m == 1:
        return path(grid,n-1,m,k-grid[n-1][m-1])
    else:
        return path(grid,n-1,m,k-grid[n-1][m-1]) or path(grid,n,m-1,k-grid[n-1][m-1])
    
print(path(grid,n,m,k))


query  =[4,5,8,0]
result = []

for i in query:
    result.append(path(grid,n,m,i))
print(result)



