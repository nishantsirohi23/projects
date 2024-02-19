def maxSubarraySum(nums, k):
    max_sum = float('-inf')  # Initialize maximum sum as negative infinity
    current_sum = 0  # Initialize current sum
    start = 0  # Initialize the start index of the window

    for end in range(len(nums)):
        current_sum += nums[end]  # Add the current element to the window

        # If the window size is greater than k, subtract the leftmost element
        if end >= k - 1:
            max_sum = max(max_sum, current_sum)  # Update the maximum sum
            current_sum -= nums[start]  # Remove the leftmost element
            start += 1  # Move the window one step to the right

    return max_sum

# Example usage:
nums = [1,12,-5,-6,50,3]
k = 4
result = maxSubarraySum(nums, k)
print(result)  # Output should be 19 (the maximum sum subarray is [4, 2, 10, 2])
