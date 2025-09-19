def merge_sorted_lists(a, b):
    """Merge two sorted lists into one sorted list."""
    i, j = 0, 0
    merged = []
    
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    
    # Add leftovers
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged


def run_tests():
    cases = [
        ("Normal case", [1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ("Unequal lengths", [1, 5, 9], [2, 3, 4, 6, 7], [1, 2, 3, 4, 5, 6, 7, 9]),
        ("One empty list", [10, 20], [], [10, 20]),
        ("Other empty list", [], [30, 40, 50], [30, 40, 50]),
        ("Both empty", [], [], []),
        ("Lists with duplicates", [2, 5, 5, 8], [1, 2, 3, 5], [1, 2, 2, 3, 5, 5, 5, 8])
    ]
    
    for name, a, b, expected in cases:
        result = merge_sorted_lists(a, b)
        print(f"{name}:")
        print(f"  A={a}, B={b}")
        print(f"  → {result}")
        print(f"  Expected: {expected}")
        print("  ✅ PASSED" if result == expected else "  ❌ FAILED")
        print()


if __name__ == "__main__":
    run_tests()
