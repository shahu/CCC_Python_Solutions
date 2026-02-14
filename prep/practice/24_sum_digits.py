"""
Title: Sum of Digits
Problem: Write sum_digits(n). 123 -> 6.
"""

def sum_digits(arg1):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [(123, 6), (0, 0), (99, 18)]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = sum_digits(*args)
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
