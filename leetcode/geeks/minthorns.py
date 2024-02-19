n = 5
m = 5
Geek = [2,3]
Geekina = [2, 4]

#function to check if two geek and geekina are adjacent
def isAdjacent(geek, geekina):
    if (geek[0] == geekina[0] and (geek[1] == geekina[1] + 1 or geek[1] == geekina[1] - 1)):
        return True
    elif (geek[1] == geekina[1] and (geek[0] == geekina[0] + 1 or geek[0] == geekina[0] - 1)):
        return True
    else:
        return False
    
#function to check how many moves are possible for geek in up down left right direction
def checkMoves(geek):
    moves = 0
    if (geek[0] - 1 >= 1):
        moves += 1
    if (geek[0] + 1 <= n):
        moves += 1
    if (geek[1] - 1 >= 1):
        moves += 1
    if (geek[1] + 1 <= m):
        moves += 1
    return moves

print(checkMoves(Geek))
    
