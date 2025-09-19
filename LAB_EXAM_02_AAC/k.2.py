def merge_sorted_lists(list_a, list_b):
    result = []
    i = j = 0
    while i < len(list_a) and j < len(list_b):
        if list_a[i] <= list_b[j]:
            result.append(list_a[i])
            i += 1
        else:
            result.append(list_b[j])
            j += 1
    while i < len(list_a):
        result.append(list_a[i])
        i += 1
    while j < len(list_b):
        result.append(list_b[j])
        j += 1
    return result
def run_tests():
    tests = [("Normal case", [1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
            ("Unequal lengths", [1, 5, 9], [2, 3, 4, 6, 7], [1, 2, 3, 4, 5, 6, 7, 9]),
            ("One empty list", [10, 20], [], [10, 20]),
            ("Other empty list", [], [30, 40, 50], [30, 40, 50]),
            ("Both empty", [], [], []),
            ("Lists with duplicates", [2, 5, 5, 8], [1, 2, 3, 5], [1, 2, 2, 3, 5, 5, 5, 8])]
    for name, a, b, expected in tests:
        result = merge_sorted_lists(a, b)
        print(f"Test: {name}")
        print(f"  Input: A={a}, B={b}")
        print(f"  Result: {result}")
        print(f"  Expected: {expected}")
        print("  Status: ✅ PASSED" if result == expected else "  Status: ❌ FAILED")
        print("-" * 30)
if __name__ == "__main__":
    run_tests()
