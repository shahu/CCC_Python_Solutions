"""
Title: Find Duplicates
Problem: Write a function find_dups(nums) that returns a sorted list of all elements that appear more than once.
"""

def find_dups(arg1):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [([1, 2, 3, 2, 1, 4], [1, 2]), ([1, 2, 3], [])]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = find_dups(*args)
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
