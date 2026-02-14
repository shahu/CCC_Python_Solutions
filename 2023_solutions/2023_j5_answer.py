"""
CCC 2023 Junior - Problem J5 - Answer
============================================================

CCC Word Hunt
Find word in grid. Allowed:
1. Straight line
2. One turn (90 degrees)
   - Must travel at least 1 letter before turn
   - Must travel at least 1 letter after turn
============================================================
"""

import os
import sys
from io import StringIO

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2023CCCJuniorTestData", "j5")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    word = input().strip()
    R = int(input())
    C = int(input())
    
    grid = []
    for _ in range(R):
        row = input().strip().replace(' ', '')
        grid.append(row)
    
    word_len = len(word)
    count = 0
    
    # 8 directions
    # (dr, dc)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    # Pre-calculate valid perpendicular turns
    # For each direction index i, turns are at indices:
    # 0->2,6; 1->3,4; 2->0,7 etc.
    # Actually simpler: check dot product is 0 for perpendicular
    
    for r in range(R):
        for c in range(C):
            if grid[r][c] != word[0]:
                continue
            
            for dr, dc in directions:
                # 1. Check straight line
                valid_straight = True
                for k in range(1, word_len):
                    nr, nc = r + dr*k, c + dc*k
                    if not (0 <= nr < R and 0 <= nc < C and grid[nr][nc] == word[k]):
                        valid_straight = False
                        break
                if valid_straight:
                    count += 1
                
                # 2. Check turns
                # Turn can happen at index k (1 to word_len-1)
                # Word index: 0 ... k (turn) ... word_len-1
                # Segment 1: indices 0 to k (length k+1)
                # Segment 2: indices k to word_len-1 (length word_len-k)
                
                # Check segment 1 first
                # We need valid straight line up to index k
                # Optimization: reuse the loop, but we need to check turns at EACH step
                
                current_r, current_c = r, c
                # Verify segment 1 step by step
                for k in range(1, word_len):
                    current_r += dr
                    current_c += dc
                    
                    if not (0 <= current_r < R and 0 <= current_c < C and grid[current_r][current_c] == word[k]):
                        break # Segment 1 broken, stop checking this direction
                    
                    # At index k, we can turn 90 degrees
                    # Only if remaining length > 0
                    if k < word_len - 1:
                        # Try both perpendicular directions
                        # (dr, dc) -> (-dc, dr) and (dc, -dr)
                        perp_dirs = [(-dc, dr), (dc, -dr)]
                        
                        for pdr, pdc in perp_dirs:
                            valid_turn = True
                            # Check segment 2
                            tr, tc = current_r, current_c
                            for m in range(k + 1, word_len):
                                tr += pdr
                                tc += pdc
                                if not (0 <= tr < R and 0 <= tc < C and grid[tr][tc] == word[m]):
                                    valid_turn = False
                                    break
                            if valid_turn:
                                count += 1
    
    print(count)


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
