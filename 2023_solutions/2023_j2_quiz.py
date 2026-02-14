"""
CCC 2023 Junior - Problem J2
============================================================

 Chili Peppers
Problem Description
Ron is cooking chili using an assortment of peppers.
The spiciness of a pepper is measured in Scolville Heat Units (SHU). Ron’s chili is currently
not spicy at all, but each time Ron adds a pepper, the total spiciness of the chili increases
by the SHU value of that pepper.
The SHU values of the peppers available to Ron are shown in the following table:
Pepper Name Scolville Heat Units
Poblano 1500
Mirasol 6000
Serrano 15500
Cayenne 40000
Thai 75000
Habanero 125000
Your job is to determine the total spiciness of Ron’s chili after he has ﬁnished adding peppers.
Input Speciﬁcation
The ﬁrst line of input will contain a positive integer N, representing the number of peppers
Ron adds to his chili. The next N lines will each contain the name of a pepper Ron has
added. Each pepper name will exactly match a name that appears in the table above. Note
that more than one pepper of the same name can be added.
Output Speciﬁcation
The output will consist of a positive integer T , representing the total spiciness of Ron’s chili.
Sample Input
4
Poblano
Cayenne
Thai
Poblano
Output for Sample Input
118000
Explanation of Output for Sample Input
A Poblano pepper has an SHU value of 1500. A Cayenne pepper has an SHU value of 40000.
A Thai pepper has an SHU value of 75000. The total spiciness of Ron’s chili is therefore
1500 + 40000 + 75000 + 1500 = 118000.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Probl` eme J2 : Piments
´Enonc´ e du probl` eme
Ron pr´ epare du chili en utilisant une vari´ et´ e de piments.
Le piquant d’un piment est mesur´ e en unit´ es thermiques de Scoville (SHU). Au d´ ebut, le
chili de Ron n’est pas du tout ´ epic´ e. Cependant, ` a chaque fois qu’il ajoute un piment, le
piquant total de son chili augmente d’une valeur ´ egale ` a celle du SHU de ce piment.
Les valeurs SHU des piments dont dispose Ron sont indiqu´ ees dans le tableau suivant :
Vari´ et´ es de pimentUnit´ es thermiques de Scoville
Poblano 1500
Mirasol 6000
Serrano 15500
Cayenne 40000
Thai 75000
Habanero 125000
Votre tˆ ache consiste ` a d´ eterminer le piquant total du chili de Ron une fois qu’il a termin´ e
d’ajouter des piments.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
La premi` ere ligne des donn´ ees d’entr´ ee doit contenir un entier strictement positifN, repr´ esentant
le nombre de piments que Ron a ajout´ e ` a son chili. Chacune des N lignes suivantes doit
contenir le nom d’un piment que Ron a ajout´ e. Les noms des piments ajout´ es doivent corres-
pondre exactement aux noms des piments qui ﬁgurent dans le tableau ci-dessus. Remarquez
que n’importe quelle vari´ et´ e de piment peut ˆ etre ajout´ ee plus d’une seule fois.
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sortie devraient aﬃcher un entier strictement positif T , repr´ esentant le pi-
quant total du chili de Ron.
Exemple de donn´ ees d’entr´ ee
4
Poblano
Cayenne
Thai
Poblano
Exemple de donn´ ees de sortie
118000
English version appears before the French version
Justiﬁcation des donn´ ees de sortie
Un piment poblano a une valeur SHU de 1500. Un piment de Cayenne a une valeur SHU de
40000. Un piment tha¨ ı a une valeur SHU de 75000. Le chili de Ron a donc un piquant total
de 1500 + 40000 + 75000 + 1500 = 118000.
English version appears before the French version

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2023CCCJuniorTestData", "j2")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2023 Problem J2
    
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