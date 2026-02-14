"""
Title: Valid Parentheses
Problem: Write a function is_valid(s) that checks if a string of '(' and ')' is balanced.
# '(()())' -> True, '(()' -> False, ')(' -> False.
"""

def is_valid(arg1):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [('(()())', True), ('(()', False), (')(', False), ('', True)]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = is_valid(*args)
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
