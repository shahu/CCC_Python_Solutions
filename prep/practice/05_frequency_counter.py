"""
Title: Character Frequency
Problem: Write a function char_freq(s) that returns a dictionary with the count of each character.
# 'aba' -> {'a': 2, 'b': 1}
"""

def char_freq(arg1):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [('aba', {'a': 2, 'b': 1}), ('hello', {'h': 1, 'e': 1, 'l': 2, 'o': 1})]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = char_freq(*args)
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
