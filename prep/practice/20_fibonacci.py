"""
Title: Fibonacci List
Problem: Write fib(n) to return a list of the first n Fibonacci numbers.
# 0, 1, 1, 2, 3, 5...
"""

def fib(arg1):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [(5, [0, 1, 1, 2, 3]), (1, [0]), (0, [])]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = fib(*args)
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
