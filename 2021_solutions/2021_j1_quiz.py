"""
CCC 2021 Junior - Problem J1
============================================================

 Boiling Water
Problem Description
At sea level, atmospheric pressure is 100 kPa and water begin s to boil at 100 ◦C. As you go
above sea level, atmospheric pressure decreases, and water boils at lower temperatures. As
you go below sea level, atmospheric pressure increases, and water boils at higher tempera-
tures. A formula relating atmospheric pressure to the tempe rature at which water begins to
boil is
P = 5 × B − 400
where P is atmospheric pressure measured in kPa, and B is the temperature at which water
begins to boil measured in ◦C.
Given the temperature at which water begins to boil, determi ne atmospheric pressure. Also
determine if you are below sea level, at sea level, or above se a level.
Note that the science of this problem is generally correct but the values of 100◦C and 100 kPa
are approximate and the formula is a simpliﬁcation of the exact relationship between water’s
boiling point and atmospheric pressure.
Input Speciﬁcation
The input is one line containing an integer B where B ≥ 80 and B ≤ 200. This represents
the temperature in ◦C at which water begins to boil.
Output Speciﬁcation
The output is two lines. The ﬁrst line must contain an integer w hich is atmospheric pressure
measured in kPa. The second line must contain the integer -1, 0, or 1. This integer represents
whether you are below sea level, at sea level, or above sea lev el, respectively.
Sample Input 1
99
Output for Sample Input 1
95
1
Explanation of Output for Sample Input 1
When B = 99, we can substitute into the formula and get P = 5 × 99 − 400 which equals
95. Since 95 kPa is less than 100 kPa, you are above sea level.
Sample Input 2
102
Output for Sample Input 2
110
-1
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Explanation of Output for Sample Input 2
When B = 102, we can substitute into the formula and get P = 5 × 102 − 400 which equals
110. Since 110 kPa is greater than 100 kPa, you are below sea le vel.
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Probl` eme J1 : L’´ ebullition de l’eau
´Enonc´ e du probl` eme
Au niveau de la mer, la pression atmosph´ erique est de 100 kPa e t l’eau commence ` a bouillir
` a 100◦C. Au fur et ` a mesure que l’on monte en altitude, la pression at mosph´ erique diminue
et l’eau bout ` a des temp´ eratures plus basses. Au fur et ` a mes ure que l’on descend sous le
niveau de la mer, la pression atmosph´ erique augmente et l’e au bout ` a des temp´ eratures plus
´ elev´ ees. La formule suivante relie la pression atmosph´ erique au point d’´ ebullition de l’eau :
P = 5 × B − 400
P ´ etant la pression atmosph´ erique en kPa etB ´ etant la temp´ erature en◦C ` a laquelle l’eau
commence ` a bouillir.
´Etant donn´ e la temp´ erature ` a laquelle l’eau commence ` a b ouillir, d´ eterminer la pression
atmosph´ erique. D´ eterminer ´ egalement si l’on est situ´ een dessous du niveau de la mer, au
niveau de la mer ou au-dessus du niveau de la mer.
Remarquons que les informations scientiﬁques pr´ esent´ ees sont en g´ en´ eral correctes mais que
les valeurs de 100◦C et 100 kPa sont approximatives. De plus, la formule pr´ esent´ ee est une
simpliﬁcation de la relation exacte qui existe entre le point d’´ ebullition de l’eau et la pression
atmosph´ erique.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
Les donn´ ees d’entr´ ee ne contiennent qu’une seule ligne. Cette ligne ne contient qu’un seul
entier, B, tel que B ≥ 80 et B ≤ 200. Cet entier repr´ esente la temp´ erature en◦C ` a laquelle
l’eau commence ` a bouillir.
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sortie ne devraient contenir que deux lignes . La premi` ere ligne doit contenir
un entier repr´ esentant la pression atmosph´ erique en kPa.La seconde ligne doit contenir l’un
des entiers -1, 0 ou 1. Les entiers -1, 0 et 1 indiquent respectivement que l’on est situ´ e en
dessous du niveau de la mer, au niveau de la mer ou au-dessus du niveau de la mer.
Donn´ ees d’entr´ ee d’un 1er exemple
99
Donn´ ees de sortie du 1er exemple
95
1
Justiﬁcation des donn´ ees de sortie du 1 er exemple
On pose B = 99 dans la formule pour obtenir P = 5 × 99 − 400, soit 95. Puisque 95 kPa est
inf´ erieur ` a 100 kPa, alors on est situ´ e au-dessus du niveau de la mer.
English version appears before the French version
Donn´ ees d’entr´ ee d’un 2e exemple
102
Donn´ ees de sortie du 2e exemple
110
-1
Justiﬁcation des donn´ ees de sortie du 2 e exemple
On pose B = 102 dans la formule pour obtenir P = 5 × 102 − 400, soit 110. Puisque 110 kPa
est sup´ erieur ` a 100 kPa, alors on est situ´ e en dessous du niveau de la mer.
English version appears before the French version

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2021CCCJuniorTestData", "j1")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2021 Problem J1
    
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