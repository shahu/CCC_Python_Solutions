"""
Title: Longest Word
Problem: Write longest_word(sentence). Return the longest word.
# If tie, return the first one.
"""

def longest_word(arg1):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [('The quick brown fox', 'quick'), ('a bb ccc', 'ccc')]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = longest_word(*args)
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
