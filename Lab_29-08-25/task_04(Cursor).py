# Modified version - compute products instead of ratios
def compute_products(numbers):
    results = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            try:
                product = numbers[i] * (numbers[j] + numbers[i])
                results.append((i, j, product))
            except:
                print(f"Error: Cannot compute for indices {i}, {j}")
                results.append((i, j, None))
    return results

data = [2, 4, 6, 8, 10]
print(compute_products(data))
