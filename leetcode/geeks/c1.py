def maximum_good_length(A):
    N = len(A)     # Number of rows
    M = len(A[0])  # Number of columns

    low = 1
    high = min(N, M)
    max_good_length = 0

    def isGoodLength(L):
        for i in range(N - L + 1):
            for j in range(M - L + 1):
                if all(A[x][y] >= L for x in range(i, i + L) for y in range(j, j + L)):
                    return True
        return False

    while low <= high:
        mid = (low + high) // 2
        if isGoodLength(mid):
            max_good_length = mid
            low = mid + 1
        else:
            high = mid - 1

    return max_good_length

# Test case
A = [
    [2, 2, 3, 4],
    [3, 4, 5, 6],
    [4, 5, 6, 7]
]

result = maximum_good_length(A)
print("Maximum good length:", result)
