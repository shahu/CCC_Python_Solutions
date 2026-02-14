"""
Title: Flatten 2D List
Problem: Write a function flatten(grid) that converts a 2D list into a 1D list.
# [[1, 2], [3]] -> [1, 2, 3]
"""

def flatten(arg1):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [([[1, 2], [3], []], [1, 2, 3]), ([[]], [])]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = flatten(*args)
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
