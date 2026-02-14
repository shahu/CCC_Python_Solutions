"""
CCC 2021 Junior - Problem J2
============================================================

 Silent Auction
Problem Description
A charity is having a silent auction where people place bids o n a prize without knowing
anyone else’s bid. Each bid includes a person’s name and the a mount of their bid. After the
silent auction is over, the winner is the person who has place d the highest bid. If there is a
tie, the person whose bid was placed ﬁrst wins. Your job is to d etermine the winner of the
silent auction.
Input Speciﬁcation
The ﬁrst line of input contains a positive integer N , where 1 ≤ N ≤ 100, representing the
number of bids collected at the silent auction. Each of the ne xt N pairs of lines contains a
person’s name on one line, and the amount of their bid, in doll ars, on the next line. Each
bid is a positive integer less than 2000. The order of the inpu t is the order in which bids
were placed.
Output Speciﬁcation
Output the name of the person who has won the silent auction.
Sample Input 1
3
Ahmed
300
Suzanne
500
Ivona
450
Output for Sample Input 1
Suzanne
Explanation of Output for Sample Input 1
The highest bid placed was 500 and it was placed by Suzanne. Suzanne wins the silent
auction.
Sample Input 2
2
Ijeoma
20
Goor
20
Output for Sample Input 2
Ijeoma
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Explanation of Output for Sample Input 2
The highest bid placed was 20 and it was placed by both Ijeoma and Goor. Since Ijeoma’s
bid was placed ﬁrst, Ijeoma wins the silent auction.
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Problem J2 : Vente aux ench` eres silencieuse
´Enonc´ e du probl` eme
Un organisme de bienfaisance organise une vente aux ench` ere s silencieuse. Lors de cet
´ ev` enement, les participants et participantes placent des oﬀres sur un article sans conna ˆ ıtre
les oﬀres des autres. Chaque oﬀre comprend le nom de la person ne et le montant de son oﬀre.
Une fois l’ench` ere silencieuse termin´ ee, la personne ayant plac´ e l’oﬀre la plus ´ elev´ ee rempor-
tera l’ench` ere. S’il y a ´ egalit´ e, la personne dont l’oﬀre a ´ et´ e plac´ ee en premier remportera
l’ench` ere. Votre tˆ ache consiste ` a d´ eterminer le gagnant de l’ench` ere silencieuse.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
La premi` ere ligne ne contient qu’un seul entier strictemen t positif N tel que 1 ≤ N ≤ 100.
Cet entier repr´ esente le nombre d’oﬀres qui ont ´ et´ e plac´ees lors de la vente aux ench` eres
silencieuse. Chacun des N prochains couples de lignes contient le nom d’une personne s ur
une ligne et le montant de son oﬀre, en dollars, sur la ligne su ivante. Chaque oﬀre est un
entier strictement positif inf´ erieur ` a 2000. L’ordre des donn´ ees d’entr´ ee est celui dans lequel
les oﬀres ont ´ et´ e plac´ ees.
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sortie ne comprennent que le nom de la personn e qui a remport´ e l’ench` ere.
Donn´ ees d’entr´ ee d’un 1er exemple
3
Ahmed
300
Suzanne
500
Ivona
450
Donn´ ees de sortie du 1er exemple
Suzanne
Justiﬁcation des donn´ ees de sortie du 1 er exemple
L’oﬀre la plus ´ elev´ ee (soit500) a ´ et´ e plac´ ee par Suzanne. Suzanne remporte donc l’ench`ere.
Donn´ ees d’entr´ ee d’un 2e exemple
2
Ijeoma
20
Goor
20
Donn´ ees de sortie du 2e exemple
Ijeoma
English version appears before the French version
Justiﬁcation des donn´ ees de sortie du 2 e exemple
L’oﬀre la plus ´ elev´ ee (soit20) a ´ et´ e plac´ ee et par Ijeoma et par Goor. Or, puisque l’oﬀre
d’Ijeoma a ´ et´ e plac´ ee en premier, Ijeoma remporte donc l’ench` ere.
English version appears before the French version

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2021CCCJuniorTestData", "j2")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2021 Problem J2
    
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