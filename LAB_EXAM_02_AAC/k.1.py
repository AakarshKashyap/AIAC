def rotate_matrix_in_place(matrix):
    n = len(matrix)
    if n == 0 or n != len(matrix[0]): return
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix: row.reverse()

def run_tests():
    tests = {
        "3x3": ([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),
        "2x2": ([[1,2],[3,4]], [[3,1],[4,2]]),
        "1x1": ([[5]], [[5]]),
    }
    for name, (inp, exp) in tests.items():
        mat = [r[:] for r in inp]
        rotate_matrix_in_place(mat)
        print(f"Test case: {name}")
        print(f"Input: {inp}")
        print(f"Result: {mat}")
        print(f"Expected: {exp}")
        print("✅ Test Passed!" if mat == exp else "❌ Test Failed.")
        print("-" * 20)

run_tests()