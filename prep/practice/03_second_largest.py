"""
Title: Second Largest Value
Problem: Write a function second_max(nums) that returns the second largest distinct number in a list.
# If fewer than 2 distinct numbers exist, return None.
"""

def second_max(arg1):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [([10, 20, 4, 45, 99], 45), ([5, 5, 5], None), ([1], None), ([1, 2], 1)]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = second_max(*args)
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
