"""
CCC 2023 Junior - Problem J1
============================================================

 Deliv-e-droid
Problem Description
In the game, Deliv-e-droid, a robot droid has to deliver packages while avoiding obstacles.
At the end of the game, the ﬁnal score is calculated based on the following point system:
• Gain 50 points for every package delivered.
• Lose 10 points for every collision with an obstacle.
• Earn a bonus 500 points if the number of packages delivered is greater than the number
of collisions with obstacles.
Your job is to determine the ﬁnal score at the end of a game.
Input Speciﬁcation
The input will consist of two lines. The ﬁrst line will contain a non-negative integer P ,
representing the number of packages delivered. The second line will contain a non-negative
integer C, representing the number of collisions with obstacles.
Output Speciﬁcation
The output will consist of a single integer F , representing the ﬁnal score.
Sample Input 1
5
2
Output for Sample Input 1
730
Explanation of Output for Sample Input 1
There are 5 packages delivered, so 5 × 50 = 250 points are gained. There are 2 collisions, so
2 × 10 = 20 points are lost. Since 5 > 2, a bonus 500 points are earned. Therefore, the ﬁnal
score is 250 − 20 + 500 = 730.
Sample Input 2
0
10
Output for Sample Input 2
-100
Explanation of Output for Sample Input 2
There are 0 packages delivered, so 0 × 50 = 0 points are gained. There are 10 collisions, so
10 × 10 = 100 points are lost. Since 0 ≤ 10, no bonus points are earned. Therefore, the ﬁnal
score is 0 − 100 + 0 = −100.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Probl` eme J1 : Livr-` a-dro¨ ıde
´Enonc´ e du probl` eme
Dans le jeu Livr-` a-dro¨ ıde, un dro¨ ıde robot doit livrer des colis tout en ´ evitant des obstacles.
`A la ﬁn du jeu, le score ﬁnal est calcul´ e en fonction du syst` eme de points suivant :
— Vous gagnez 50 points pour chaque colis livr´ e.
— Vous perdez 10 points pour chaque collision avec un obstacle.
— Vous gagnez un bonus de 500 points si le nombre de colis livr´ es est sup´ erieur au
nombre de collisions avec des obstacles.
Votre tˆ ache consiste ` a d´ eterminer le score ﬁnal ` a la ﬁn d’une partie.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
Les donn´ ees d’entr´ ee ne contiennent que deux lignes. La premi` ere ligne doit contenir un
entier non n´ egatifP , repr´ esentant le nombre de colis livr´ es. La seconde ligne doit contenir
un entier non n´ egatifC, repr´ esentant le nombre de collisions avec des obstacles.
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sortie ne devraient contenir qu’un seul entierF , repr´ esentant le score ﬁnal.
Donn´ ees d’entr´ ee d’un 1er exemple
5
2
Donn´ ees de sortie du 1er exemple
730
Justiﬁcation des donn´ ees de sortie du 1er exemple
Puisqu’il y a 5 colis qui sont livr´ es, alors 5 × 50 = 250 points sont gagn´ es. Puisqu’il y a 2
collisions, alors 2 × 10 = 20 points sont perdus. Puisque 5 > 2, alors le bonus de 500 points
est accord´ e. Donc, le score ﬁnal est ´ egal ` a 250− 20 + 500 = 730.
Donn´ ees d’entr´ ee d’un 2e exemple
0
10
Donn´ ees de sortie du 2e exemple
-100
Justiﬁcation des donn´ ees de sortie du 2e exemple
Puisqu’il y a 0 colis qui sont livr´ es, alors 0 × 50 = 0 points sont gagn´ es. Puisqu’il y a 10
collisions, alors 10 × 10 = 100 points sont perdus. Puisque 0 ≤ 10, le bonus de 500 points
n’est pas accord´ e. Donc, le score ﬁnal est ´ egal ` a 0− 100 + 0 = −100.
English version appears before the French version

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2023CCCJuniorTestData", "j1")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2023 Problem J1
    
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