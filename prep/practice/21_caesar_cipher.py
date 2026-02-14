"""
Title: Caesar Cipher Shift
Problem: Write encrypt(s, k) to shift lowercase letters by k.
# Wrap around 'z' to 'a'. Ignore non-letters.
# 'abc', 1 -> 'bcd'. 'z', 1 -> 'a'.
"""

def encrypt(arg1, arg2):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [('abc', 1, 'bcd'), ('xyz', 1, 'yza'), ('a b', 1, 'b c')]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = encrypt(*args)
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
