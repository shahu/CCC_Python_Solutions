"""
CCC 2023 Junior - Problem J4/S1
============================================================

 Trianglane
Problem Description
Bocchi the Builder just ﬁnished constructing her latest project: a laneway consisting of two
rows of white equilateral triangular tiles. However, at the last moment, disaster struck! She
accidentally spilled black paint on some of the tiles. Now, some of the tiles are wet and the
other tiles are dry. Bocchi must place warning tape around the perimeters of all wet areas.
Can you help her determine how many metres of tape she needs?
The ﬁrst triangular tile will point upwards. Each pair of adjacent tiles (that is, tiles that
share a common side) will point in opposite directions. Each tile has a side length of 1 metre.
Input Speciﬁcation
The ﬁrst line of input will consist of one positive integer C, representing the number of
columns.
The next two lines will each consist ofC integers separated by spaces. Each integer represents
the colour of a tile along the laneway, with 1 indicating that the tile is black (wet) and 0
indicating that the tile is white (dry).
The following table shows how the available 15 marks are distributed:
Marks Description Bound
3 The laneway is not very long, black tiles are never adjacent
and the second row is fully white.
C ≤ 2 000
3 The laneway is not very long, black tiles may be adjacent
and the second row is fully white.
C ≤ 2 000
5 The laneway is not very long, black tiles may be adjacent
and may appear in the second row.
C ≤ 2 000
4 The laneway may be very long, black tiles may be adjacent
and may appear in the second row.
C ≤ 200 000
Output Speciﬁcation
Output a single integer representing the length of tape Bocchi needs, in metres.
Sample Input 1
5
1 0 1 0 1
0 0 0 0 0
Output for Sample Input 1
9
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Explanation of Output for Sample Input 1
The tiles are painted as follows, creating three wet areas. Bocchi will need 9 metres of
warning tape as shown in yellow.
Sample Input 2
7
0 0 1 1 0 1 0
0 0 1 0 1 0 0
Output for Sample Input 2
11
Explanation of Output for Sample Input 2
The tiles are painted as follows, creating three wet areas. Bocchi will need 5 metres of
warning tape to surround one area and 3 metres of warning tape to surround each of the
other two areas as shown in yellow.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Probl` eme J4/S1 : All´ ee de triangles
´Enonc´ e du probl` eme
Bocchi la Bˆ atisseuse vient de terminer la construction de son dernier projet : une all´ ee com-
pos´ ee de deux rang´ ees de tuiles triangulaires ´ equilat´ erales blanches. Cependant, au dernier
moment, le d´ esastre a frapp´ e ! Elle a accidentellement renvers´ e de la peinture noire sur cer-
taines des tuiles. Par cons´ equent, certaines des tuiles sont humides tandis que d’autres sont
s` eches. Bocchi doit placer du ruban de signalisation autour du p´ erim` etre de toutes les surfaces
humides. Pouvez-vous l’aider ` a d´ eterminer le nombre de m` etres de ruban de signalisation
dont elle aura besoin ?
La premi` ere tuile triangulaire sera orient´ ee vers le haut. Les tuiles de chaque paire de tuiles
adjacentes (soit les tuiles qui partagent un cˆ ot´ e commun) seront orient´ ees dans des directions
oppos´ ees. Les cˆ ot´ es de chaque tuile mesurent 1 m` etres.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
La premi` ere ligne des donn´ ees d’entr´ ee doit contenir un entier strictement positifC, repr´ esentant
le nombre de colonnes.
Chacune des deux lignes suivantes doit contenir C entiers, chacun des entiers ´ etant s´ epar´ e
des autres par un espace simple. Chaque entier repr´ esente la couleur d’une tuile le long de
l’all´ ee, 1 indiquant que la tuile est noire (humide) et 0 indiquant que la tuile est blanche
(s` eche).
Le tableau suivant indique la mani` ere dont les 15 points disponibles sont r´ epartis.
Points Description Bornes
3 L’all´ ee n’est pas tr` es longue, les tuiles noires ne sont jamais
adjacentes et la seconde rang´ ee est enti` erement blanche.
C ≤ 2 000
3 L’all´ ee n’est pas tr` es longue, les tuiles noires peuvent ˆ etre
adjacentes et la seconde rang´ ee est enti` erement blanche.
C ≤ 2 000
5 L’all´ ee n’est pas tr` es longue, les tuiles noires peuvent ˆ etre
adjacentes et peuvent paraitre dans la seconde rang´ ee.
C ≤ 2 000
4 L’all´ ee peut ˆ etre tr` es longue, les tuiles noires peuvent ˆ etre
adjacentes et peuvent paraitre dans la seconde rang´ ee.
C ≤ 200 000
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sortie devraient contenir un seul entier repr´ esentant le nombre de m` etres de
ruban de signalisation dont Bocchi aura besoin.
English version appears before the French version
Donn´ ees d’entr´ ee d’un 1er exemple
5
1 0 1 0 1
0 0 0 0 0
Donn´ ees de sortie du 1er exemple
9
Justiﬁcation des donn´ ees de sortie du 1er exemple
Les tuiles sont peintes comme dans la ﬁgure ci-dessous, cr´ eant ainsi trois surfaces humides
s´ epar´ ees. Bocchi aura besoin de 9 m` etres de ruban de signalisation (le ruban ´ etant repr´ esent´ e
par les lignes jaunes).
Donn´ ees d’entr´ ee d’un 2e exemple

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2023CCCJuniorTestData", "s1j4")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2023 Problem J4/S1
    
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