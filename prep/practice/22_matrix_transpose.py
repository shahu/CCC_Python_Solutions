"""
Title: Matrix Transpose
Problem: Write transpose(grid). Rows become columns.
# [[1, 2], [3, 4]] -> [[1, 3], [2, 4]]
"""

def transpose(arg1):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [([[1, 2], [3, 4]], [[1, 3], [2, 4]]), ([[1]], [[1]])]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = transpose(*args)
        except Exception as e:
            print(f'❌ Error on input {args}: {e}')
            all_passed = False
            continue
        if actual != expected:
            print(f'❌ Failed for input {args}')
            print(f'   Expected: {expected}')
            print(f'   Got: {actual}')
            all_passed = False
    if all_passed:
        print('✅ All Tests Passed!')

if __name__ == '__main__':
    run_test()
