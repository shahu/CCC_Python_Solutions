"""
CCC 2024 Junior - Problem J2
============================================================

 Dusa And The Yobis
Problem Description
Dusa eats Yobis, but only Yobis of a certain size.
If Dusa encounters a Yobi that is smaller than itself, it eats the Yobi, and absorbs its size.
For example, if Dusa is of size 10 and it encounters a Yobi of si ze 6, Dusa eats the Yobi and
expands to size 10 + 6 = 16.
If Dusa encounters a Yobi that is the same size as itself or lar ger, Dusa runs away without
eating the Yobi.
Dusa is currently facing a line of Yobis and will encounter th em in order. Dusa is guaranteed
to eventually encounter a Yobi that causes it to run away. You r job is to determine Dusa’s
size when this happens.
Input Speciﬁcation
The ﬁrst line of input contains a positive integer, D, representing Dusa’s starting size.
The remaining lines of input contain positive integers repr esenting the sizes of the Yobis in
order.
Output Speciﬁcation
Output the positive integer, R, which is Dusa’s size when it eventually runs away.
Sample Input 1
5
3
2
9
20
22
14
Output for Sample Input 1
19
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Explanation of Output for Sample Input 1
Dusa is large enough to eat the Yobi of size 3. This brings Dusa ’s size to 8. Dusa is large
enough to eat the Yobi of size 2. This brings Dusa’s size to 10. Dusa is large enough to eat
the Yobi of size 9. This brings Dusa’s size to 19. The Yobi of si ze 20 causes Dusa to run
away.
Sample Input 2
10
10
3
5
13
Output for Sample Input 2
10
Explanation of Output for Sample Input 2
The Yobi of size 10 causes Dusa to run away, leaving its size un changed.
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Probl` eme J2 : Dusa et les Yobis
Problem Description
Dusa se nourrit de Yobis, mais seulement de ceux d’une taille sp´ eciﬁque.
Lorsque Dusa croise un Yobi plus petit que lui, il le mange et e n absorbe la taille. Par
exemple, si Dusa a une taille de 10 et qu’il tombe sur un Yobi de taille 6, il mange ce dernier
et sa taille augmente ` a 10 + 6 = 16.
Si Dusa croise un Yobi de la mˆ eme taille que lui ou plus grand, Dusa s’enfuit sans manger
le Yobi.
Dusa est actuellement confront´ e ` a une s´ erie de Yobis qu’il va croiser de mani` ere successive.
Il est certain qu’il ﬁnira par tomber sur un Yobi qui le pousse ra ` a la fuite. Votre tˆ ache est
de d´ eterminer quelle sera la taille de Dusa au moment de sa fu ite.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
La premi` ere ligne des donn´ ees d’entr´ ee contient un entier strictement positif D, repr´ esentant
la taille de d´ epart de Dusa.
Les lignes restantes des donn´ ees d’entr´ ee contiennent des entiers strictement positifs repr´ esentant
les tailles des Yobis en ordre.
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sortie devraient aﬃcher un entier strictement positif R, repr´ esentant la taille
de Dusa au moment o` u il prend la fuite.
Donn´ ees d’entr´ ee d’un 1er exemple
5
3
2
9
20
22
14
English version appears before the French version
Donn´ ees de sortie du 1er exemple
19
Justiﬁcation des donn´ ees de sortie du 1 er exemple
Dusa est assez grand pour manger le Yobi de taille 3, ce qui aug mente sa taille ` a 8. Dusa est
assez grand pour manger le Yobi de taille 2, ce qui augmente sa taille ` a 10. Dusa est assez
grand pour manger le Yobi de taille 9, ce qui augmente sa taill e ` a 19. Cependant, confront´ e
` a un Yobi de taille 20, Dusa prend la fuite.
Donn´ ees d’entr´ ee du 2e exemple
10
10
3
5
13
Donn´ ees de sortie du 2e exemple
10
Justiﬁcation des donn´ ees de sortie du 2 e exemple
Confront´ e ` a un Yobi de taille 10, Dusa s’enfuit et sa taille reste donc inchang´ ee.
English version appears before the French version

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2024CCCJuniorTestData", "j2")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2024 Problem J2
    
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