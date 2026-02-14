"""
Title: Missing Number
Problem: Given a list containing n distinct numbers taken from 0, 1, 2, ..., n.
# Find the one that is missing from the list.
# [3, 0, 1] (n=3) -> missing 2.
"""

def missing_number(arg1):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [([3, 0, 1], 2), ([0, 1], 2), ([0], 1)]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = missing_number(*args)
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
