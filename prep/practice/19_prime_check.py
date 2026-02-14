"""
Title: Prime Checker
Problem: Write is_prime(n) to return True if n is prime, else False.
# 1 is not prime.
"""

def is_prime(arg1):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [(2, True), (3, True), (4, False), (1, False), (17, True)]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = is_prime(*args)
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
