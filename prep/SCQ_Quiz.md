# Python Syntax & Basics Quiz

For each question, select the best answer.

### 1. Which of the following is a valid Python variable name?
- A) 2myvar
- B) my-var
- C) my_var
- D) my var

### 2. What is the output of print(type(3.14))?
- A) <class 'int'>
- B) <class 'float'>
- C) <class 'str'>
- D) <class 'bool'>

### 3. What is the result of 10 // 3?
- A) 3.33
- B) 3
- C) 1
- D) 30

### 4. What is the output of print('Python'[0])?
- A) P
- B) y
- C) n
- D) Error

### 5. What is the result of 'Hello' * 3?
- A) Hello3
- B) HelloHelloHello
- C) Error
- D) Hello Hello Hello

### 6. What is the output of len([1, 2, 3])?
- A) 2
- B) 3
- C) 4
- D) 0

### 7. Which list method adds an element to the end of a list?
- A) add()
- B) insert()
- C) append()
- D) push()

### 8. What is the output of bool(0)?
- A) True
- B) False
- C) None
- D) Error

### 9. What does range(3) generate (conceptually)?
- A) 1, 2, 3
- B) 0, 1, 2
- C) 0, 1, 2, 3
- D) 1, 2

### 10. What is the correct keyword to define a function?
- A) func
- B) function
- C) def
- D) define

### 11. What is the result of 10 % 3?
- A) 3
- B) 1
- C) 3.33
- D) 0

### 12. What is the output of 'apple' in ['apple', 'banana']?
- A) True
- B) False
- C) None
- D) Error

### 13. What is the output of list('cat')?
- A) ['cat']
- B) ['c', 'a', 't']
- C) Error
- D) ('c', 'a', 't')

### 14. Which function is used to get input from the user?
- A) get()
- B) read()
- C) input()
- D) scan()

### 15. Which of the following data types is immutable?
- A) List
- B) Dictionary
- C) Tuple
- D) Set

### 16. What is the result of 2 ** 3?
- A) 6
- B) 8
- C) 5
- D) 9

### 17. Which of the following is a valid dictionary definition?
- A) {'a', 1}
- B) {'a': 1}
- C) ['a': 1]
- D) ('a', 1)

### 18. What is the result of 'a' + 'b'?
- A) ab
- B) a b
- C) Error
- D) 9798

### 19. What is the output of print('Py' 'thon')? (Implicit concatenation)
- A) Python
- B) Py thon
- C) Error
- D) Py+thon

### 20. What is the result of int('10') + 5?
- A) 105
- B) 15
- C) Error
- D) '105'

### 21. What is the result of str(10) + '5'?
- A) 15
- B) 105
- C) Error
- D) 50

### 22. What is the output of True and False?
- A) True
- B) False
- C) None
- D) Error

### 23. What is the output of not True?
- A) True
- B) False
- C) None
- D) Error

### 24. What is the output of 10 == 10.0?
- A) True
- B) False
- C) Error
- D) None

### 25. What is the output of '  strip  '.strip()?
- A) '  strip  '
- B) 'strip'
- C) 'strip  '
- D) '  strip'


---

# Answer Key & Explanations

**1. C**
> Variable names cannot start with a number (A), cannot contain hyphens (B), and cannot contain spaces (D). Underscores are allowed.

**2. B**
> 3.14 is a floating-point number, so its type is float.

**3. B**
> The // operator performs floor division, discarding the fractional part.

**4. A**
> Python strings are 0-indexed, so index 0 refers to the first character 'P'.

**5. B**
> Multiplying a string by an integer repeats the string that many times.

**6. B**
> The len() function returns the number of items in a list. Here there are 3 items.

**7. C**
> append() adds an item to the end. insert() adds at a specific index. add() is for sets.

**8. B**
> In Python, 0 is considered falsy, so bool(0) returns False.

**9. B**
> range(n) generates numbers from 0 up to n-1.

**10. C**
> 'def' is the keyword used to define functions in Python.

**11. B**
> The % operator (modulus) returns the remainder of the division. 10 divided by 3 is 3 with a remainder of 1.

**12. A**
> The 'in' operator checks for membership. Since 'apple' exists in the list, it returns True.

**13. B**
> Converting a string to a list breaks it down into individual characters.

**14. C**
> input() is the standard built-in function to read a line from standard input.

**15. C**
> Tuples are immutable sequences, meaning their elements cannot be changed after creation. Lists, sets, and dicts are mutable.

**16. B**
> The ** operator performs exponentiation. 2 to the power of 3 is 8.

**17. B**
> Dictionaries use curly braces {} with key-value pairs separated by colons.

**18. A**
> The + operator concatenates (joins) two strings together.

**19. A**
> Python automatically concatenates adjacent string literals.

**20. B**
> int('10') converts the string to the integer 10. Then 10 + 5 = 15.

**21. B**
> str(10) converts integer 10 to string '10'. Then '10' + '5' concatenates them to '105'.

**22. B**
> The 'and' operator returns True only if both operands are True.

**23. B**
> The 'not' operator inverts the boolean value.

**24. A**
> Python compares the values of numbers, even if types differ (int vs float). 10 is equal to 10.0.

**25. B**
> The strip() method removes leading and trailing whitespace.

