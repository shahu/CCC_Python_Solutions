"""
CCC 2022 Junior - Problem J1
============================================================

 Cupcake Party
Problem Description
A regular box of cupcakes holds 8 cupcakes, while a small box holds 3 cupcakes. There are
28 students in a class and a total of at least 28 cupcakes. Your job is to determine how many
cupcakes will be left over if each student gets one cupcake.
Input Speciﬁcation
The input consists of two lines.
• The ﬁrst line contains an integer R ≥ 0, representing the number of regular boxes.
• The second line contains an integer S ≥ 0, representing the number of small boxes.
Output Speciﬁcation
Output the number of cupcakes that are left over.
Sample Input 1
2
5
Output for Sample Input 1
3
Explanation of Output for Sample Input 1
The total number of cupcakes is 2 × 8 + 5× 3 which equals 31. Since there are 28 students,
there are 3 cupcakes left over.
Sample Input 2
2
4
Output for Sample Input 2
0
Explanation of Output for Sample Input 2
The total number of cupcakes is 2 × 8 + 4× 3 which equals 28. Since there are 28 students,
there are no cupcakes left over.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Probl` eme J1 : Petits gˆ ateaux festifs
´Enonc´ e du probl` eme
Une boˆ ıte ` a gateaux de taille normale contient 8 petits gˆ ateaux tandis qu’une petite boˆ ıte
` a gateaux contient 3 petits gˆ ateaux. Il y a 28 ´ el` eves dans une classe et au moins 28 petits
gˆ ateaux en tout. Votre tˆ ache consiste ` a d´ eterminer le nombre de petits gˆ ateaux restants
apr` es que chaque ´ el` eve en ait re¸ cu un.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
Les donn´ ees d’entr´ ee ne contiennent que deux lignes.
— La premi` ere ligne contient un entierN ≥ 0 repr´ esentant le nombre de boˆ ıtes de taille
normale.
— La seconde ligne contient un entier P ≥ 0, repr´ esentant le nombre de petites boˆ ıtes.
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sortie devraient aﬃcher le nombre de petits gˆ ateaux restants.
Donn´ ees d’entr´ ee d’un 1er exemple
2
5
Donn´ ees de sortie du 1er exemple
3
Justiﬁcation des donn´ ees de sortie du 1er exemple
Il y a 2 × 8 + 5 × 3 = 31 petits gˆ ateaux en tout. Puisqu’il y a 28 ´ el` eves, alors il y a 3 petits
gˆ ateaux restants.
Donn´ ees d’entr´ ee d’un 2e exemple
2
4
Donn´ ees de sortie du 2e exemple
0
Justiﬁcation des donn´ ees de sortie du 2e exemple
Il y a 2 × 8 + 4× 3 = 28 petits gˆ ateaux en tout. Puisqu’il y a 28 ´ el` eves, il ne reste donc pas
de petits gˆ ateaux.
English version appears before the French version.

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2022CCCJuniorTestData", "j1")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2022 Problem J1
    
    Read input from standard input and write output to standard output.
    You can use input() to read lines and print() to write output.
    """
    # TODO: Read input
    
    # TODO: Process the input and calculate the result
    
    # TODO: Print the output
    pass


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
        print(f"Script location: {SCRIPT_DIR}")
        print(f"Looking in: {TEST_DATA_DIR}")
        print(f"Absolute path: {os.path.abspath(TEST_DATA_DIR)}")
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