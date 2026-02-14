"""
Title: Prefix Sum Array
Problem: Write a function prefix_sum(nums) that returns a new list where index i
# contains the sum of nums[0]...nums[i].
# [1, 2, 3] -> [1, 3, 6]
"""

def prefix_sum(arg1):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [([1, 2, 3], [1, 3, 6]), ([-1, 1], [-1, 0])]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = prefix_sum(*args)
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
