"""
CCC 2024 Junior - Problem J4
============================================================

 Troublesome Keys
Problem Description
As Alex is typing, their keyboard is acting strangely. Two lett er keys are causing trouble:
• One letter key displays the same wrong letter each time it is p ressed. Alex calls this
key the silly key . Oddly, Alex never actually tries to type the wrong letter dis played
by the silly key.
• Another letter key doesn’t display anything when it is presse d. Alex calls this key the
quiet key .
Alex presses the silly key at least once but they don’t necessa rily press the quiet key.
Your job is to determine the troublesome keys and the wrong le tter that is displayed. Luckily,
this is possible because Alex never presses the silly key imme diately after pressing the quiet
key and Alex never presses the quiet key immediately after pre ssing the silly key.
Input Speciﬁcation
There will be two lines of input. The ﬁrst line of input repres ents the N keys Alex presses
on the keyboard. The second line of input represents the lett ers displayed on the screen.
Both lines of input will only contain lowercase letters of th e alphabet.
The following table shows how the available 15 marks are dist ributed.
Marks Description Bound
3 The quiet key is not pressed. A small number of keys are presse d. N ≤ 50
3 The ﬁrst troublesome key pressed is the silly key. A small num -
ber of keys are pressed.
N ≤ 50
5 The ﬁrst troublesome key pressed may be the silly key or the
quiet key. A small number of keys are pressed.
N ≤ 50
4 The ﬁrst troublesome key pressed may be the silly key or the
quiet key. A large number of keys are pressed.
N ≤ 500 000
Output Speciﬁcation
There will be two lines of output.
On the ﬁrst line, output the letter corresponding to the sill y key and the wrong letter
displayed on the screen when it is pressed, separated by a sin gle space.
On the second line, output the letter corresponding to the qui et key if it is pressed. Output
the dash character ( -) if the quiet key is not pressed.
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Sample Input 1
forloops
fxrlxxps
Output for Sample Input 1
o x
-
Explanation of Sample Output 1
The letter corresponding to the silly key was the letter o. Each time it was pressed, the
wrong letter x was displayed. The quiet key was not pressed.
Sample Input 2
forloops
fxrlxxp
Output for Sample Input 2
o x
s
Explanation of Sample Output 2
The letter corresponding to the silly key was the letter o. Each time it was pressed, the
wrong letter x was displayed. The quiet key corresponds to the letter s which was not
displayed.
Sample Input 3
forloops
frlpz
Output for Sample Input 3
s z
o
Explanation of Sample Output 3
The letter corresponding to the silly key was the letter s. Each time it was pressed, the
wrong letter z was displayed. The quiet key corresponds to the letter o which was not
displayed.
La version fran¸ caise ﬁgure ` a la suite de la version anglais e.
Probl` eme J4 : Touches probl´ ematiques
´Enonc´ e du probl` eme
Alors qu’Alex tape sur son clavier d’ordinateur, son clavier s e comporte ´ etrangement. Deux
touches de lettres posent probl` eme :
— Une touche aﬃche la mˆ eme lettre erron´ ee ` a chaque fois qu’e lle est frapp´ ee. Alex a
surnomm´ e cette touche la touche absurde . Curieusement, Alex ne cherche jamais ` a
taper la lettre erron´ ee aﬃch´ ee par la touche absurde.
— Une autre touche n’aﬃche rien lorsqu’elle est frapp´ ee. Alex a surnomm´ e cette touche
la touche silencieuse .
Alex frappe la touche absurde au moins une fois, mais ne frappe pas n´ ecessairement la touche
silencieuse.
Votre tˆ ache consiste ` a d´ eterminer quelles sont les touches probl´ ematiques et la lettre erron´ ee
qu’aﬃche la touche absurde. Heureusement, cela est r´ ealisa ble car Alex ne frappe jamais la
touche absurde imm´ ediatement apr` es avoir frapp´ e la touche silencieuse et ne frappe jamais
la touche silencieuse imm´ ediatement apr` es avoir frapp´ ela touche absurde.
Pr´ ecisions par rapport aux donn´ ees d’entr´ ee
Les donn´ ees d’entr´ ee contiennent deux lignes. La premi` ere ligne des donn´ ees d’entr´ ee contient
les N touches qu’Alex frappe sur le clavier. La seconde ligne des do nn´ ees d’entr´ ee contient
les lettres qui s’aﬃchent ` a l’´ ecran.
Les deux lignes des donn´ ees d’entr´ ee ne doivent contenir que des lettres minuscules de l’al-
phabet.
Le tableau ci-dessous d´ etaille la r´ epartition des 15 points disponibles.
Points Description Bornes
3 La touche silencieuse n’est pas frapp´ ee. Un petit nombre de
touches sont frapp´ ees.
N ≤ 50
3 La premi` ere touche probl´ ematique frapp´ ee est la touche absurde.
Un petit nombre de touches sont frapp´ ees.
N ≤ 50
5 La premi` ere touche probl´ ematique frapp´ ee peut ˆ etre la touche
absurde ou la touche silencieuse. Un petit nombre de touches
sont frapp´ ees.
N ≤ 50
4 La premi` ere touche probl´ ematique frapp´ ee peut ˆ etre la touche
absurde ou la touche silencieuse. Un grand nombre de touches

============================================================

TODO: Implement the solution function below
"""

import os
import sys
from io import StringIO

# FIXED: Get script directory and navigate to test data
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2024CCCJuniorTestData", "j4")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    """
    TODO: Implement your solution for CCC 2024 Problem J4
    
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