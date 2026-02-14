"""
CCC 2021 Junior - Problem J4
============================================================

 Arranging Books
Problem Description
Valentina wants books on a shelf to be arranged in a particula r way. Every time she sees
a shelf of books, she rearranges the books so that all the larg e books appear on the left,
followed by all the medium-sized books, and then all the smal l books on the right. She does
this by repeatedly choosing any two books and exchanging the ir locations. Exchanging the
locations of two books is called a swap.
Help Valentina determine the fewest number of swaps needed to arrange a shelf of books as
she wishes.
Input Speciﬁcation
The input will consist of exactly one line containing at leas t one character.
The following table shows how the available 15 marks are dist ributed.
7 marks at most 1000 characters each character will be L or S
2 marks at most 500 000 characters each character will be L or S
4 marks at most 1000 characters each character will be L, M, or S
2 marks at most 500 000 characters each character will be L, M, or S
Output Speciﬁcation
Output a single integer which is equal to the minimum possibl e number of swaps needed to
arrange the books so that all occurrences of L come ﬁrst, followed by all occurrences of M,
and then all occurrences of S.
Sample Input 1
LMMMS
Output for Sample Input 1
0
Explanation of Output for Sample Input 1
The books are already arranged according to Valentina’s wis hes.
Sample Input 2
LLSLM
Output for Sample Input 2
2
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Explanation of Output for Sample Input 2
By swapping the S and M, we end up with LLMLS. Then the M can be swapped with the L to
its right. This is one way to use two swaps to arrange the books as Valentina wants them to
be. It is not possible to use fewer swaps because both S and M need to be moved but using
one swap to exchange them does not leave the books arranged as Valentina wants them to
be.
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Probl` eme J4 : Comment organiser ses livres
´Enonc´ e du probl` eme
Valentina veut que les livres sur une ´ etag` ere soient dispos´ es d’une certaine mani` ere. Chaque
fois qu’elle voit une ´ etag` ere de livres, elle r´ eorganiseles livres de mani` ere que les grands livres
soient situ´ es ` a gauche sur l’´ etag` ere, que les petits livres soient situ´ es ` a droite sur l’´ etag` ere et
que les livres de taille moyenne soient situ´ es entre les deux. Elle accomplit cela en choisissant
deux livres et en ´ echangeant leurs emplacements sur l’´ etag` ere. Elle r´ ep` ete cette manoeuvre
d’´ echangejusqu’` a atteindre la disposition souhait´ ee.
Votre tˆ ache est d’aider Valentina ` a d´ eterminer le nombreminimal d’´ echanges n´ ecessaires aﬁn
d’atteindre la disposition souhait´ ee des livres.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
Les donn´ ees d’entr´ ee consisteront exactement en une ligne contenant au moins un caract` ere.
Chacun des caract` eres dans la ligne sera soit L (un grand livre), soit M (un livre de taille
moyenne), soit S (un petit livre).
Le tableau suivant indique la mani` ere dont les 15 points dis ponibles sont r´ epartis.
7 points au plus 1000 caract` eres chaque caract` ere sera un L ou un S
2 points au plus 500 000 caract` eres chaque caract` ere sera un L ou un S
4 points au plus 1000 caract` eres chaque caract` ere sera un L, un M ou un S
2 points au plus 500 000 caract` eres chaque caract` ere sera un L, un M ou un S
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sortie ne devraient contenir qu’un seul enti er, soit le nombre minimal
d’´ echanges n´ ecessaires aﬁn que toutes les occurrences de L paraissent en premier, suivies
de toutes les occurences de M, puis toutes les occurences de S.
Donn´ ees d’entr´ ee d’un 1er exemple
LMMMS
Donn´ ees de sortie du 1er exemple
0
Justiﬁcation des donn´ ees de sortie du 1 er exemple
Les livres sont d´ ej` a dispos´ es de la mani` ere souhait´ ee.
Donn´ ees d’entr´ ee d’un 2e exemple
LLSLM
English version appears before the French version
Donn´ ees de sortie du 2e exemple
2
Justiﬁcation des donn´ ees de sortie du 2 e exemple
En ´ echangeant leS et le M, on obtient LLMLS. Ensuite, on atteint la disposition souhait´ ee en
´ echangeant leM avec le L ` a sa droite. On a donc atteint la disposition souhait´ ee en a yant
eﬀectu´ e deux ´ echanges. Il n’est pas possible d’atteindrela disposition souhait´ ee en eﬀectuant
moins d’´ echanges puisque l’´ echange n´ ecessaire deS et M ne r´ esulte pas en une disposition qui
satisfait aux crit` eres de Valentina.
English version appears before the French version

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2021CCCJuniorTestData", "j4")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2021 Problem J4
    
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