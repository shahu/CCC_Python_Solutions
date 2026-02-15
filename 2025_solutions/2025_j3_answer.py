"""
CCC 2025 Junior - Problem J3 - Answer
============================================================

Product Codes
Remove lowercase letters, keep uppercase in order, sum all integers.

============================================================
"""

import os
import sys
from io import StringIO
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2025CCCJuniorTestData", "j3")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    N = int(input())
    
    for _ in range(N):
        code = input().strip()
        
        # Extract uppercase letters
        # Extract only the uppercase letters from the code string.
        # This generator expression iterates over each character 'c' in 'code',
        # checks if it is uppercase using c.isupper(), and joins them into a new string.
        uppercase = ''.join(c for c in code if c.isupper())
        
        # Extract all integers (positive and negative)
        # Initialize the total sum of integers to 0
        total = 0
        # Initialize the index variable `i` to 0 to start iterating through the string
        i = 0
        # Get the length of the string `code` to use in the loop condition
        n_len = len(code)
        # Iterate through the string as long as `i` is less than the length of the string
        while i < n_len:
            # Check if the current character is a digit OR if it's a minus sign followed by a digit (representing a negative number)
            if code[i].isdigit() or (code[i] == '-' and i + 1 < n_len and code[i+1].isdigit()):
                # Mark the start index of the number
                start = i
                # If the number starts with a minus sign, increment `i` to skip it
                if code[i] == '-':
                    # Move to the next character
                    i += 1
                # Continue incrementing `i` as long as the current character is a digit
                while i < n_len and code[i].isdigit():
                    # Move to the next character
                    i += 1
                # Convert the substring from `start` to `i` (the number) to an integer and add it to `total`
                total += int(code[start:i])
            else:
                # If the current character is not part of a number, increment `i` to move to the next character
                i += 1
        
        print(uppercase + str(total))


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
