"""
CCC 2023 Junior - Problem J3 - Answer
============================================================

Special Event
Given N people's availability for 5 days, find the best day(s) with most people available.
If tie, choose the earliest day. Output day number and count.

============================================================
"""

import os
import sys
from io import StringIO

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2023CCCJuniorTestData", "j3")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    Solution for CCC 2023 Junior Problem J3 - Special Event
    Time: O(N), Space: O(1)
    """
    N = int(input())
    
    # Count availability for each day (1-5)
    day_count = [0] * 6  # Index 0 unused, 1-5 for days
    
    for _ in range(N):
        availability = input().strip()
        for i, avail in enumerate(availability):
            if avail == 'Y':
                day_count[i + 1] += 1
    
    # Find max availability
    max_count = max(day_count[1:])
    
    # Find all days with max availability (earliest first)
    best_days = []
    for day in range(1, 6):
        if day_count[day] == max_count:
            best_days.append(str(day))
    
    print(",".join(best_days))


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
