"""
CCC 2022 Junior - Problem J3
============================================================

 Harp Tuning
Problem Description
The CCC harp is a stringed instrument with strings labelled
A, B, . . . , T. Like other instruments, it can be out of tune.
A musically inclined computer science student has written
a clever computer program to help tune the harp. The
program analyzes the sounds produced by the harp and
provides instructions to ﬁx each string that is out of tune.
Each instruction includes a group of strings, whether they
should be tightened or loosened, and by how many turns.
Unfortunately, the output of the program is not very user
friendly. It outputs all the tuning instructions on a single
line. For example, the single line AFB+8HC-4 actually con-
tains two tuning instructions: AFB+8 and HC-4. The ﬁrst
instruction indicates that harp strings A, F , and B should
be tightened 8 turns, and the second instruction indicates
that harp strings H and C should be loosened 4 turns.
Your job is to take a single line of tuning instructions and make them easier to read.
Input Speciﬁcation
There will be one line of input which is a sequence of tuning instructions. Each tuning
instruction will be a sequence of uppercase letters, followed by a plus sign ( +) or minus
sign (-), followed by a positive integer. There will be at least one instruction and at least
one letter per instruction. Also, each uppercase letter will appear at most once.
The following table shows how the available 15 marks are distributed.
Maximum Input Values
Marks Number of Number of Letters Number of Example
Awarded Instructions in an Instruction Turns Input
5 marks 1 20 9 AFB+8
5 marks 20 1 9 A+8H-4
3 marks 20 20 9 AFB+8HC-4
2 marks 20 20 999 999 AFB+88HC-444
Output Speciﬁcation
There will be one line of output for each tuning instruction. Each line of output will consist of
three parts, each separated by a single space: the uppercase letters referring to the strings,
tighten if the instruction contained a plus sign or loosen if the instruction contained a
minus sign, and the number of turns.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Sample Input 1
AFB+8HC-4
Output for Sample Input 1
AFB tighten 8
HC loosen 4
Explanation of Sample Output 1
The input contains two tuning instructions: AFB+8 and HC-4.
Sample Input 2
AFB+8SC-4H-2GDPE+9
Output for Sample Input 2
AFB tighten 8
SC loosen 4
H loosen 2
GDPE tighten 9
Explanation of Sample Output 2
The input contains four tuning instructions: AFB+8, SC-4, H-2, and GDPE+9.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Probl` eme J3 : Accorder une harpe
´Enonc´ e du probl` eme
La harpe CCC est un instrument ` a cordes. Les cordes de
la harpe CCC sont ´ etiquet´ ees A, B, . . . , T. Tout comme
d’autres instruments, la harpe peut ˆ etre d´ esaccord´ ee.
Un ´ etudiant en informatique ayant une aﬃnit´ e pour la
musique a ´ ecrit un programme informatique qui facilite
l’accordage de la harpe. Le programme analyse les sons
produits par la harpe et fournit des instructions pour r´ egler
chaque corde d´ esaccord´ ee. Chaque instruction indique : le
groupe de cordes ` a r´ egler, la mani` ere dont ces cordes doivent
ˆ etre r´ egl´ ees (soit en les resserrant ou en les desserrant) et
ﬁnalement le nombre de tours ` a eﬀectuer en resserrant ou
en desserrant la corde.
Malheureusement, les donn´ ees de sortie du programme ne
sont pas tr` es conviviales car toutes les instructions sont af-
ﬁch´ ees en une seule ligne. Par exemple, la ligne AFB+8HC-4
contient deux instructions : AFB+8 et HC-4. La premi` ere ins-
truction indique que les cordes A, F et B devraient ˆ etre
resserr´ ees de 8 tours tandis que la seconde instruction in-
dique que les cordes H et C devraient ˆ etre desserr´ ees de
4 tours.
Votre tˆ ache consiste ` a rendre une ligne d’instructions de r´ eglage plus facile ` a lire.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
Les donn´ ees d’entr´ ee ne contiennent qu’une seule ligne. Cette ligne contiendra une s´ equence
d’instructions de r´ eglage. Chaque instruction de r´ eglage sera compos´ ee d’une s´ equence de
lettres majuscules, suivie d’un signe plus ( +) ou d’un signe moins ( -), suivi d’un entier
strictement positif. Il doit y avoir au moins une instruction et au moins une lettre par
instruction. De plus, chaque lettre majuscule paraitra au plus une fois.
Le tableau suivant indique la mani` ere dont les 15 points disponibles sont r´ epartis.
Valeurs d’entr´ ee maximales
Attribution Nombre Nombre de lettres Nombre de Exemple de
des points d’instructions dans une instruction tours donn´ ees d’entr´ ee
5 points 1 20 9 AFB+8
5 points 20 1 9 A+8H-4
3 points 20 20 9 AFB+8HC-4
2 points 20 20 999 999 AFB+88HC-444
English version appears before the French version.
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sortie devraient contenir une ligne pour chaque instruction de r´ eglage. Chaque
ligne sera compos´ ee de trois parties (chacune des parties ´ etant s´ epar´ ee des autres par un seul
espace) de la mani` ere suivante : les lettres majuscules correspondant aux cordes qu’il faut
r´ egler, suivies detighten si l’instruction contenait un signe plus ou loosen si l’instruction
contenait un signe moins, suivi du nombre de tours ` a eﬀectuer.
Donn´ ees d’entr´ ee d’un 1er exemple
AFB+8HC-4

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2022CCCJuniorTestData", "j3")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2022 Problem J3
    
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