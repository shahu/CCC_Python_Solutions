"""
CCC 2022 Junior - Problem J4/S2
============================================================

 Good Groups
Problem Description
A class has been divided into groups of three. This division into groups might violate two
types of constraints: some students must work together in the same group, and some students
must work in separate groups.
Your job is to determine how many of the constraints are violated.
Input Speciﬁcation
The ﬁrst line will contain an integer X with X ≥ 0. The next X lines will each consist of
two diﬀerent names, separated by a single space. These two students must be in the same
group.
The next line will contain an integer Y with Y ≥ 0. The next Y lines will each consist of
two diﬀerent names, separated by a single space. These two students must not be in the
same group.
Among these X + Y lines representing constraints, each possible pair of students appears at
most once.
The next line will contain an integer G with G ≥ 1. The last G lines will each consist of
three diﬀerent names, separated by single spaces. These three students have been placed in
the same group.
Each name will consist of between 1 and 10 uppercase letters. No two students will have
the same name and each name appearing in a constraint will appear in exactly one of the G
groups.
The following table shows how the available 15 marks are distributed at the Junior level.
Marks Awarded Number of Groups Number of Constraints
4 marks G ≤ 50 X ≤ 50 and Y = 0
10 marks G ≤ 50 X ≤ 50 and Y ≤ 50
1 mark G ≤ 100 000 X ≤ 100 000 and Y ≤ 100 000
The following table shows how the available 15 marks are distributed at the Senior level.
Marks Awarded Number of Groups Number of Constraints
3 marks G ≤ 50 X ≤ 50 and Y = 0
5 marks G ≤ 50 X ≤ 50 and Y ≤ 50
7 marks G ≤ 100 000 X ≤ 100 000 and Y ≤ 100 000
Output Speciﬁcation
Output an integer between 0 and X +Y which is the number of constraints that are violated.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Sample Input 1
1
ELODIE CHI
0
2
DWAYNE BEN ANJALI
CHI FRANCOIS ELODIE
Output for Sample Input 1
0
Explanation of Output for Sample Input 1
There is only one constraint and it is not violated: ELODIE and CHI are in the same group.
Sample Input 2
3
A B
G L
J K
2
D F
D G
4
A C G
B D F
E H I
J K L
Output for Sample Input 2
3
Explanation of Output for Sample Input 2
The ﬁrst constraint is that A and B must be in the same group. This is violated.
The second constraint is that G and L must be in the same group. This is violated.
The third constraint is that J and K must be in the same group. This is not violated.
The fourth constraint is that D and F must not be in the same group. This is violated.
The ﬁfth constraint is that D and G must not be in the same group. This is not violated.
Of the ﬁve constraints, three are violated.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Probl` eme J4/S2 : De bons groupes
´Enonc´ e du probl` eme
Une classe a ´ et´ e divis´ ee en groupes de trois. Cette division en groupes peut enfreindre deux
types de r` egles. Ces types de r` egles sont : certains ´ el` eves doivent travailler ensemble dans le
mˆ eme groupe tandis que d’autres doivent travailler dans des groupes diﬀ´ erents.
Votre tˆ ache consiste ` a d´ eterminer le nombre de r` egles qui ont ´ et´ e enfreintes.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
La premi` ere ligne des donn´ ees d’entr´ ee ne contient qu’un seul entierX (X ≥ 0). Les X lignes
suivantes contiennent chacune deux noms diﬀ´ erents, ces derniers ´ etant s´ epar´ es par un seul
espace. Ces deux ´ el` evesdoivent ˆ etre dans le mˆ eme groupe.
La ligne suivante ne contient qu’un seul entierY (Y ≥ 0). Les Y lignes suivantes contiennent
chacune deux noms diﬀ´ erents, ces derniers ´ etant s´ epar´ es par un seul espace. Ces deux ´ el` eves
ne peuvent ˆ etre dans le mˆ eme groupe.
Dans ces X + Y lignes de r` egles, chaque couple possible d’´ el` eves ne peut paraitre plus d’une
seule fois.
La ligne suivante ne contient qu’un seul entier G (G ≥ 1). Les G lignes restantes contiennent
chacune trois noms diﬀ´ erents, chacun de ces derniers ´ etant s´ epar´ e des autres par un espace.
Ces trois ´ el` eves ont ´ et´ e plac´ es dans le mˆ eme groupe.
Chaque nom sera compos´ e de 1 ` a 10 lettres majuscules. Deux ´ el` eves ne peuvent avoir le
mˆ eme nom. De plus, chaque nom paraissant dans une r` egle doit ´ egalement paraitre dans
exactement un des G groupes.
Le tableau suivant indique la mani` ere dont les 15 points disponibles sont r´ epartis au niveau
interm´ ediaire.
Attribution des points Nombre de groupes Nombre de r` egles
4 points G ≤ 50 X ≤ 50 and Y = 0
10 points G ≤ 50 X ≤ 50 and Y ≤ 50
1 point G ≤ 100 000 X ≤ 100 000 and Y ≤ 100 000
Le tableau suivant indique la mani` ere dont les 15 points disponibles sont r´ epartis au niveau
sup´ erieur.
Attribution des points Nombre de groupes Nombre de r` egles
3 points G ≤ 50 X ≤ 50 and Y = 0
5 points G ≤ 50 X ≤ 50 and Y ≤ 50

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2022CCCJuniorTestData", "s2j4")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2022 Problem J4/S2
    
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