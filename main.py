list = [4, 2, 6, 2, 13]
max1 = list[0]
max2 = list[0]
for num in list:
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num
pair_sum = max1 + max2
print(pair_sum)
# 19