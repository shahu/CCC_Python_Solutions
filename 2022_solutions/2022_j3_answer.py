"""
CCC 2022 Junior - Problem J3 - Answer
============================================================

Harp Tuning
Given instructions like "AFB+3" (strings A-F tighten 3) or "D-2" (string D loosen 2)
Output instructions in readable format.

============================================================
"""

import os
import sys
from io import StringIO

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2022CCCJuniorTestData", "j3")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    Solution for CCC 2022 Junior Problem J3 - Harp Tuning
    Time: O(L) where L is length of input string
    Space: O(1)
    
    Parse instruction format:
    - Group of strings (A-T)
    - +N to tighten N turns, or -N to loosen N turns
    """
    instructions = input().strip()
    
    i = 0
    n = len(instructions)
    results = []
    
    while i < n:
        # Read string group (consecutive uppercase letters)
        strings = ""
        while i < n and instructions[i].isalpha():
            strings += instructions[i]
            i += 1
        
        # Read sign (+ or -)
        sign = instructions[i]
        i += 1
        
        # Read number
        num = ""
        while i < n and instructions[i].isdigit():
            num += instructions[i]
            i += 1
        
        # Format output
        action = "tighten" if sign == "+" else "loosen"
        results.append(f"{strings} {action} {num}")
    
    print("\n".join(results))


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
