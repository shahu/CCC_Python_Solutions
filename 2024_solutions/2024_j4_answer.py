"""
CCC 2024 Junior - Problem J4 - Answer
============================================================

Troublesome Keys
Find silly key (wrong output) and quiet key (no output).
Silly key output is consistent.
============================================================
"""

import os
import sys
from io import StringIO

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2024CCCJuniorTestData", "j4")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    input_str = input().strip()
    output_str = input().strip()
    
    # Try all possible pairs of (silly_key, quiet_key) isn't feasible (26*26)
    # But we can iterate and check consistency.
    
    # Strategy:
    # 1. Identify all unique characters in input
    # 2. Iterate through possible silly keys and quiet keys
    
    unique_chars = sorted(list(set(input_str)))
    possible_silly = unique_chars
    possible_quiet = unique_chars + [None] # Quiet key might not exist? Problem says "Alex presses the silly key at least once but they don’t necessarily press the quiet key."
    # So quiet_key could be None if lengths match? No, if lengths differ, quiet key must exist.
    
    if len(input_str) == len(output_str):
        possible_quiet = [None]
    
    for silly in possible_silly:
        for quiet in possible_quiet:
            if silly == quiet: continue
            
            # Determine wrong letter
            # Find first occurrence of silly in input
            # Map it to displayed
            
            wrong_char = None
            
            # Simulate
            simulated = []
            valid_hypothesis = True
            
            # We need to deduce the wrong_char
            # Scan to find first mismatch that isn't quiet
            
            temp_wrong = None
            
            idx_in = 0
            idx_out = 0
            
            while idx_in < len(input_str) and idx_out < len(output_str):
                char = input_str[idx_in]
                
                if char == quiet:
                    idx_in += 1
                    continue
                
                if char == silly:
                    # If we haven't determined wrong_char yet, set it
                    if temp_wrong is None:
                        temp_wrong = output_str[idx_out]
                    
                    # Check consistency
                    if output_str[idx_out] != temp_wrong:
                        valid_hypothesis = False
                        break
                    
                    idx_out += 1
                    idx_in += 1
                else:
                    # Normal char
                    if char != output_str[idx_out]:
                        valid_hypothesis = False
                        break
                    idx_out += 1
                    idx_in += 1
            
            # Check remaining input (should only be quiet keys)
            while idx_in < len(input_str):
                if input_str[idx_in] != quiet:
                    valid_hypothesis = False
                    break
                idx_in += 1
            
            if valid_hypothesis and idx_out == len(output_str):
                # Found it!
                print(f"{silly} {temp_wrong}")
                if quiet:
                    print(quiet)
                else:
                    print("-")
                return


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
