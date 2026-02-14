"""
CCC 2021 Junior - Problem J5/S2
============================================================

 Modern Art
Problem Description
A new and upcoming artist has a unique way to create checkered patterns. The idea is to
use an M -by-N canvas which is initially entirely black. Then the artist re peatedly chooses
a row or column and runs their magic brush along the row or colu mn. The brush changes
the colour of each cell in the row or column from black to gold o r gold to black.
Given the artist’s choices, your job is to determine how much gold appears in the pattern
determined by these choices.
Input Speciﬁcation
The ﬁrst line of input will be a positive integer M . The second line of input will be a positive
integer N . The third line of input will be a positive integer K. The remaining input will be
K lines giving the choices made by the artist. Each of these lin es will either be R followed
by a single space and then an integer which is a row number, or C followed by a single space
and then an integer which is a column number. Rows are numbere d top down from 1 to M .
Columns are numbered left to right from 1 to N .
The following table shows how the available 15 marks are dist ributed.
1 mark M = 1 N = 1 K ≤ 100 only one cell, and
up to 100 choices by the artist
4 marks M = 1 N ≤ 100 K ≤ 100 only one row, and
up to 100 choices by the artist
5 marks M ≤ 100 N ≤ 100 K ≤ 100 up to 100 rows, up to 100 columns, and
up to 100 choices by the artist
5 marks M N ≤ 5 000 000 K ≤ 1 000 000 up to 5 000 000 cells, and
up to 1 000 000 choices by the artist
Output Speciﬁcation
Output one non-negative integer which is equal to the number of cells that are gold in the
pattern determined by the artist’s choices.
Sample Input 1
3
3
2
R 1
C 1
Output for Sample Input 1
4
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Explanation of Output for Sample Input 1
After running the brush along the ﬁrst row, the canvas looks li ke this:
GGG
BBB
BBB
Then after running the brush along the ﬁrst column, four cell s are gold in the ﬁnal pattern
determined by the artist’s choices:
BGG
GBB
GBB
Sample Input 2
4
5
7
R 3
C 1
C 2
R 2
R 2
C 1
R 4
Output for Sample Input 2
10
Explanation of Output for Sample Input 2
Ten cells are gold in the ﬁnal pattern determined by the artis t’s choices:
BGBBB
BGBBB
GBGGG
GBGGG
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Probl` eme J5/S2 : L’art moderne
´Enonc´ e du probl` eme
Un nouvel artiste a d´ evelopp´ e une fa¸ con unique de cr´ eer des motifs en damier. L’artiste se
procure d’abord une toile de couleur noire et de dimensions M × N . Ensuite, l’artiste choisit
` a plusieurs reprises une rang´ ee ou une colonne et donne un c oup de son pinceau magique le
long de la rang´ ee ou de la colonne. Le pinceau change la coule ur de chaque case de la rang´ ee
ou de la colonne du noir ` a l’or ou de l’or au noir.
´Etant donn´ e les choix de l’artiste, votre tˆ ache consiste `a d´ eterminer le nombre de cases dor´ ees
qui paraissent dans le motif en damier r´ esultant.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
La premi` ere ligne des donn´ ees d’entr´ ee ne contient qu’unseul entier strictement positif, soit
M . La deuxi` eme ligne des donn´ ees d’entr´ ee ne contient qu’un seul entier strictement positif,
soit N . La troisi` eme ligne des donn´ ees d’entr´ ee ne contient qu’un seul entier strictement posi-
tif, soit K. Le restant des donn´ ees d’entr´ ee sera compos´ e deK lignes ; ces lignes repr´ esentant
les choix de l’artiste. Chacune de ces K lignes commencera par R ou par C (indiquant res-
pectivement une rang´ ee ou une colonne) suivi d’un seul espa ce puis d’un entier strictement
positif inf´ erieur ou ´ egal ` aN . Cet entier repr´ esente le num´ ero d’une rang´ ee ou d’une colonne.
Les rang´ ees sont num´ erot´ ees de haut en bas de 1 ` a M . Les colonnes sont num´ erot´ ees de
gauche ` a droite de 1 ` a N .
Le tableau suivant indique la mani` ere dont les 15 points dis ponibles sont r´ epartis.
1 point M = 1 N = 1 K ≤ 100 Une seule case, et
usqu’` a 100 choix de l’artiste
4 points M = 1 N ≤ 100 K ≤ 100 Une seule rang´ ee, et
jusqu’` a 100 choix de l’artiste
5 points M ≤ 100 N ≤ 100 K ≤ 100
Jusqu’` a 100 rang´ ees, et
jusqu’` a 100 colonnes, et
jusqu’` a 100 choix de l’artiste
5 points M N ≤ 5 000 000 K ≤ 1 000 000 Jusqu’` a 5 000 000 cases, et
jusqu’` a 1 000 000 choix de l’artiste
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sortie ne devraient contenir qu’un seul enti er non n´ egatif. Cet entier est ´ egal
au nombre de cases dor´ ees dans le motif en damier r´ esultant des choix de l’artiste.
English version appears before the French version

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2021CCCJuniorTestData", "j5")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2021 Problem J5/S2
    
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