#function to print all the paths possible from 1,1 to n,m can only move down and right
grid = [[2,-2,-2,-2],[-2,2,2,-2],[2,2,2,-2]]
n = len(grid)
m = len(grid[0])

k = 4

count = grid[0][0]
for i in range(0,len(n)):
    for j in range(0,len(m)):
        