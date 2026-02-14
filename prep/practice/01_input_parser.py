"""
Title: CCC Input Parser
Problem: Read an integer N from the first line.
# Then read N integers from the *next* N lines.
# Return the sum of these integers.
# Input format:
# 3
# 10
# 20
# 30
"""

def solve():
    # TODO: Write your code here
    pass

# --- Test Code ---
import sys
from io import StringIO

def run_test():
    test_input = """3
10
20
30"""
    expected_output = """60"""

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
