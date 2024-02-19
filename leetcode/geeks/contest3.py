def is_beautiful_string(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    odd_count = sum(1 for val in freq.values() if val % 2 != 0)
    return odd_count <= 1


def count_beautiful_string_pairs(box):
    n = len(box)
    count = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            concatenated_string = box[i] + box[j]
            if is_beautiful_string(concatenated_string):
                count += 1
    
    return count


# Test caseb
box = ["aaaa","abba","ccc","caa","cbba","acaac","bcb"]
result = count_beautiful_string_pairs(box)
print("Number of beautiful string pairs:", result)
