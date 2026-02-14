"""
CCC 2021 Junior - Problem J5/S2 - Answer
============================================================

Modern Art
Given MxN canvas (initially all black), K operations of flipping row R or column C.
Count gold cells after all operations.

============================================================
"""

import os
import sys
from io import StringIO

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2021CCCJuniorTestData", "j5")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    Solution for CCC 2021 Junior Problem J5/S2 - Modern Art
    Time: O(K + M*N) where K is number of operations
    Space: O(M + N) - only track which rows/columns are flipped odd times
    
    Key insight: We don't need to simulate the entire grid.
    Just track row_flip[i] = number of times row i is flipped
    and col_flip[j] = number of times col j is flipped
    
    Cell (i,j) is gold if: (row_flip[i] + col_flip[j]) % 2 == 1
    """
    M = int(input())
    N = int(input())
    K = int(input())
    
    row_flip = [0] * M
    col_flip = [0] * N
    
    for _ in range(K):
        op = input().split()
        if op[0] == 'R':
            row = int(op[1]) - 1  # Convert to 0-indexed
            row_flip[row] += 1
        else:  # op[0] == 'C'
            col = int(op[1]) - 1  # Convert to 0-indexed
            col_flip[col] += 1
    
    # Count gold cells
    # Cell (i,j) is gold if row_flip[i] + col_flip[j] is odd
    gold = 0
    odd_rows = sum(1 for r in row_flip if r % 2 == 1)
    even_rows = M - odd_rows
    odd_cols = sum(1 for c in col_flip if c % 2 == 1)
    even_cols = N - odd_cols
    
    # Gold cells = (odd row + even col) + (even row + odd col)
    gold = odd_rows * even_cols + even_rows * odd_cols
    
    print(gold)


def run_tests():
    """Run all test cases from the test data directory"""
    test_cases = []
    
    if os.path.exists(TEST_DATA_DIR):
        for filename in sorted(os.listdir(TEST_DATA_DIR)):
            if filename.endswith(".in"):
                base_name = filename[:-3]
                in_file = os.path.join(TEST_DATA_DIR, filename)
                out_file = os.path.join(TEST_DATA_DIR, base_name + ".out")
                
                if os.path.exists(out_file):
                    with open(in_file, "r") as f:
                        input_data = f.read()
                    with open(out_file, "r") as f:
                        expected_output = f.read().strip()
                    test_cases.append({"name": base_name, "input": input_data, "expected": expected_output})
    
    if not test_cases:
        print("No test cases found!")
        return False
    
    print(f"\nRunning {len(test_cases)} test cases...")
    print("="*60)
    
    passed = 0
    failed = 0
    
    for tc in test_cases:
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        
        capture = StringIO()
        sys.stdin = StringIO(tc["input"])
        sys.stdout = capture
        
        try:
            solve()
            output = capture.getvalue().strip()
            expected = tc["expected"].strip()
            
            sys.stdin = old_stdin
            sys.stdout = old_stdout
            
            if output == expected:
                print(f"✓ {tc['name']}: PASSED")
                passed += 1
            else:
                print(f"✗ {tc['name']}: FAILED")
                print(f"  Expected: {repr(expected)}")
                print(f"  Got: {repr(output)}")
                failed += 1
        except Exception as e:
            sys.stdin = old_stdin
            sys.stdout = old_stdout
            print(f"✗ {tc['name']}: ERROR - {e}")
            import traceback
            traceback.print_exc()
            failed += 1
    
    print("="*60)
    print(f"Results: {passed} passed, {failed} failed")
    print("="*60)
    return failed == 0


if __name__ == "__main__":
    run_tests()
