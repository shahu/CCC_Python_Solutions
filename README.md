# CCC Junior Python Solutions

Complete Python practice environment for the Canadian Computing Contest (CCC) Junior division (2021-2025).

## ✅ Features

- **50 Python files** covering all problems from 2021-2025
- **Complete problem descriptions** extracted from official CCC PDFs
- **Automatic test case loading** from official test data
- **Two file types per problem**:
  - `*_quiz.py` - Practice with TODOs (implement yourself)
  - `*_answer.py` - Solution template with test runner

## 📁 Structure

```
CCC_Python_Solutions/
├── 2021_solutions/          # 5 problems: J1-J4, J5/S2 (Modern Art)
├── 2022_solutions/          # 5 problems: J1-J3, J5, J4/S2 (Square Pool)
├── 2023_solutions/          # 5 problems: J1-J3, J5, J4/S1 (Trianglane)
├── 2024_solutions/          # 5 problems: J1-J5
├── 2025_solutions/          # 5 problems: J1-J5
└── README.md
```

## 🚀 Quick Start

### Run Any File Directly
```bash
cd 2021_solutions
python3 2021_j1_answer.py
```

**No parameters needed!** The script automatically:
1. Finds test cases in `../../2021CCCJuniorTestData/j1/`
2. Runs all test cases
3. Shows pass/fail results

### Example Output
```
Running 7 test cases...
============================================================
✗ j1.01: FAILED
  Expected: '210\n-1'
  Got: ''
✗ j1.02: FAILED
  Expected: '85\n1'
  Got: ''
...
Results: 0 passed, 7 failed
============================================================
```

*Note: Tests fail because the solution is a placeholder. Implement the `solve()` function to make them pass!*

## 📝 How to Use

### 1. Practice Mode (Quiz Files)

```python
# Open 2021_j1_quiz.py and implement:
def solve():
    # TODO: Read input
    B = int(input())
    
    # TODO: Calculate
    P = 5 * B - 400
    
    # TODO: Determine sea level
    if P > 100:
        level = -1  # Below sea level
    elif P < 100:
        level = 1   # Above sea level
    else:
        level = 0   # At sea level
    
    # TODO: Print output
    print(P)
    print(level)
```

### 2. Test Your Solution

```bash
python3 2021_j1_quiz.py
```

### 3. Compare with Custom Input

```bash
echo "99" | python3 2021_j1_quiz.py
```

## 📊 Problem Summary

| Year | Problems | Total Tests |
|------|----------|-------------|
| 2021 | J1, J2, J3, J4, J5/S2 | 54 |
| 2022 | J1, J2, J3, J4/S2, J5 | 91 |
| 2023 | J1, J2, J3, J4/S1, J5 | 83 |
| 2024 | J1, J2, J3, J4, J5 | 102 |
| 2025 | J1, J2, J3, J4, J5 | 63 |
| **Total** | **25 problems** | **393 tests** |

## 🔍 Problem ID Mapping

Some problems are shared between Junior and Senior divisions:
- **2021 J5** = J5/S2 (Modern Art)
- **2022 S2J4** = J4/S2 (Square Pool)
- **2023 S1J4** = J4/S1 (Trianglane)

## 💡 Tips

1. **Start with quiz files** to practice problem-solving
2. **Run tests frequently** to check your progress
3. **Study test cases** to understand edge cases
4. **Time yourself** to simulate contest conditions
5. **Review solutions** in answer files after attempting

## 🎯 Test Data Source

All test cases are loaded from official CCC test data:
- Location: `../{Year}CCCJuniorTestData/{problem}/`
- Format: `*.in` (input) and `*.out` (expected output)
- Includes both sample and official test cases

## 📚 File Format

Each Python file includes:
- ✅ Complete problem description from official PDF
- ✅ Input/Output specifications
- ✅ Sample inputs and outputs
- ✅ TODO comments for implementation
- ✅ Automatic test case loader
- ✅ Test runner with pass/fail reporting

## 🏆 Good Luck!

Practice consistently and you'll do great on the CCC!

---
*Generated for CCC Junior 2021-2025*
