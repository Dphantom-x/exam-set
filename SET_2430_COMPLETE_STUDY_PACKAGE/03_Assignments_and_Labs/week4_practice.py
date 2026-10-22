# SET 2430 - Week 4 Practice Problems

# Practice 2: Different Solutions, Different Big-O (1 + 2 + ... + n)

# Approach 1: Loop
def sum_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
# Time Complexity: O(n) - loop runs n times with 1 addition per step


# Approach 2: Formula
def sum_formula(n):
    return n * (n + 1) // 2
# Time Complexity: O(1) - single arithmetic calculation regardless of n


# Slide Practice 1: Count occurrences of x in sorted array
def count_occurrences(arr, x):
    # Linear scan: O(n)
    count = 0
    for val in arr:
        if val == x:
            count += 1
    return count

def count_occurrences_fast(arr, x):
    # Binary search approach: O(log n)
    import bisect
    left = bisect.bisect_left(arr, x)
    right = bisect.bisect_right(arr, x)
    return right - left


# Slide Practice 2: Print all pairs (i, j) where 0 <= i < j < n using recursion
def print_pairs(n, i=0, j=1):
    if i >= n - 1:
        return
    if j >= n:
        print_pairs(n, i + 1, i + 2)
        return
    print((i, j))
    print_pairs(n, i, j + 1)


if __name__ == '__main__':
    print("--- Practice 2 (Sum 1 to n) ---")
    n = 10
    print(f"sum_loop({n}):", sum_loop(n))
    print(f"sum_formula({n}):", sum_formula(n))

    print("\n--- Slide Practice 1 (Count x) ---")
    test_arr = [1, 2, 2, 2, 3, 4]
    target = 2
    print(f"Count of {target} in {test_arr}:", count_occurrences(test_arr, target))
    print(f"Fast count (binary search):", count_occurrences_fast(test_arr, target))

    print("\n--- Slide Practice 2 (Pairs with n=4) ---")
    print_pairs(4)
