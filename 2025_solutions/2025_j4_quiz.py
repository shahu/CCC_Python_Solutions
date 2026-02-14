"""
CCC 2025 Junior - Problem J4
============================================================

 Sunny Days
Problem Description
There is a large amount of historical weather data for CEMCity. Each
day in the data is listed as either a day with sunshine or a day with
precipitation. Jeremy is interested in ﬁnding the record for the most
consecutive days with sunshine. Unfortunately, the data is incorrect
for exactly one day, but Jeremy doesn’t know which day this is.
Your job is to help Jeremy determine the maximum possible number
of consecutive days with sunshine.
Input Speciﬁcation
The ﬁrst line of input contains a positive integer, N, representing the number of days in the
historical data. The following N lines each contain either the character S or the character P,
representing a day with sunshine or a day with precipitation, respectively, in chronological
order.
The following table shows how the available 15 marks are distributed:
Marks Description Bounds
2 There are not many days in the historical data. The data con-
sists of a single block of all S’s followed by a single block of all
P’s. One of these blocks may be empty.
N ≤ 1000
4 There are not many days in the historical data. The data con-
tains S’s and P’s possibly in mixed order.
N ≤ 1000
9 There are possibly many days in the historical data. N ≤ 500 000
Output Speciﬁcation
Output the non-negative integer, M, which is the maximum possible number of consecutive
days with sunshine.
Sample Input
8
P
S
P
S
S
P
P
S
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Output for Sample Input
4
Explanation of Output for Sample Input
If the data is incorrect for the third day, then there was sunshine from the second day to the
ﬁfth day which is four consecutive days with sunshine. This is the maximum possible number
of consecutive days with sunshine. That is, no matter which day the data is incorrect for,
there were not ﬁve (or more) consecutive days of sunshine.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Probl` eme J4 : Journ´ ees ensoleill´ ees
´Enonc´ e du probl` eme
Il existe un vaste ensemble de donn´ ees m´ et´ eorologiques historiques
pour la municipalit´ e de CEMIville. Chaque jour est cat´ egoris´ e dans
cet ensemble de donn´ ees comme une journ´ ee de soleil ou une journ´ ee
de pluie. J´ er´ emie souhaite trouver le record du plus grand nombre de
journ´ ees de soleil cons´ ecutives. Malheureusement, la donn´ ee pour l’une
des journ´ ees est erron´ ee et J´ er´ emie ne sait pas de quel jour il s’agit.
Votre tˆ ache consiste ` a aider J´ er´ emie ` a d´ eterminer le nombre maximal
de jours de soleil cons´ ecutifs possible.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
La premi` ere ligne de donn´ ees d’entr´ ee contient un entier strictement positif,N, repr´ esentant
le nombre de jours dans l’ensemble de donn´ ees historique. LesN lignes de donn´ ees d’entr´ ee
suivantes contiennent chacune le caract` ereS ou le caract` ereP, repr´ esentant respectivement
un jour de soleil ou de pluie, en ordre chronologique.
Le tableau suivant d´ etaille la r´ epartition des 15 points disponibles.
Points Description Bornes
2 Il n’y a pas beaucoup de jours dans l’ensemble de donn´ ees histo-
riques. Les donn´ ees seront constitu´ ees d’un seul bloc deS suivi
d’un seul bloc de P et l’un de ces blocs peut ˆ etre vide.
N ≤ 1000
4 Il n’y a pas beaucoup de jours dans l’ensemble de donn´ ees his-
toriques. Les donn´ ees contiennent desS et des P, possiblement
dans un ordre mixte.
N ≤ 1000
9 Il est possible qu’il y ait beaucoup de jours dans l’ensemble de
donn´ ees historiques.
N ≤ 500 000
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sortie devraient contenir un entier positif,M, repr´ esentant le nombre maximal
de jours de soleil cons´ ecutifs possible.
Donn´ ees d’entr´ ee
8
P
S
P
S
S
P
P
S
English version appears before the French version
Donn´ ees de sortie
4
Justiﬁcation des donn´ ees de sortie
Si la donn´ ee du troisi` eme jour est erron´ ee, le soleil aura ´ et´ e pr´ esent du deuxi` eme au cinqui` eme
jour, soit quatre jours de soleil cons´ ecutifs. Il s’agit du nombre maximal de jours de soleil
cons´ ecutifs possible. Autrement dit, quel que soit le jour pour lequel la donn´ ee est incorrecte,
il ne peut y avoir eu cinq (ou plus) jours de soleil cons´ ecutifs.
English version appears before the French version

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2025CCCJuniorTestData", "j4")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2025 Problem J4
    
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