"""
CCC 2025 Junior - Problem J1
============================================================

 Roller Coaster Ride
Problem Description
You are spending the day at the CEMC’s funfair. One of the rides
at the funfair is a roller coaster which has one train with a number
of cars. Each car holds the same number of people.
When you arrive at the roller coaster, you see that there is a line.
Your job is to determine whether or not you will be on the next
train ride, assuming that every car is fully occupied for every ride.
Input Speciﬁcation
The ﬁrst line of input contains a positive integer, N, representing your place in line. For
example, if N is 5 then you are the ﬁfth person in line.
The second line contains a positive integer, C, representing the number of cars the train has.
The third line contains a positive integer, P , representing the number of people a single car
holds.
Output Speciﬁcation
Output either yes or no, indicating whether or not you will be on the next train ride.
Sample Input 1
14
3
2
Output for Sample Input 1
no
Explanation of Output for Sample Input 1
The train has 3 cars and each car holds 2 people. Therefore, 6 people can ride the next
train. Since you are the 14th person in line, you will not be on the next train ride.
Sample Input 2
12
4
3
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Output for Sample Input 2
yes
Explanation of Output for Sample Input 2
The train has 4 cars and each car holds 3 people. Therefore, 12 people can ride the next
train. Since you are the 12th person in line, you will be on the next train ride.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Probl` eme J1 : Montagnes russes
´Enonc´ e du probl` eme
Vous passez la journ´ ee ` a la fˆ ete foraine du CEMI. L’un des man` eges
` a la fˆ ete foraine est une montagne russe avec un train compos´ e de
plusieurs wagons. Chaque wagon peut transporter le mˆ eme nombre
de personnes.
Lorsque vous arrivez au man` ege, vous constatez qu’il y a une ﬁle
d’attente. Votre tˆ ache consiste ` a d´ eterminer si vous pourrez monter
` a bord du prochain train, en supposant que, tous les tours, tous les
wagons sont enti` erement occup´ es.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
La premi` ere ligne des donn´ ees d’entr´ ee contient un entier strictement positif,N, repr´ esentant
votre rang dans la ligne. Par exemple, si N est ´ egal ` a 5, vous ˆ etes la cinqui` eme personne
dans la ﬁle d’attente.
La deuxi` eme ligne des donn´ ees d’entr´ ee contient un entier strictement positif,W , repr´ esentant
le nombre de wagons du train.
La troisi` eme ligne des donn´ ees d’entr´ ee contient un entier strictement positif,P , repr´ esentant
le nombre de personnes dans un seul wagon.
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sorties devraient ˆ etreyes ou no, indiquant si vous serez ou non ` a bord du
prochain train.
Donn´ ees d’entr´ ee d’un 1er exemple
14
3
2
Donn´ ees de sortie du 1er exemple
no
Justiﬁcation des donn´ ees de sortie du 1er exemple
Le train est compos´ e de 3 wagons et chaque wagon contient 2 personnes. Par cons´ equent, 6
personnes monteront ` a bord du prochain train. Comme vous ˆ etes la 14e personne dans la ﬁle
d’attente, vous ne pourrez pas monter ` a bord du prochain train.
Donn´ ees d’entr´ ee du 2e exemple
12
4
3
English version appears before the French version
Donn´ ees de sortie du 2e exemple
yes
Justiﬁcation des donn´ ees de sortie du 2e exemple
Le train est compos´ e de 4 wagons et chaque wagon contient 3 personnes. Par cons´ equent,
12 personnes monteront ` a bord du prochain train. Comme vous ˆ etes la 12e personne dans la
ﬁle d’attente, vous pourrez monter ` a bord du prochain train.
English version appears before the French version

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2025CCCJuniorTestData", "j1")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2025 Problem J1
    
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