"""
CCC 2025 Junior - Problem J2
============================================================

 Donut Shop
Problem Description
The owner of a donut shop spends the day baking and selling donuts.
Given the events that happen over the course of the day, your job is
to determine the number of donuts remaining when the shop closes.
Input Speciﬁcation
The ﬁrst line of input contains a non-negative integer, D, representing the number of donuts
available when the shop ﬁrst opens.
The second line contains a positive integer,E, representing the number of events that happen
over the course of the day. The next E pairs of input lines describe these events.
The ﬁrst line in the pair contains either the + (plus) symbol, indicating that donuts have
been baked, or the - (minus) symbol, indicating that donuts have been sold. The second
line in the pair contains a positive integer, Q, representing the quantity of donuts associated
with the event.
For each sale of donuts, the value of Q will be less than or equal to the number of donuts
available at that time.
Output Speciﬁcation
Output the non-negative integer, R, which is the number of donuts remaining when the shop
closes.
Sample Input
10
3
+
24
-
6
-
12
Output for Sample Input
16
Explanation of Output for Sample Input
The shop opened with 10 donuts and there were 3 events during the day. The owner ﬁrst
baked 24 donuts. Then the owner sold 6 donuts, followed by another 12. The number of
donuts remaining is 10 + 24 − 6 − 12 = 16.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Probl` eme J2 : Beignerie
´Enonc´ e du probl` eme
La propri´ etaire d’une beignerie passe sa journ´ ee ` a pr´ eparer et ` a vendre
des beignets.
Votre tˆ ache consiste ` a d´ eterminer le nombre de beignets invendus
au moment de la fermeture de la beignerie, en vous basant sur les
´ ev´ enements de la journ´ ee.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
La premi` ere ligne des donn´ ees d’entr´ ee contient un entier positif,B, repr´ esentant le nombre
de beignets en vente ` a l’ouverture de la beignerie.
La deuxi` eme ligne des donn´ ees d’entr´ ee contient un entier strictement positif,E, repr´ esentant
le nombre d’´ ev´ enements de la journ´ ee. LesE paires de lignes de donn´ ees d’entr´ ee suivantes
d´ ecrivent ces ´ ev´ enements.
La premi` ere ligne de chaque paire contient soit le symbole+ (plus), indiquant que des beignets
ont ´ et´ e pr´ epar´ es, soit le symbole- (moins), indiquant que des beignets ont ´ et´ e vendus. La
deuxi` eme ligne de la paire de lignes contient un entier strictement positif, Q, repr´ esentant
la quantit´ e de beignets associ´ ee ` a l’´ ev´ enement.
Pour chaque vente de beignets, la valeur de l’entier strictement positif Q sera inf´ erieure ou
´ egale au nombre de beignets disponibles ` a ce moment-l` a.
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sortie devraient contenir un entier positif, I, repr´ esentant le nombre de
beignets invendus ` a la fermeture de la boutique.
Donn´ ees d’entr´ ee
10
3
+
24
-
6
-
12
Donn´ ees de sortie
16
English version appears before the French version
Justiﬁcation des donn´ ees de sortie
Lorsque la boutique a ouvert ses portes, 10 beignets ´ etaient en vente, puis 3 ´ ev´ enements ont
eu lieu au cours de la journ´ ee. La propri´ etaire a d’abord pr´ epar´ e 24 beignets. Elle a ensuite
vendu 6 beignets, puis 12 autres. Le nombre de beignets invendus au moment de la fermeture
est de 10 + 24 − 6 − 12 = 16.
English version appears before the French version

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2025CCCJuniorTestData", "j2")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2025 Problem J2
    
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