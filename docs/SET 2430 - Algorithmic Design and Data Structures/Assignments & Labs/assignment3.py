# Assignment 3

# Part A
def mystery(n):
    count = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            count += 1
    return count

# 1. Summation expression:
# Sum_{i=1 to n} (i) = 1 + 2 + 3 + ... + n

# 2. Closed-form formula:
# n * (n + 1) / 2  =  (n^2 + n) / 2

# 3. Big-O time complexity:
# O(n^2)


# Part B: Running Sum of 1D Array
def runningSum(nums):
    res = []
    current = 0
    for x in nums:
        current += x
        res.append(current)
    return res

# 2. Runtime expressed mathematically:
# Sum_{i=1 to n} (c) = c * n

# 3. Big-O time complexity:
# O(n)


if __name__ == '__main__':
    # test Part A
    print("Part A test:")
    print("mystery(4):", mystery(4))

    # test Part B
    print("\nPart B test:")
    sample = [1, 2, 3, 4]
    print("Input: ", sample)
    print("Output:", runningSum(sample))
