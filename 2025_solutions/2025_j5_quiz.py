"""
CCC 2025 Junior - Problem J5
============================================================

 Connecting Territories
Problem Description
Ava is playing a strategic game on a grid of tiles.
Each tile has an associated cost. When the costs
of the tiles are read from left to right, starting
with the ﬁrst row, a repeating pattern of the ﬁrst
M positive integers in increasing order is revealed:
1, 2, 3, . . . , M,1, 2, 3, . . . , M,1, 2, 3, . . .. In this pattern,
M represents the maximum cost of a tile. In the grid
of tiles shown, M is equal to 5.
Ava needs to purchase one tile in each row in order to
make a connecting path from the upper territory (above
the ﬁrst row of tiles) to the lower territory (below the
last row of tiles). The ﬁrst tile purchased must be in
the ﬁrst row. Each subsequently purchased tile must
share either an edge or a corner with the tile purchased
previously. In the grid of tiles shown, the cost of Ava’s
connecting path is 9.
Given a grid of tiles, your job is to determine the mini-
mum cost of a connecting path between the upper and
lower territories.
Input Speciﬁcation
The ﬁrst line of input contains a positive integer, R, representing the number of rows in the
grid. The second line contains a positive integer, C, representing the number of columns in
the grid. The third line contains a positive integer, M where M ≤ 100 000, representing the
maximum cost of a tile.
The following table shows how the available 15 marks are distributed:
Marks Description Bounds
3 There are two rows and at most ten columns. R = 2 and C ≤ 10
8 There are at most ten rows and at most ten columns. R ≤ 10 and C ≤ 10
2 There are at most 100 rows and at most 100 columns. R ≤ 100 and C ≤ 100
2 The grid may be very large. R ≤ 20 000 and C ≤ 20 000
Output Speciﬁcation
Output the positive integer, P , which is the minimum cost of a connecting path between the
upper and lower territories.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Sample Input
3
5
7
Output for Sample Input
6
Explanation of Output for Sample Input
The cost of each tile is shown. The sequence of tiles that Ava should purchase to minimize
the cost of a connecting path is highlighted in green.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Probl` eme J5 : Jonction de territoires
´Enonc´ e du probl` eme
`Eve joue ` a un jeu de strat´ egie sur une grille de
cases. Un coˆ ut est associ´ e ` a chaque case. La lecture
de gauche ` a droite et de haut en bas du coˆ ut des
cases en commen¸ cant par la case en haut ` a gauche
r´ ev` ele une suite ﬁnie croissante des M premiers en-
tiers strictement positifs qui se r´ ep` ete comme suit :
1, 2, 3, . . . , M,1, 2, 3, . . . , M,1, 2, 3, . . . Dans ce sch´ ema,
M repr´ esente le coˆ ut maximal d’une case. Dans l’illus-
tration de la grille de cases, M est ´ egal ` a 5.
`Eve doit acheter une case dans chaque rang´ ee aﬁn de
cr´ eer un chemin de jonction entre le territoire du haut
(au-dessus de la premi` ere rang´ ee de cases) et le territoire
du bas (en dessous de la derni` ere rang´ ee de cases). La
premi` ere case achet´ ee doit se trouver dans la premi` ere
rang´ ee. Ensuite, chaque case achet´ ee doit partager un
bord ou un coin avec la case pr´ ec´ edente. Dans l’illustra-
tion de la grille de cases, le coˆ ut du chemin de jonction
d’`Eve est de 9.
`A l’aide de la grille de cases, votre tˆ ache consiste ` a
d´ eterminer le coˆ ut minimum d’un chemin de jonction
entre le territoire du haut et le territoire du bas.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
La premi` ere ligne de donn´ ees d’entr´ ee contient un entier strictement positif,R, repr´ esentant
le nombre de rang´ ees de la grille. La deuxi` eme ligne de donn´ ees d’entr´ ee contient un entier
strictement positif, C, repr´ esentant le nombre de colonnes de la grille. La troisi` eme ligne de
donn´ ees d’entr´ ee contient un entier strictement positif,M (M ≤ 100 000), repr´ esentant le
coˆ ut maximal d’une case.
Le tableau suivant d´ etaille la r´ epartition des 15 points disponibles.
Points Description Bornes
3 Il y a deux rang´ ees et au plus dix colonnes. R = 2 et C ≤ 10
8 Il y a au plus dix rang´ ees et au plus dix colonnes. R ≤ 10 et C ≤ 10
2 Il y a au plus 100 rang´ ees et au plus 100 colonnes. R ≤ 100 et C ≤ 100
2 La grille peut ˆ etre tr` es grande. R ≤ 20 000 et C ≤ 20 000
English version appears before the French version
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sortie devraient contenir un entier strictement positif,P , repr´ esentant le coˆ ut
minimum d’un chemin de jonction entre le territoire du haut et le territoire du bas.
Donn´ ees d’entr´ ee
3
5
7
Donn´ ees de sortie
6
Justiﬁcation des donn´ ees de sortie
Le coˆ ut de chaque case est indiqu´ e. Les cases qu’`Eve doit acheter pour minimiser le coˆ ut de
son chemin de jonction sont surlign´ ees en vert.
English version appears before the French version

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2025CCCJuniorTestData", "j5")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2025 Problem J5
    
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