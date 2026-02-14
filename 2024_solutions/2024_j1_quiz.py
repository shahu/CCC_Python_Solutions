"""
CCC 2024 Junior - Problem J1
============================================================

 Conveyor Belt Sushi
Problem Description
There is a new conveyor belt sushi restaurant in town. Plates of sushi travel around the
restaurant on a raised conveyor belt and customers choose wh at to eat by removing plates.
Each red plate of sushi costs $3, each green plate of sushi costs $4, and each blue plate of
sushi costs $5.
Your job is to determine the cost of a meal, given the number of plates of each colour chosen
by a customer.
Input Speciﬁcation
The ﬁrst line of input contains a non-negative integer, R, representing the number of red
plates chosen. The second line contains a non-negative inte ger, G, representing the number
of green plates chosen. The third line contains a non-negati ve integer, B, representing the
number of blue plates chosen.
Output Speciﬁcation
Output the non-negative integer, C, which is the cost of the meal in dollars.
Sample Input
0
2
4
Output for Sample Input
28
Explanation of Output for Sample Input
This customer chose 0 red plates, 2 green plates, and 4 blue pl ates. Therefore, the cost of
the meal in dollars is 0 × 3 + 2 × 4 + 4 × 5 = 28.
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Probl` eme J1: Sushi sur tapis roulant
´Enonc´ e du probl` eme
Un restaurant de sushis sur tapis roulant a r´ ecemment ouvertses portes. Dans ce restaurant,
les clients peuvent s´ electionner leurs sushis en prenant des assiettes qui circulent sur un tapis
roulant sur´ elev´ e.
Chaque assiette rouge de sushi coˆ ute 3 $, chaque assiette verte de sushi coˆ ute 4 $ et chaque
assiette bleue de sushi coˆ ute 5 $.
Votre tˆ ache consiste ` a d´ eterminer le coˆ ut d’un repas en fonction du nombre d’assiettes de
chaque couleur s´ electionn´ ees par un client.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
La premi` ere ligne des donn´ ees d’entr´ ee contient un entier non n´ egatif, R, repr´ esentant le
nombre d’assiettes rouges s´ electionn´ ees. La deuxi` eme ligne contient un entier non n´ egatif,
G, repr´ esentant le nombre d’assiettes vertes s´ electionn´ees. La troisi` eme ligne contient un
entier non n´ egatif,B, repr´ esentant le nombre d’assiettes bleues s´ electionn´ees.
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sortie devraient aﬃcher un seul entier non n´egatif C, repr´ esentant le coˆ ut du
repas en dollars.
Exemple de donn´ ees d’entr´ ee
0
2
4
Exemple de donn´ ees de sortie
28
Justiﬁcation des donn´ ees de sortie
Ce client a s´ electionn´ e 0 assiette rouge, 2 assiettes vertes et 4 assiettes bleues. Donc, le coˆ ut
du repas, en dollars, est ´ egal ` a 0 × 3 + 2 × 4 + 4 × 5 = 28.
English version appears before the French version

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2024CCCJuniorTestData", "j1")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2024 Problem J1
    
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