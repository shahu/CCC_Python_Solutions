"""
Title: Rotate List
Problem: Write a function rotate(nums, k) that rotates a list to the right by k steps.
# [1, 2, 3, 4, 5], k=2 -> [4, 5, 1, 2, 3]
"""

def rotate(arg1):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [(([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3]), (([1, 2], 3), [2, 1])]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = rotate(*args)
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
