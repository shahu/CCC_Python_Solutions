"""
CCC 2024 Junior - Problem J3
============================================================

 Bronze Count
Problem Description
After completing a competition, you are struck with curiosit y. How many participants were
awarded bronze level?
Gold level is awarded to all participants who achieve the hig hest score. Silver level is awarded
to all participants who achieve the second highest score. Br onze level is awarded to all
participants who achieve the third highest score.
Given a list of all the scores, your job is to determine the sco re required for bronze level and
how many participants achieved this score.
Input Speciﬁcation
The ﬁrst line of input contains a positive integer, N , representing the number of participants.
Each of the next N lines of input contain a single integer representing a parti cipant’s score.
Each score is between 0 and 75 (inclusive) and there will be at least three distinct scores.
The following table shows how the available 15 marks are dist ributed:
Marks Description Bound
6 The scores are distinct and the number of participants is sma ll. N ≤ 50
7 The scores might not be distinct and the number of participan ts
is small.
N ≤ 50
2 The scores might not be distinct and the number of participan ts
could be large.
N ≤ 250 000
Output Speciﬁcation
Output a non-negative integer, S, and a positive integer, P , separated by a single space,
where S is the score required for bronze level and P is how many participants achieved this
score.
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Sample Input 1
4
70
62
58
73
Output for Sample Input 1
62 1
Explanation of Output for Sample Input 1
The score required for bronze level is 62 and one participant achieved this score.
Sample Input 2
8
75
70
60
70
70
60
75
70
Output for Sample Input 2
60 2
Explanation of Output for Sample Input 2
The score required for bronze level is 60 and two participant s achieved this score.
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Probl` eme J3 : Compte de bronze
´Enonc´ e du probl` eme
Apr` es la ﬁn d’une comp´ etition, une question vous intrigue : combien de personnes partici-
pantes se sont vu attribuer le niveau bronze ?
Le niveau or est d´ ecern´ e ` a toutes les personnes participantes qui ont obtenu le score le plus
´ elev´ e. Le niveau argent est d´ ecern´ e ` a toutes les personnes participantes qui ont obtenu le
deuxi` eme meilleur score. Le niveau bronze est attribu´ e ` a toutes les personnes participantes
qui obtiennent le troisi` eme meilleur score.
´Etant donn´ e une liste de tous les scores, votre tˆ ache consiste ` a d´ eterminer le score n´ ecessaire
pour atteindre le niveau bronze et le nombre de personnes par ticipantes qui ont r´ eussi ` a
l’obtenir.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
La premi` ere ligne des donn´ ees d’entr´ ee contient un entier strictement positif N , repr´ esentant
le nombre de personnes participantes.
Chacune des N lignes suivantes d’entr´ ee contient un seul entier repr´ esentant le score d’une
personne participante.
Chaque score est un entier de 0 ` a 75 (inclusivement) et il doi t y avoir au moins trois scores
distincts.
Le tableau ci-dessous d´ etaille la r´ epartition des 15 points disponibles.
Points Description Bornes
6 Les scores sont distincts et il y a peu de personnes participa ntes. N ≤ 50
7 Les scores ne sont pas n´ ecessairement distincts et il y a peu de
personnes participantes.
N ≤ 50
2 Les scores ne sont pas n´ ecessairement distincts et le nombr e de
personnes participantes peut ˆ etre ´ elev´ e.
N ≤ 250 000
English version appears before the French version
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sortie devraient aﬃcher un entier non n´ egatif S (le score requis pour atteindre
le niveau bronze) et un entier strictement positif P (le nombre de personnes participantes
ayant obtenu ce score), les deux ´ etant s´ epar´ es par un espace.
Donn´ ees d’entr´ ee d’un 1er exemple
4
70
62
58
73
Donn´ ees de sortie du 1er exemple
62 1
Justiﬁcation des donn´ ees de sortie du 1 er exemple
Le score requis pour atteindre le niveau bronze est 62 et une s eule personne participante a
obtenu ce score.
Donn´ ees d’entr´ ee d’un 2e exemple
8
75
70
60

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2024CCCJuniorTestData", "j3")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2024 Problem J3
    
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