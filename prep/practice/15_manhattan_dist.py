"""
Title: Manhattan Distance
Problem: Write a function distance(p1, p2) where p1 and p2 are (x, y) tuples.
# Calculate |x1 - x2| + |y1 - y2|.
"""

def distance(arg1):
    # TODO: Write your code here
    return None

# --- Test Code ---
def run_test():
    test_cases = [(((0, 0), (3, 4)), 7), (((1, 1), (1, 1)), 0)]
    all_passed = True

    for *args, expected in test_cases:
        try:
            actual = distance(*args)
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
