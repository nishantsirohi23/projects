#Prime Pairs With Target Sum

n = 1000000
output = []
prime = [True for i in range(n+1)]
p = 2

while (p * p <= n):
    if (prime[p] == True):
        for i in range(p * p, n+1, p):
            prime[i] = False
    p += 1

for p in range(2, n):
    if prime[p]:
        output.append(p)


def prime_pairs_with_target_sum(arr, target):
    output = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                output.append((arr[i], arr[j]))
    return output

print(prime_pairs_with_target_sum(output, 1000000))