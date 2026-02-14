"""
Title: String Cleaner
Problem: Write a function clean_string(s) that removes all non-alphanumeric characters
# and converts the string to lowercase.
# Example: 'Hello, World!' -> 'helloworld'
"""

def clean_string(arg1):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [('Hello, World!', 'helloworld'), ('Python 3.10', 'python310'), ('###', '')]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = clean_string(*args)
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
