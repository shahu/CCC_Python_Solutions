"""
CCC 2022 Junior/Senior - Problem J4/S2 - Answer
============================================================

Good Groups
Given constraints about who must be together or separate,
count violations in assigned groups.

============================================================
"""

import os
import sys
from io import StringIO

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2022CCCJuniorTestData", "s2j4")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    Solution for CCC 2022 Junior/Senior Problem J4/S2 - Good Groups
    Time: O(X + Y + G) where G is total people in groups
    Space: O(P) where P is number of people
    
    Strategy:
    1. Read all constraints
    2. For each group assignment, check all constraints
    3. Count violations
    """
    X = int(input())  # Same group constraints
    same_constraints = []
    for _ in range(X):
        a, b = input().split()
        same_constraints.append((a, b))
    
    Y = int(input())  # Different group constraints
    diff_constraints = []
    for _ in range(Y):
        a, b = input().split()
        diff_constraints.append((a, b))
    
    G = int(input())  # Number of groups
    groups = []
    person_to_group = {}
    
    for i in range(G):
        people = input().split()
        groups.append(set(people))
        for person in people:
            person_to_group[person] = i
    
    violations = 0
    
    # Check same group constraints
    for a, b in same_constraints:
        if a in person_to_group and b in person_to_group:
            if person_to_group[a] != person_to_group[b]:
                violations += 1
    
    # Check different group constraints
    for a, b in diff_constraints:
        if a in person_to_group and b in person_to_group:
            if person_to_group[a] == person_to_group[b]:
                violations += 1
    
    print(violations)


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
