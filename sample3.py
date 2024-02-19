#function to print every subset of a set
k = 4
p = 1
nums = [1,2,3,4]

#function to find the number of elements divisible by k
def divisible_by_k(nums, k):
    count = 0
    for i in range(len(nums)):
        if(nums[i] % k == 0):
            count += 1
    return count


subsets = [[]]
result = []
# for num in nums:
#     n = len(subsets)

#     for i in range(n):
#         subset = list(subsets[i])
#         subset.append(num)
#         if(divisible_by_k(subset, p) <= k):
#             if (subset not in result):
#                 result.append(subset)
#         subsets.append(subset)

# print(len(subsets))
# print(result)


#function to print all the subarrays of a given array
def printSubArrays(arr, start, end):
    if end == len(arr):
        return
    elif start > end:
        return printSubArrays(arr, 0, end + 1)
    else:
        print(arr[start:end + 1])
        subset = arr[start:end + 1]
        if(divisible_by_k(subset, p) <= k):
            if (subset not in result):
              result.append(subset)
        return printSubArrays(arr, start + 1, end)

arr = [2,3,3,2,2]
printSubArrays(arr, 0, 0)
print(len(result))
