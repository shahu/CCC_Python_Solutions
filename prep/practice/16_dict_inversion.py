"""
Title: Invert Dictionary
Problem: Write invert_dict(d). Swap keys and values.
# If multiple keys have same value, store keys in a list.
# {'a': 1, 'b': 2, 'c': 1} -> {1: ['a', 'c'], 2: ['b']} (sorted lists for test)
"""

def invert_dict(arg1):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [({'a': 1, 'b': 2, 'c': 1}, {1: ['a', 'c'], 2: ['b']}), ({}, {})]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = invert_dict(*args)
        except Exception as e:
            print(f'❌ Error on input {args}: {e}')
            all_passed = False
            continue
        # Sort lists in dict values for comparison
        if isinstance(actual, dict):
            for k in actual:
                if isinstance(actual[k], list):
                    actual[k].sort()
        if actual != expected:
            print(f'❌ Failed for input {args}')
            print(f'   Expected: {expected}')
            print(f'   Got: {actual}')
            all_passed = False
    if all_passed:
        print('✅ All Tests Passed!')

if __name__ == '__main__':
    run_test()
