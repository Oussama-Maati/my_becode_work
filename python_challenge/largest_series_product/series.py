def largest_product(strings, length_s):
    if length_s > len(strings) or length_s < 0:
        raise ValueError("wrong input")

    biggest_pro = 0
    nums = [int(x) for x in strings]

    for i in range(len(nums) - length_s+1):
        prod = 1
        for j in range(length_s):
            prod *= nums[i + j]

        biggest_pro = prod if biggest_pro < prod else biggest_pro

    return biggest_pro
