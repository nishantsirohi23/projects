

from copy import copy
grid = [[1,2,3],[2,5,7],[3,5,1]]


#assiggn infinty to a variable
inf = float('inf')

#add infinty around the grid
grid = [[inf] + row + [inf] for row in grid]

#add infinty to the top and bottom of the grid
grid = [[inf] * len(grid[0])] + grid + [[inf] * len(grid[0])]

#print(grid[2][3])

level = 0



def dfs(i,j,q,root):
    #print("i,j",i,j)
    global level
    if(root[i][j] > q):
        return 0
    elif(root[i][j] == q):
        return 0
    else:
        level += 1
        #print("value at",grid[i][j])
        root[i][j] = inf
        #print("value before",grid[i][j])
        dfs(i+1,j,q,root)
        dfs(i-1,j,q,root)
        dfs(i,j-1,q,root)
        dfs(i,j+1,q,root)
        return level



mylist = []

query = [5,6,2]
for i in range(len(query)):
    grid = copy(grid)
    print(grid)
    mylist.append(dfs(1,1,query[i]))
root = copy(grid)
print(dfs(1,1,1,root))

print(grid)

   



