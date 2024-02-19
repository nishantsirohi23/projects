def minimum_toys(price, magical_price, M):
    total_cost = sum(price)
    magic_count = 0

    toys = sorted(enumerate(magical_price), key=lambda x: x[1], reverse=True)

    for toy in toys:
        if total_cost <= M:
            return toy[0] + 1
        total_cost -= (price[toy[0]] - toy[1])
        magic_count += 1

    if total_cost <= M:
        return magic_count

    return -1


# Test case 1
price1 = [2, 4, 6, 2, 4]
magical_price1 = [1, 2, 5, 1, 3]
M1 = 13

result1 = minimum_toys(price1, magical_price1, M1)
print("Minimum number of toys to buy:", result1)

# Test case 2
price2 = [4, 3, 4]
magical_price2 = [2, 2, 3]
M2 = 6

result2 = minimum_toys(price2, magical_price2, M2)
print("Minimum number of toys to buy:", result2)
