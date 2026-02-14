"""
CCC 2023 Junior/Senior - Problem J4/S1 - Answer
============================================================

Trianglane
Count perimeter (warning tape length).
Each filled triangle has 3 meters.
Subtract shared edges.
Horizontal sharing: C and C+1
Vertical sharing: 
 - Row 0 index i points UP if i is even, DOWN if i is odd
 - Row 1 index i points UP if i is even, DOWN if i is odd (Wait, usually alternate?)
 
Re-reading standard tiling:
Row 0: /\ /\ /\ ... (Up, Down, Up...) -> NO
Actually standard grid:
Row 0: Up (0), Down (1), Up (2)...
Row 1: Up (0), Down (1), Up (2)...

BUT vertical connection only happens when bases touch.
Row 0 Down (odd index) touches Row 1 Up (odd index)? No.
Row 0 Up (even) base is at bottom.
Row 1 Up (even) base is at bottom.
Row 1 Down (odd) base is at top.

Correct alignment for Trianglane:
Row 0 (Top): Indices 0, 2, 4... point UP. Indices 1, 3, 5... point DOWN.
Row 1 (Bottom): Indices 0, 2, 4... point UP. Indices 1, 3, 5... point DOWN.

Wait, if Row 0 index i points DOWN, its base is at TOP? No, usually point down means V.
Point UP: ^ (base at bottom)
Point DOWN: v (base at top)

Vertical shared edge happens when:
Row 0 triangle points UP (base at bottom) AND Row 1 triangle points DOWN (base at top)?
OR
Row 0 triangle points DOWN (base at top) - no neighbor below.

Let's look at logic:
Indices are columns 0, 1, 2...
C1 = column index (0-based)
If C1 is EVEN (0, 2...):
  Row 0: Points UP (base bottom)
  Row 1: Points UP (base bottom) -> No shared edge (Row 1 is below Row 0)
  Wait, maybe they are interleaved?
  
Let's try simpler logic based on parity.
Vertical adjacency occurs at even columns (0, 2, 4...) OR odd columns (1, 3, 5...)?
Typically in this problem, vertical neighbors exist at ODD indices (1, 3, 5...).
Let's test this hypothesis.
============================================================
"""

import os
import sys
from io import StringIO

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2023CCCJuniorTestData", "s1j4")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    C = int(input())
    row0 = list(map(int, input().split()))
    row1 = list(map(int, input().split()))
    
    perimeter = 0
    
    # 1. Count wet tiles -> each contributes 3
    perimeter += sum(row0) * 3
    perimeter += sum(row1) * 3
    
    # 2. Subtract horizontal shared edges (count twice, once for each neighbor)
    for i in range(C - 1):
        # Row 0 horizontal
        if row0[i] == 1 and row0[i+1] == 1:
            perimeter -= 2
        # Row 1 horizontal
        if row1[i] == 1 and row1[i+1] == 1:
            perimeter -= 2
            
    # 3. Subtract vertical shared edges
    # Vertical connection happens at ODD indices (0-based: 0, 2, 4...) because:
    # Col 0 (Even): Top ^, Bottom ^ (No touch) or Top ^, Bottom v (Touch?)
    # Actually for this problem specifically:
    # Vertical connections are at even indices (0, 2, 4...)
    
    for i in range(C):
        if i % 2 == 0:  # Vertical connection only at even indices 0, 2, 4...
            if row0[i] == 1 and row1[i] == 1:
                perimeter -= 2
                
    print(perimeter)


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
