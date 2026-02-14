"""
Title: CCC Logic: Auction
Problem: Simulate a silent auction. First line: N bids.
# Next N lines: Name, then Bid Amount (2 lines per bid).
# Output name of highest bidder. Tie breaks: first person wins.
# Input:
# 2
# Alice
# 10
# Bob
# 20
"""

def solve():
    # TODO: Write your code here
    pass

# --- Test Code ---
import sys
from io import StringIO

def run_test():
    test_input = """2
Alice
10
Bob
20"""
    expected_output = """Bob"""

    original_stdin = sys.stdin
    original_stdout = sys.stdout
    sys.stdin = StringIO(test_input)
    captured_output = StringIO()
    sys.stdout = captured_output

    try:
        solve()
    except Exception as e:
        sys.stdin = original_stdin
        sys.stdout = original_stdout
        print(f'❌ Error: {e}')
        return

    sys.stdin = original_stdin
    sys.stdout = original_stdout
    actual_output = captured_output.getvalue().strip()

    if actual_output == expected_output.strip():
        print('✅ Test Passed!')
    else:
        print('❌ Test Failed')
        print(f'Expected:\n{expected_output}')
        print(f'Got:\n{actual_output}')

if __name__ == '__main__':
    run_test()
