"""
CCC 2022 Junior - Problem J2
============================================================

 Fergusonball Ratings
Problem Description
Fergusonball players are given a star rating based on the number of points that they score
and the number of fouls that they commit. Speciﬁcally, they are awarded 5 stars for each
point scored, and 3 stars are taken away for each foul committed. For every player, the
number of points that they score is greater than the number of fouls that they commit.
Your job is to determine how many players on a team have a star rating greater than 40.
You also need to determine if the team is considered a gold team which means that all the
players have a star rating greater than 40.
Input Speciﬁcation
The ﬁrst line of input consists of a positive integerN representing the total number of players
on the team. This is followed by a pair of consecutive lines for each player. The ﬁrst line
in a pair is the number of points that the player scored. The second line in a pair is the
number of fouls that the player committed. Both the number of points and the number of
fouls, are non-negative integers.
Output Speciﬁcation
Output the number of players that have a star rating greater than 40, immediately followed
by a plus sign if the team is considered a gold team.
Sample Input 1
3
12
4
10
3
9
1
Output for Sample Input 1
3+
Explanation of Output for Sample Input 1
The image shows the star rating for each player.
For example, the star rating for the ﬁrst player is
12×5−4×3 = 48. All three players have a rating
greater than 40 so the team is considered a gold
team.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Sample Input 2
2
8
0
12
1
Output for Sample Input 2
1
Explanation of Output for Sample Input 2
The image shows the star rating for each player.
Since only one of the two players has a rating
greater than 40, this team is not considered a gold
team.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Probl` eme J2 : Classements de Fergusonball
´Enonc´ e du probl` eme
Les joueurs de Fergusonball re¸ coivent un classement bas´ e sur le nombre de points qu’ils
marquent et le nombre de fautes qu’ils commettent. Plus pr´ ecis´ ement, leur classement aug-
mente de 5 points pour chaque point marqu´ e et diminue de 3 points pour chaque faute com-
mise. Pour un quelconque joueur, le nombre de points qu’il a marqu´ e est toujours sup´ erieur
au nombre de fautes qu’il a commis.
Votre tˆ ache consiste ` a d´ eterminer combien de joueurs parmi une ´ equipe ont un classement
sup´ erieur ` a 40. Vous devez ´ egalement d´ eterminer si l’´ equipe est une´ equipe en or; c’est-` a-dire
une ´ equipe dont chacun des joueurs a un classement sup´ erieur ` a 40.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
La premi` ere ligne des donn´ ees d’entr´ ee ne contient qu’un seul entier strictement positifN
repr´ esentant le nombre total de joueurs dans l’´ equipe. Cette ligne est suivie d’un couple de
lignes cons´ ecutives pour chaque joueur. La premi` ere ligne d’un couple est le nombre de points
que le joueur a marqu´ es. La seconde ligne d’un couple est le nombre de fautes commises par
le joueur. Le nombre de points marqu´ es et le nombre de fautes commises sont des entiers
non n´ egatifs.
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sortie devraient aﬃcher le nombre de joueurs ayant un classement sup´ erieur
` a 40, suivi imm´ ediatement d’un signe plus si l’´ equipe est une ´ equipe en or.
Donn´ ees d’entr´ ee d’un 1er exemple
3
12
4
10
3
9
1
Donn´ ees de sortie du 1er exemple
3+
Justiﬁcation des donn´ ees de sortie du
1er exemple
Dans la ﬁgure ci-contre, on voit le classement de
chaque joueur. Par exemple, le premier joueur a
un classement de 12×5 −4 ×3 = 48. Puisque cha-
cun des trois joueurs a un classement sup´ erieur ` a
40, alors l’´ equipe est une ´ equipe en or.
English version appears before the French version.
Donn´ ees d’entr´ ee d’un 2e exemple
2
8
0
12
1
Donn´ ees de sortie du 2e exemple
1
Justiﬁcation des donn´ ees de sortie du
2e exemple
Dans la ﬁgure ci-contre, on voit le classement de
chaque joueur. L’´ equipe n’est pas une ´ equipe en or
puisqu’un seul des deux joueurs a un classement

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2022CCCJuniorTestData", "j2")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2022 Problem J2
    
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