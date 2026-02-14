"""
Title: Grid Row Sum
Problem: Write a function max_row_sum(grid) that takes a 2D list (list of lists)
# and returns the maximum sum of any single row.
"""

def max_row_sum(arg1):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [([[1, 2, 3], [10, 1, 1], [5, 5, 5]], 15), ([[1]], 1)]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = max_row_sum(*args)
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
