"""
CCC 2024 Junior - Problem J5
============================================================

 Harvest Waterloo
Problem Description
There is a wildly popular new harvest simulation game called Harvest Waterloo . The game
is played on a rectangular pumpkin patch which contains bale s of hay and pumpkins of
diﬀerent sizes. To begin the game, a farmer is placed at the lo cation of a pumpkin.
The farmer harvests all pumpkins they can reach by moving lef t, right, up, and down through-
out the patch. The farmer cannot move diagonally. The farmer can also not move through
a bale of hay nor move outside of the patch.
Your job is to determine the total value of all the pumpkins ha rvested by the farmer. A
small pumpkin is worth $1, a medium pumpkin is worth $5, and a large pumpkin is worth
$10 dollars.
Input Speciﬁcation
The ﬁrst line of input is an integer R > 0 which is the number of rows within the patch.
The second line of input is an integer C > 0 which is the number of columns within the
patch.
The next R lines describe the patch. Each line will contain C characters and each character
will either represent a pumpkin size or a bale of hay: S for a small pumpkin, M for a medium
pumpkin, L for a large pumpkin, or * for a bale of hay.
The next line of input is an integer A where 0 ≤ A < R , and the last line of input is an
integer B where 0 ≤ B < C . Row A and column B is the starting location of the farmer
and the top-left corner of the patch is row 0 and column 0.
The following table shows how the available 15 marks are dist ributed:
Marks Description Bound
1 The patch is small and there are no bales of hay. R × C ≤ 100
4 The patch is small and the bales of hay divide the entire
patch into rectangular areas.
R × C ≤ 100
5 The patch is small and the bales of hay can be anywhere. R × C ≤ 100
5 The patch is large and the bales of hay can be anywhere. R × C ≤ 100 000
Output Speciﬁcation
Output the integer, V , which is the total value in dollars of all the pumpkins harve sted by
the farmer.
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Sample Input 1
6
6
**LMLS
S*LMMS
S*SMSM
******
LLM*MS
SSL*SS
5
1
Output for Sample Input 1
37
Explanation of Output for Sample Input 1
Starting at row 5 and column 1, the farmer can reach the 6 pumpk ins in the highlighted
area. They harvest 2 small pumpkins, 1 medium pumpkin, and 3 l arge pumpkins. The total
value in dollars of this harvest is 2 × 1 + 1 × 5 + 3 × 10 = 37.
Sample Input 2
6
6
**LMLS
S*LMMS
S*SMSM
***SLL
LLM*MS
SSL*SS
2
4
Output for Sample Input 2
88
Explanation of Output for Sample Input 2
Starting at row 2 and column 4, the farmer can reach the 19 pump kins in the highlighted
area. They harvest 8 small pumpkins, 6 medium pumpkin, and 5 l arge pumpkins. The total
value in dollars of this harvest is 8 × 1 + 6 × 5 + 5 × 10 = 88.
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Probl` eme J5 : R´ ecolte Waterloo
´Enonc´ e du probl` eme
Le jeu R´ ecolte Waterlooest un nouveau jeu de simulation tr` es populaire. Le jeu se d´ eroule
dans un champ rectangulaire qui contient des bottes de foin e t des citrouilles de diﬀ´ erentes
tailles. Au d´ ebut du jeu, un fermier est positionn´ e l` a o` u se trouve une citrouille.
Le fermier r´ ecolte toutes les citrouilles qu’il peut attei ndre en se d´ epla¸ cant vers la gauche, la
droite, en haut ou en bas dans le champ. Il ne peut se d´ eplacer en diagonale, traverser une
botte de foin, ni sortir des limites du champ.
Votre tˆ ache consiste ` a d´ eterminer la valeur totale des citrouilles que le fermier a r´ ecolt´ ees.
Une petite citrouille vaut 1 $, une citrouille moyenne vaut 5 $ et une grande citrouille vaut
10 $.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
La premi` ere ligne des donn´ ees d’entr´ ee contient un entier R > 0, repr´ esentant le nombre de
rang´ ees dans le champ.
La deuxi` eme ligne des donn´ ees d’entr´ ee contient un entier C > 0, repr´ esentant le nombre de
colonnes dans le champ.
Les R lignes suivantes d´ ecrivent le champ. Chacune de ces lignes contient C caract` eres et
chaque caract` ere repr´ esente soit une taille de citrouill e, soit une botte de foin : S pour une
petite citrouille, M pour une citrouille moyenne, L pour une grande citrouille ou * pour une
botte de foin.
La ligne suivante des donn´ ees d’entr´ ee est un entierA (0 ≤ A < R ) et la derni` ere ligne des
donn´ ees d’entr´ ee est un entierB (0 ≤ B < C ). La rang´ eeA et la colonne B repr´ esentent
l’emplacement initial du fermier ; le coin sup´ erieur gauche du champ correspond ` a la rang´ ee
0 et ` a la colonne 0.
Le tableau ci-dessous d´ etaille la r´ epartition des 15 points disponibles.
Points Description Bornes
1 Le champ est petit et il n’y a pas de bottes de foin. R × C ≤ 100
4 Le champ est petit et les bottes de foin divisent le champ
en r´ egions rectangulaires.
R × C ≤ 100
5 Le champ est petit et les bottes de foin peuvent se trouver
n’importe o` u.

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2024CCCJuniorTestData", "j5")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2024 Problem J5
    
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