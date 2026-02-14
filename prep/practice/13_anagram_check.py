"""
Title: Anagram Check
Problem: Write a function is_anagram(s1, s2) that checks if s1 and s2 are anagrams (same chars in different order).
"""

def is_anagram(arg1, arg2):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [('listen', 'silent', True), ('hello', 'world', False)]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = is_anagram(*args)
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
