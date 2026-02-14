"""
CCC 2025 Junior - Problem J5 - Answer
============================================================

Connecting Territories
Optimization: Use 3-pass scan for DP transition to avoid inner loop.
============================================================
"""

import os
import sys
from io import StringIO

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2025CCCJuniorTestData", "j5")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    # Ultra Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    iterator = iter(input_data)
    try:
        R = int(next(iterator))
        C = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return
        
    # Row 0 costs
    # dp[c] stores min cost to reach cell (r, c)
    dp = [(c % M) + 1 for c in range(C)]
    
    # Pre-allocate arrays
    new_dp = [0] * C
    
    # Process rows
    for r in range(1, R):
        # Calculate base costs for current row
        base_val = (r * C) % M
        
        # 3-pass optimization:
        # We need min(dp[c-1], dp[c], dp[c+1]) + cost
        # This is equivalent to finding local minimum in window of 3
        
        # Pass 1: Handle same column and cost calculation
        for c in range(C):
            cost = ((base_val + c) % M) + 1
            new_dp[c] = dp[c] + cost
            
        # Pass 2: Propagate from left (c-1 to c)
        # Actually we need min from prev row, not current row propagation
        # The transition is: new_dp[c] = min(dp[c-1], dp[c], dp[c+1]) + cost
        
        # Left boundary
        if C > 1:
            val = dp[1]
            if val < dp[0]:
                # dp[0] stays min(dp[0], dp[1])
                new_dp[0] = min(new_dp[0], val + ((base_val) % M) + 1)
        
        # Middle columns
        for c in range(1, C - 1):
            # min of dp[c-1], dp[c], dp[c+1]
            m = dp[c]
            if dp[c-1] < m: m = dp[c-1]
            if dp[c+1] < m: m = dp[c+1]
            
            # Recalculate with minimum neighbor
            cost = ((base_val + c) % M) + 1
            new_dp[c] = m + cost
            
        # Right boundary
        if C > 1:
            c = C - 1
            val = dp[c-1]
            if val < dp[c]:
                new_dp[c] = min(new_dp[c], val + ((base_val + c) % M) + 1)
                
        # Swap arrays
        dp[:] = new_dp[:]
        
    print(min(dp))


def run_tests():
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
