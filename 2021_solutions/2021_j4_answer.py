"""
CCC 2021 Junior - Problem J4 - Answer
============================================================

Arranging Books
Arrange books so all Large (L) on left, Medium (M) in middle, Small (S) on right.
Find minimum number of swaps needed.

============================================================
"""

import os
import sys
from io import StringIO

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2021CCCJuniorTestData", "j4")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    Solution for CCC 2021 Junior Problem J4 - Arranging Books
    Time: O(N), Space: O(N)
    
    Count misplaced books in each section and compute minimum swaps
    """
    books = list(input().strip())
    n = len(books)
    
    count_L = books.count('L')
    count_M = books.count('M')
    
    # Section boundaries (0-indexed):
    # L-section: [0, count_L)
    # M-section: [count_L, count_L + count_M)
    # S-section: [count_L + count_M, n)
    
    # Count books in wrong sections
    L_in_M = 0  # L books in M-section
    L_in_S = 0  # L books in S-section
    M_in_L = 0  # M books in L-section
    M_in_S = 0  # M books in S-section
    S_in_L = 0  # S books in L-section
    S_in_M = 0  # S books in M-section
    
    for i, book in enumerate(books):
        if i < count_L:  # L-section
            if book == 'M':
                M_in_L += 1
            elif book == 'S':
                S_in_L += 1
        elif i < count_L + count_M:  # M-section
            if book == 'L':
                L_in_M += 1
            elif book == 'S':
                S_in_M += 1
        else:  # S-section
            if book == 'L':
                L_in_S += 1
            elif book == 'M':
                M_in_S += 1
    
    # Direct swaps: L in M-section <-> M in L-section
    direct_LM = min(L_in_M, M_in_L)
    swaps = direct_LM
    L_in_M -= direct_LM
    M_in_L -= direct_LM
    
    # Direct swaps: L in S-section <-> S in L-section
    direct_LS = min(L_in_S, S_in_L)
    swaps += direct_LS
    L_in_S -= direct_LS
    S_in_L -= direct_LS
    
    # Direct swaps: M in S-section <-> S in M-section
    direct_MS = min(M_in_S, S_in_M)
    swaps += direct_MS
    M_in_S -= direct_MS
    S_in_M -= direct_MS
    
    # Remaining misplaced books form cycles of 3, each needs 2 swaps
    remaining = L_in_M + L_in_S + M_in_L + M_in_S + S_in_L + S_in_M
    swaps += (remaining // 3) * 2
    
    print(swaps)


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
