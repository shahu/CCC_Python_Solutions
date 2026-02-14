import time

questions = [{'q': '1. Which of the following is a valid Python variable name?', 'options': ['A) 2myvar', 'B) my-var', 'C) my_var', 'D) my var'], 'answer': 'C', 'explanation': 'Variable names cannot start with a number (A), cannot contain hyphens (B), and cannot contain spaces (D). Underscores are allowed.'}, {'q': '2. What is the output of print(type(3.14))?', 'options': ["A) <class 'int'>", "B) <class 'float'>", "C) <class 'str'>", "D) <class 'bool'>"], 'answer': 'B', 'explanation': '3.14 is a floating-point number, so its type is float.'}, {'q': '3. What is the result of 10 // 3?', 'options': ['A) 3.33', 'B) 3', 'C) 1', 'D) 30'], 'answer': 'B', 'explanation': 'The // operator performs floor division, discarding the fractional part.'}, {'q': "4. What is the output of print('Python'[0])?", 'options': ['A) P', 'B) y', 'C) n', 'D) Error'], 'answer': 'A', 'explanation': "Python strings are 0-indexed, so index 0 refers to the first character 'P'."}, {'q': "5. What is the result of 'Hello' * 3?", 'options': ['A) Hello3', 'B) HelloHelloHello', 'C) Error', 'D) Hello Hello Hello'], 'answer': 'B', 'explanation': 'Multiplying a string by an integer repeats the string that many times.'}, {'q': '6. What is the output of len([1, 2, 3])?', 'options': ['A) 2', 'B) 3', 'C) 4', 'D) 0'], 'answer': 'B', 'explanation': 'The len() function returns the number of items in a list. Here there are 3 items.'}, {'q': '7. Which list method adds an element to the end of a list?', 'options': ['A) add()', 'B) insert()', 'C) append()', 'D) push()'], 'answer': 'C', 'explanation': 'append() adds an item to the end. insert() adds at a specific index. add() is for sets.'}, {'q': '8. What is the output of bool(0)?', 'options': ['A) True', 'B) False', 'C) None', 'D) Error'], 'answer': 'B', 'explanation': 'In Python, 0 is considered falsy, so bool(0) returns False.'}, {'q': '9. What does range(3) generate (conceptually)?', 'options': ['A) 1, 2, 3', 'B) 0, 1, 2', 'C) 0, 1, 2, 3', 'D) 1, 2'], 'answer': 'B', 'explanation': 'range(n) generates numbers from 0 up to n-1.'}, {'q': '10. What is the correct keyword to define a function?', 'options': ['A) func', 'B) function', 'C) def', 'D) define'], 'answer': 'C', 'explanation': "'def' is the keyword used to define functions in Python."}, {'q': '11. What is the result of 10 % 3?', 'options': ['A) 3', 'B) 1', 'C) 3.33', 'D) 0'], 'answer': 'B', 'explanation': 'The % operator (modulus) returns the remainder of the division. 10 divided by 3 is 3 with a remainder of 1.'}, {'q': "12. What is the output of 'apple' in ['apple', 'banana']?", 'options': ['A) True', 'B) False', 'C) None', 'D) Error'], 'answer': 'A', 'explanation': "The 'in' operator checks for membership. Since 'apple' exists in the list, it returns True."}, {'q': "13. What is the output of list('cat')?", 'options': ["A) ['cat']", "B) ['c', 'a', 't']", 'C) Error', "D) ('c', 'a', 't')"], 'answer': 'B', 'explanation': 'Converting a string to a list breaks it down into individual characters.'}, {'q': '14. Which function is used to get input from the user?', 'options': ['A) get()', 'B) read()', 'C) input()', 'D) scan()'], 'answer': 'C', 'explanation': 'input() is the standard built-in function to read a line from standard input.'}, {'q': '15. Which of the following data types is immutable?', 'options': ['A) List', 'B) Dictionary', 'C) Tuple', 'D) Set'], 'answer': 'C', 'explanation': 'Tuples are immutable sequences, meaning their elements cannot be changed after creation. Lists, sets, and dicts are mutable.'}, {'q': '16. What is the result of 2 ** 3?', 'options': ['A) 6', 'B) 8', 'C) 5', 'D) 9'], 'answer': 'B', 'explanation': 'The ** operator performs exponentiation. 2 to the power of 3 is 8.'}, {'q': '17. Which of the following is a valid dictionary definition?', 'options': ["A) {'a', 1}", "B) {'a': 1}", "C) ['a': 1]", "D) ('a', 1)"], 'answer': 'B', 'explanation': 'Dictionaries use curly braces {} with key-value pairs separated by colons.'}, {'q': "18. What is the result of 'a' + 'b'?", 'options': ['A) ab', 'B) a b', 'C) Error', 'D) 9798'], 'answer': 'A', 'explanation': 'The + operator concatenates (joins) two strings together.'}, {'q': "19. What is the output of print('Py' 'thon')? (Implicit concatenation)", 'options': ['A) Python', 'B) Py thon', 'C) Error', 'D) Py+thon'], 'answer': 'A', 'explanation': 'Python automatically concatenates adjacent string literals.'}, {'q': "20. What is the result of int('10') + 5?", 'options': ['A) 105', 'B) 15', 'C) Error', "D) '105'"], 'answer': 'B', 'explanation': "int('10') converts the string to the integer 10. Then 10 + 5 = 15."}, {'q': "21. What is the result of str(10) + '5'?", 'options': ['A) 15', 'B) 105', 'C) Error', 'D) 50'], 'answer': 'B', 'explanation': "str(10) converts integer 10 to string '10'. Then '10' + '5' concatenates them to '105'."}, {'q': '22. What is the output of True and False?', 'options': ['A) True', 'B) False', 'C) None', 'D) Error'], 'answer': 'B', 'explanation': "The 'and' operator returns True only if both operands are True."}, {'q': '23. What is the output of not True?', 'options': ['A) True', 'B) False', 'C) None', 'D) Error'], 'answer': 'B', 'explanation': "The 'not' operator inverts the boolean value."}, {'q': '24. What is the output of 10 == 10.0?', 'options': ['A) True', 'B) False', 'C) Error', 'D) None'], 'answer': 'A', 'explanation': 'Python compares the values of numbers, even if types differ (int vs float). 10 is equal to 10.0.'}, {'q': "25. What is the output of '  strip  '.strip()?", 'options': ["A) '  strip  '", "B) 'strip'", "C) 'strip  '", "D) '  strip'"], 'answer': 'B', 'explanation': 'The strip() method removes leading and trailing whitespace.'}]


def run_quiz():
    score = 0
    print("Welcome to the Python Basics Quiz!")
    print("Type A, B, C, or D for each question.\n")
    
    for i, q in enumerate(questions):
        print("-" * 50)
        print(q['q'])
        for opt in q['options']:
            print(opt)
        
        user_ans = input("Your answer: ").strip().upper()
        
        if user_ans == q['answer']:
            print("Correct! ✅")
            score += 1
        else:
            print(f"Wrong ❌. The correct answer was {q['answer']}.")
        
        # Show explanation regardless of right/wrong
        print(f"\nExplanation: {q['explanation']}\n")
        
        # Pause briefly
        time.sleep(1.5)

    print("=" * 50)
    print(f"Quiz Finished! Your score: {score}/{len(questions)}")
    if score == len(questions):
        print("Perfect! 🏆")
    elif score >= 20:
        print("Great job! 🥈")
    else:
        print("Keep practicing! 💪")

if __name__ == "__main__":
    run_quiz()
