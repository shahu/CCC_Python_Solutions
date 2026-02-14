"""
CCC 2022 Junior - Problem J5 - Answer
============================================================

Square Pool
Given NxN yard with T trees, find largest square pool that can be built.

============================================================
"""

import os
import sys
from io import StringIO

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2022CCCJuniorTestData", "j5")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    Solution for CCC 2022 Junior Problem J5 - Square Pool
    Time: O(T^2)
    Space: O(T)
    """
    N = int(input())
    T = int(input())
    
    # Store tree positions (r, c)
    trees = []
    for _ in range(T):
        trees.append(list(map(int, input().split())))
    
    # Add dummy trees at boundaries to simplify logic
    # But wait, logic is: Find largest square in empty space.
    # Empty space is bounded by trees or yard edges.
    
    # Key idea: The top edge of the maximum square must be either:
    # 1. The top edge of the yard (row 1)
    # 2. Immediately below a tree (row r+1)
    
    # So potential top rows are 1 and r+1 for each tree
    # Potential bottom rows are N and r-1 for each tree
    # But checking all pairs is O(T^2).
    
    # Let's add boundary "trees" slightly outside
    # No, let's stick to the logic:
    # For every pair of trees (or boundary), if they form the vertical bounds,
    # find max width between horizontal bounds.
    
    trees.append([0, 0]) # Top-Left outer
    # Actually just consider row indices
    
    # Potential top rows: 1, and r+1 for every tree
    rows = set()
    rows.add(1)
    for r, c in trees:
        if r < N:
            rows.add(r + 1)
    
    sorted_rows = sorted(list(rows))
    max_size = 0
    
    # Iterate through each potential top row
    for r_top in sorted_rows:
        # We want to find the largest square starting at r_top
        # The bottom of this square is limited by N
        # And by any tree with row >= r_top
        
        # Maintain a list of "active" trees below r_top
        # We want to find max width for a given height
        
        # Actually, simpler O(T^2) approach:
        # For every vertical strip defined by two trees (or boundaries)
        # Find the max square.
        pass

    # Alternative O(T^2) Algorithm:
    # A maximal empty square must be bounded by trees/walls on all 4 sides?
    # Not necessarily all 4, but at least on some sides.
    
    # Correct O(T^2) Logic:
    # For every tree i (and top boundary), consider it as the top constraint.
    # Then iterate through all other trees j (and bottom boundary) as bottom constraint.
    # For the strip between row i and row j, find the widest gap between trees.
    
    # Trees + Boundaries
    # Use (row, col)
    # Add dummy trees for boundaries?
    # Top wall: acts like trees at (0, c) for all c? No.
    
    # Let's use the row-based sweep.
    # Possible top/bottom boundaries are determined by trees.
    
    # Add dummy trees at row 0 and row N+1
    relevant_trees = trees[:]
    relevant_trees.append([0, 0]) # Just row 0 matters
    relevant_trees.append([N+1, 0]) # Just row N+1 matters
    
    # Sort by row
    relevant_trees.sort()
    
    ans = 0
    
    # Iterate over all pairs of trees to define vertical strip
    for i in range(len(relevant_trees)):
        for j in range(i + 1, len(relevant_trees)):
            # Define strip between tree i and tree j
            r1 = relevant_trees[i][0]
            r2 = relevant_trees[j][0]
            
            # Height of strip
            h = r2 - r1 - 1
            
            if h <= ans:
                continue
                
            # If we have enough height, find max width in this strip
            # Find all trees strictly inside this row range (r1 < r < r2)
            cols = [0, N + 1] # Left and right yard boundaries
            for k in range(len(relevant_trees)):
                tr, tc = relevant_trees[k]
                if r1 < tr < r2:
                    cols.append(tc)
            
            cols.sort()
            
            # Find max width gap
            max_w = 0
            for k in range(len(cols) - 1):
                w = cols[k+1] - cols[k] - 1
                max_w = max(max_w, w)
            
            # The square size is limited by height and width
            ans = max(ans, min(h, max_w))
            
    print(ans)


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
