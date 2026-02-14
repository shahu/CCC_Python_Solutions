"""
CCC 2021 Junior - Problem J3
============================================================

 Secret Instructions
Problem Description
Professor Santos has decided to hide a secret formula for a ne w type of biofuel. She has,
however, left a sequence of coded instructions for her assis tant.
Each instruction is a sequence of ﬁve digits which represent s a direction to turn and the
number of steps to take.
The ﬁrst two digits represent the direction to turn:
• If their sum is odd, then the direction to turn is left.
• If their sum is even and not zero, then the direction to turn is right.
• If their sum is zero, then the direction to turn is the same as t he previous instruction.
The remaining three digits represent the number of steps to t ake which will always be at
least 100.
Your job is to decode the instructions so the assistant can us e them to ﬁnd the secret formula.
Input Speciﬁcation
There will be at least two lines of input. Each line except the last line will contain exactly
ﬁve digits representing an instruction. The ﬁrst line will n ot begin with 00. The last line
will contain 99999 and no other line will contain 99999.
Output Speciﬁcation
There must be one line of output for each line of input except t he last line of input. These
output lines correspond to the input lines (in order). Each o utput line gives the decoding of
the corresponding instruction: either right or left, followed by a single space, followed by
the number of steps to be taken in that direction.
Sample Input
57234
00907
34100
99999
Output for Sample Input
right 234
right 907
left 100
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Explanation of Output for Sample Input
The ﬁrst instruction is 57234 which is decoded as right 234 because 5 + 7 = 12 which is
even and 57 is followed by 234.
The second instruction is 00907 which is decoded with the same direction as the previous
instruction ( right) but with 907 steps.
The third instruction is 34100 which is decoded as left 100 because 3 + 4 = 7 which is odd
and 34 is followed by 100.
The last line contains 99999 which tells us these are the only three instructions.
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Probl` eme J3 : Des instructions secr` etes
´Enonc´ e du probl` eme
La professeure Santos a d´ ecid´ e de cacher une formule secr` ete pour un nouveau type de
biocarburant. Elle a cependant laiss´ e une s´ equence d’instructions cod´ ees pour son assistante.
Chaque instruction est compos´ ee d’une s´ equence de cinq chiﬀres. Ces chiﬀres indiquent une
direction vers laquelle il faut se tourner et un nombre de pas ` a eﬀectuer.
Les deux premiers chiﬀres repr´ esentent la direction vers l aquelle il faut se tourner :
– Si leur somme est impaire, alors il faut se tourner vers la ga uche.
– Si leur somme est paire et non nulle, alors il faut se tourner vers la droite.
– Si leur somme est nulle, alors il faut se tourner dans la mˆ em e direction que celle de
l’instruction pr´ ec´ edente.
Les trois chiﬀres restants repr´ esentent le nombre de pas ` a eﬀectuer (ce nombre sera toujours
sup´ erieur ou ´ egal ` a 100).
Votre tˆ ache consiste ` a d´ ecoder les instructions aﬁn que l’assistante puisse s’en servir pour
retrouver la formule secr` ete.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
Les donn´ ees d’entr´ ee contiennent au moins deux lignes. Ch aque ligne, ` a l’exception de la
derni` ere, contiendra exactement cinq chiﬀres repr´ esentant une instruction. La premi` ere ligne
ne peut commencer par 00. La derni` ere ligne contiendra 99999 et aucune autre ligne ne peut
contenir 99999.
Pr´ ecisions par rapport aux donn´ ees de sortie
Chaque ligne de donn´ ees d’entr´ ee doit avoir une ligne de donn´ ees de sortie correspondante (la
seule exception ´ etant la derni` ere ligne des donn´ ees d’entr´ ee). De plus, les lignes de donn´ ees
de sortie doivent ˆ etre dans le mˆ eme ordre que les lignes de donn´ ees d’entr´ ee auxquelles elles
correspondent. Chaque ligne de donn´ ees de sortie pr´ esente le d´ ecodage de l’instruction conte-
nue dans la ligne de donn´ ees d’entr´ ee correspondante : soit right (indiquant une direction
vers la droite) soit left (indiquant une direction vers la gauche), suivi d’un seul es pace,
suivi du nombre de pas ` a faire dans cette direction.
Exemple de donn´ ees d’entr´ ee
57234
00907
34100
99999
English version appears before the French version
Exemple de donn´ ees de sortie
right 234
right 907
left 100
Justiﬁcation des donn´ ees de sortie
La premi` ere ligne des donn´ ees d’entr´ ee, soit57234, repr´ esente les instructions right 234
car la somme des deux premiers chiﬀres, 5 + 7 = 12, est un nombre pair et 57 est suivi de
234.
La deuxi` eme ligne des donn´ ees d’entr´ ee, soit00907, repr´ esente les instructions right 907
car la somme des deux premiers chiﬀres est nulle (indiquant q u’il faut se tourner dans la
mˆ eme direction que celle de l’instruction pr´ ec´ edente) et ces chiﬀres sont suivi de 907.
La troisi` eme ligne des donn´ ees d’entr´ ee, soit34100, repr´ esente les instructionsleft 100 car
la somme des deux premiers chiﬀres, 3 + 4 = 7, est un nombre impa ir et 34 est suivi de 100.
La derni` ere ligne des donn´ ees d’entr´ ee contient99999 et signale la ﬁn des instructions. Donc,
cet exemple ne contenait que trois instructions.
English version appears before the French version

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2021CCCJuniorTestData", "j3")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2021 Problem J3
    
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