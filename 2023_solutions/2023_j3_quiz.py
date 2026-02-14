"""
CCC 2023 Junior - Problem J3
============================================================

 Special Event
Problem Description
You are trying to schedule a special event on one of ﬁve possible days.
Your job is to determine on which day you should schedule the event, so that the largest
number of interested people are able to attend.
Input Speciﬁcation
The ﬁrst line of input will contain a positive integer N, representing the number of people
interested in attending your event. The next N lines will each contain one person’s availabil-
ity using one character for each of Day 1, Day 2, Day 3, Day 4, and Day 5 (in that order).
The character Y means the person is able to attend and a period ( .) means the person is
not able to attend.
The following table shows how the available 15 marks are distributed:
Marks Description
6 There will be exactly one day on which every person will be able to
attend.
6 There will be exactly one day on which the largest number of people
will be able to attend.
3 There might be more than one day on which the largest number of
people will be able to attend.
Output Speciﬁcation
The output will consist of one line listing the day number(s) on which the largest number of
interested people are able to attend.
If there is more than one day on which the largest number of people are able to attend,
output all of these day numbers in increasing order and separated by commas (without
spaces).
Sample Input 1
3
YY.Y.
...Y.
.YYY.
Output for Sample Input 1
4
Explanation of Output for Sample Input 1
All three people are able to attend on Day 4, and they are not all available on any other day.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Sample Input 2
5
YY..Y
.YY.Y
.Y.Y.
.YY.Y
Y...Y
Output for Sample Input 2
2,5
Explanation of Output for Sample Input 2
There is no day on which all ﬁve people are able to attend. Four people are able to attend
on both Day 2 and Day 5.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Probl` eme J3 :´Ev´ enement sp´ ecial
´Enonc´ e du probl` eme
Un ´ ev´ enement sp´ ecial aura lieu lors d’une journ´ ee. Vous devez choisir parmi 5 jours la journ´ ee
pendant laquelle se tiendra cet ´ ev´ enement.
Votre tˆ ache consiste ` a d´ eterminer le jour pendant lequel l’´ ev´ enement devrait avoir lieu, de
sorte que le plus grand nombre de personnes int´ eress´ ees puissent y assister.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
La premi` ere ligne des donn´ ees d’entr´ ee doit contenir un entier strictement positifN, repr´ esentant
le nombre de personnes qui sont int´ eress´ ees ` a assister ` a l’´ ev´ enement. Chacune desN lignes
suivantes indiquera la disponibilit´ e d’une personne ` a l’aide d’un caract` ere pour chacun des
jours suivants : jour 1, jour 2, jour 3, jour 4 et jour 5 (dans cet ordre). Le caract` ereY signiﬁe
que la personne peut assister ` a l’´ ev´ enement tandis que le point (.) signiﬁe que la personne
ne peut pas assister ` a l’´ ev´ enement.
Le tableau suivant indique la mani` ere dont les 15 points disponibles sont r´ epartis.
Points Description
6 Il y aura exactement un jour o` u chaque personne pourra assister ` a
l’´ ev´ enement.
6 Il y aura exactement un jour o` u le plus grand nombre de personnes
pourra assister ` a l’´ ev´ enement.
3 Il se peut qu’il y ait plus d’un jour o` u le plus grand nombre de personnes
pourra assister ` a l’´ ev´ enement.
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sortie devraient contenir une seule ligne ´ enum´ erant le(s) num´ ero(s) de jour
auquel (auxquels) le plus grand nombre de personnes pourra assister ` a l’´ ev´ enement.
S’il y a plus d’un jour o` u le plus grand nombre de personnes pourrait assister ` a la conf´ erence,
tous les num´ eros de jour seront aﬃch´ es par ordre croissant et s´ epar´ es par des virgules (sans
espaces).
Donn´ ees d’entr´ ee d’un 1er exemple
3
YY.Y.
...Y.
.YYY.
Donn´ ees de sortie du 1er exemple
4
English version appears before the French version
Justiﬁcation des donn´ ees de sortie du 1er exemple
Les trois personnes peuvent assister ` a l’´ ev´ enement au jour 4 et il n’y a aucun autre jour o` u
elles seraient toutes les trois disponibles.
Donn´ ees d’entr´ ee d’un 2e exemple
5
YY..Y
.YY.Y
.Y.Y.
.YY.Y
Y...Y
Donn´ ees de sortie du 2e exemple
2,5
Justiﬁcation des donn´ ees de sortie du 2e exemple
Il n’y a aucun jour o` u les cinq personnes sont toutes disponibles. Cependant, quatre personnes
peuvent assister ` a l’´ ev´ enement aux jours 2 et 5.
English version appears before the French version

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2023CCCJuniorTestData", "j3")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2023 Problem J3
    
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