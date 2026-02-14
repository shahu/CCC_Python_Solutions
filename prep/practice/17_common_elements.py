"""
Title: Common Elements
Problem: Write common(l1, l2) to find elements common to both lists.
# Return sorted list of unique common elements.
"""

def common(arg1, arg2):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [([1, 2, 3], [2, 3, 4], [2, 3]), ([1, 2], [3, 4], [])]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = common(*args)
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
