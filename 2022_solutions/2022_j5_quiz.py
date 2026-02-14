"""
CCC 2022 Junior - Problem J5
============================================================

 Square Pool
Problem Description
Ron wants to build a square pool in his square N-by-N yard, but his yard contains T trees.
Your job is to determine the side length of the largest square pool he can build.
Input Speciﬁcation
The ﬁrst line of input will be an integer N with N ≥ 2. The second line will be the positive
integer T where T < N 2. The remaining input will be T lines, each representing the location
of a single tree. The location is given by two positive integers, R and then C, separated by
a single space. Each tree is located at row R and column C where rows are numbered from
top to bottom from 1 to N and columns are numbered from left to right from 1 to N. No
two trees are at the same location.
The following table shows how the available 15 marks are distributed.
Marks Awarded Length/Width of Yard Number of Trees
3 marks N ≤ 50 T = 1
5 marks N ≤ 50 T ≤ 10
4 marks N ≤ 500 000 T ≤ 10
3 marks N ≤ 500 000 T ≤ 100
Output Speciﬁcation
Output one line containing M which is the largest positive integer such that some M-by-M
square contained entirely in Ron’s yard does not contain any of the T trees.
Sample Input 1
5
1
2 4
Output for Sample Input 1
3
Explanation of Output for Sample Input 1
A picture of the yard is below. The location of the tree is marked by
 and one of several
3-by-3 squares that do not contain the tree is highlighted. All larger squares contain a tree.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Sample Input 2
15
8
4 7
4 1
14 11
10 6
13 4
4 10
10 3
9 14
Output for Sample Input 2
7
Explanation of Output for Sample Input 2
A picture of the yard is below. The location of each tree is marked by
 and one of several
7-by-7 squares that do not contain a tree is highlighted. All larger squares contain a tree.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Probl` eme J5 : Piscine carr´ ee
´Enonc´ e du probl` eme
Ron veut construire une piscine carr´ ee dans sa cour carr´ ee. Sa cour est de dimensionsN × N
et contient T arbres. Votre tˆ ache consiste ` a d´ eterminer la longueur des cˆ ot´ es de la plus grande
piscine carr´ ee qu’il puisse construire tout en ´ evitant chacun desT arbres.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
La premi` ere ligne des donn´ ees d’entr´ ee ne contient qu’un seul entierN (N ≥ 2). La deuxi` eme
ligne contient l’entier strictement positifT tel que T < N 2. Cette deuxi` eme ligne est suivie de
T lignes ; chacune de ces derni` eres indiquant l’emplacement d’un seul arbre. L’emplacement
est indiqu´ e ` a l’aide de deux entiers strictement positifs, soit R suivi de C, les deux ´ etant
s´ epar´ es par un espace. Chaque arbre est situ´ e ` a la rang´ eeR et la colonne C. Les rang´ ees
sont num´ erot´ ees de 1 ` aN de haut en bas tandis que les colonnes sont num´ erot´ ees de 1 ` a
N de gauche ` a droite. On ne peut avoir deux arbres quelconques qui soient situ´ es au mˆ eme
endroit.
Le tableau suivant indique la mani` ere dont les 15 points disponibles sont r´ epartis.
Attribution des points Longueur/Largeur de la cour Nombre d’arbres
3 points N ≤ 50 T = 1
5 points N ≤ 50 T ≤ 10
4 points N ≤ 500 000 T ≤ 10
3 points N ≤ 500 000 T ≤ 100
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sortie devraient aﬃcher l’entier strictement positifM. Cet entier repr´ esente
la longueur des cˆ ot´ es de la plus grande piscine carr´ ee (qui est donc de dimensionsM × M)
que Ron puisse construire dans sa cour tout en ´ evitant chacun des T arbres.
Donn´ ees d’entr´ ee d’un 1er exemple
5
1
2 4
Donn´ ees de sortie du 1er exemple
3
Justiﬁcation des donn´ ees de sortie du 1er exemple
On voit une ﬁgure de la cour ` a droite. L’emplacement de l’arbre est indiqu´ e
par
 . De plus, un carr´ e de dimensions 3× 3 est surlign´ e. Ce carr´ e est l’un
de plusieurs emplacements possibles o` u l’on pourrait construire une piscine
carr´ ee de dimensions 3× 3 tout en ´ evitant l’arbre. On ne peut construire
une piscine carr´ ee plus grande qui ´ eviterait cet arbre.
English version appears before the French version.
Donn´ ees d’entr´ ee d’un 2e exemple
15
8
4 7
4 1
14 11
10 6
13 4
4 10
10 3
9 14
Donn´ ees de sortie du 2e exemple
7

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2022CCCJuniorTestData", "j5")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2022 Problem J5
    
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