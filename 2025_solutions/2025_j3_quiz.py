"""
CCC 2025 Junior - Problem J3
============================================================

 Product Codes
Problem Description
A store has hired the Code Cleaning Crew to help it update all of its product codes.
The original product codes are sequences of letters, positive integers, and negative inte-
gers. For example, cG23mH-9s is a product code that contains two uppercase letters, three
lowercase letters, one positive integer, and one negative integer.
The new product codes are made by removing all lowercase letters, keeping all uppercase
letters in order, and adding all the integers to form one new integer which is placed at the
end of the code. For example, the new product code for cG23mH-9s is GH14.
Your job is to take a list of original product codes and determine the new product codes.
Input Speciﬁcation
The ﬁrst line of input contains a positive integer, N, representing the number of original
product codes that need to be updated. The following N lines each contain one original
product code.
Each original product code contains at least one uppercase letter, at least one lowercase
letter, and at least one integer. Also, a positive integer never immediately follows another
integer. This means, for example, that 23 is the integer 23 instead of the integer 2 followed
by the integer 3.
The following table shows how the available 15 marks are distributed:
Marks Description
2 All the integers are positive and single-digit.
2 All the integers are single-digit.
7 Any positive integer may be multi-digit.
4 Any integer may be multi-digit.
Output Speciﬁcation
Output the N new product codes, one per line.
Sample Input 1
1
AbC3c2Cd9
Output for Sample Input 1
ACC14
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Explanation of Output for Sample Input 1
For the single original product code, the uppercase letters A, C, and C are kept in order and
the sum of the integers is 3 + 2 + 9 = 14.
Sample Input 2
3
Ahkiy-6ebvXCV1
393hhhUHkbs5gh6QpS-9-8
PL12N-2G1234Duytrty8-86tyaYySsDdEe
Output for Sample Input 2
AXCV-5
UHQS387
PLNGDYSDE1166
Explanation of Output for Sample Input 2
For the ﬁrst original product code, the uppercase letters A, X, C, and V are kept in order and
the sum of the integers is −6 + 1 = −5.
For the second and third original product codes, their uppercase letters are also kept in order
and the sums of the integers are 393 + 5 + 6− 9 − 8 = 387 and 12 − 2 + 1234 + 8− 86 = 1166
respectively.
La version fran¸ caise ﬁgure ` a la suite de la version anglaise.
Probl` eme J3 : Codes de produits
´Enonc´ e du probl` eme
Le g´ erant d’un magasin a embauch´ e la Compagnie de correction d’identiﬁants (CCI) pour
l’aider ` a mettre ` a jour tous ses codes de produits.
Les codes de produits originaux sont des s´ equences de lettres, d’entiers strictement positifs et
d’entiers strictement n´ egatifs. Par exemple,cG23mH-9s est un code de produit qui contient
deux lettres majuscules, trois lettres minuscules, un entier strictement positif et un entier
strictement n´ egatif.
Les nouveaux codes de produits sont obtenus en ´ eliminant toutes les lettres minuscules, en
conservant toutes les lettres majuscules dans l’ordre et en additionnant tous les entiers pour
former un nouveau nombre entier qui sera plac´ e ` a la ﬁn du code. Par exemple, le nouveau
code de produit pour le code cG23mH-9s est : GH14.
Votre tˆ ache consiste ` a prendre une liste de codes de produits originaux et ` a d´ eterminer les
nouveaux codes de produits.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
La premi` ere ligne des donn´ ees d’entr´ ee contient un entier strictement positif,N, repr´ esentant
le nombre de codes de produits originaux devant ˆ etre corrig´ es. Les N lignes de donn´ ees
d’entr´ ee suivantes contiennent toutes un code de produit original.
Chaque code de produit original contient au moins une lettre majuscule, une lettre minuscule
et un entier. Un entier strictement positif ne suit jamais imm´ ediatement un autre entier. Par
exemple, cela signiﬁe que 23 correspond ` a l’entier 23 et non pas ` a l’entier 2 suivi de l’entier 3.
Le tableau suivant d´ etaille la r´ epartition des 15 points disponibles.
Points Description
2 Tous les entiers sont strictement positifs et comportent un seul chiﬀre.
2 Tous les entiers comportent un seul chiﬀre.
7 Tout entier strictement positif peut comporter plusieurs chiﬀres.
4 Tout entier peut comporter plusieurs chiﬀres.
Pr´ ecisions par rapport aux donn´ ees de sortie
Les donn´ ees de sorties devraient contenir lesN nouveaux codes de produit, un par ligne.
Donn´ ees d’entr´ ee d’un 1er exemple
1
AbC3c2Cd9
English version appears before the French version
Donn´ ees de sortie du 1er exemple
ACC14
Justiﬁcation des donn´ ees de sortie du 1er exemple
Pour le premier code de produit original, les lettres majuscules A, C, et C sont conserv´ ees
dans l’ordre et la somme des nombres entiers est de 3 + 2 + 9 = 14.
Donn´ ees d’entr´ ee du 2e exemple
3
Ahkiy-6ebvXCV1
393hhhUHkbs5gh6QpS-9-8
PL12N-2G1234Duytrty8-86tyaYySsDdEe
Donn´ ees de sortie du 2e exemple
AXCV-5
UHQS387
PLNGDYSDE1166
Justiﬁcation des donn´ ees de sortie du 2e exemple
Pour le premier code de produit original, les lettres majuscules A, X, C, et V sont conserv´ ees

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2025CCCJuniorTestData", "j3")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2025 Problem J3
    
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