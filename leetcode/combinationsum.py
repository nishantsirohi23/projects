candidates = [2,3,6,7]
target = 7

#dfs solution
def combinationSum(candidates, target):
    result = []
    dfs(candidates, target, 0, [], result)
    return result

def dfs(candidates, target, index, path, result):
    if target < 0:
        return
    if target == 0:
        result.append(path)
        return
    for i in range(index, len(candidates)):
        print(path+[candidates[i]])
        print(candidates[i])
        dfs(candidates, target-candidates[i], i, path+[candidates[i]], result)
    

print(combinationSum(candidates, target))