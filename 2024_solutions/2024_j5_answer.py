"""
CCC 2024 Junior - Problem J5 - Answer
============================================================

Harvest Waterloo
Find all connected pumpkins and sum their values.
S=$1, M=$5, L=$10. Cannot pass through hay bales (*).

============================================================
"""

import os
import sys
from io import StringIO
from collections import deque

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2024CCCJuniorTestData", "j5")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    R = int(input())
    C = int(input())
    
    grid = []
    for _ in range(R):
        grid.append(input().strip())
    
    A = int(input())  # Starting row
    B = int(input())  # Starting column
    
    # BFS to find all reachable pumpkins
    visited = [[False] * C for _ in range(R)]
    queue = deque([(A, B)])
    visited[A][B] = True
    
    value = 0
    pumpkin_values = {'S': 1, 'M': 5, 'L': 10}
    
    while queue:
        r, c = queue.popleft()
        
        # Add value if it's a pumpkin
        if grid[r][c] in pumpkin_values:
            value += pumpkin_values[grid[r][c]]
        
        # Check all 4 directions
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and grid[nr][nc] != '*':
                visited[nr][nc] = True
                queue.append((nr, nc))
    
    print(value)


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
