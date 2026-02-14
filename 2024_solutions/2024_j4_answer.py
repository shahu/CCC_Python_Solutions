"""
CCC 2024 Junior - Problem J4 - Answer
============================================================

Troublesome Keys
Find silly key (wrong output) and quiet key (no output).
Silly key output is consistent.
============================================================
"""

import os
import sys
from io import StringIO

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(SCRIPT_DIR, "..", "..", "2024CCCJuniorTestData", "j4")
TEST_DATA_DIR = os.path.normpath(TEST_DATA_DIR)


def solve():
    input_str = input().strip()
    output_str = input().strip()
    
    # 核心思路：坏键(Silly)一定出现在 Input 中，但不会以原样出现在 Output 中
    # (因为它总是被替换成了别的字符)。
    # 所以，坏键一定是 set(Input) - set(Output) 的成员。
    input_set = set(input_str)
    output_set = set(output_str)
    candidate_silly_keys = list(input_set - output_set)
    
    # 如果没找到（比如坏键替换成了已经在 output 里的字符），
    # 或者为了保险，可以回退到 input_set。但根据题目逻辑，差集通常很小（1-3个字符）。
    if not candidate_silly_keys:
        candidate_silly_keys = list(input_set)
    
    # 按字母顺序排序，确保确定性（虽然题目只要求唯一解）
    candidate_silly_keys.sort()
    
    for silly in candidate_silly_keys:
        # 我们不知道 quiet 是谁，也不道 wrong_char 是谁
        # 我们可以通过扫描过程推导出来
        
        pj = 0 # 指向 output_str
        quiet = None
        wrong_char = None
        possible = True
        
        for pi in range(len(input_str)):
            in_char = input_str[pi]
            
            # 1. 如果是已知静音键，直接跳过
            if in_char == quiet:
                continue
                
            # 2. 如果是假设的坏键
            if in_char == silly:
                # 还有输出字符可用吗？
                if pj >= len(output_str):
                    possible = False; break
                
                # 如果还没确定 wrong_char，现在就确定它
                if wrong_char is None:
                    wrong_char = output_str[pj]
                # 检查一致性：坏键必须始终变成同一个 wrong_char
                elif output_str[pj] != wrong_char:
                    possible = False; break
                
                pj += 1 # 坏键消耗一个输出字符
                
            else:
                # 3. 如果是正常键（或还没被发现的静音键）
                
                # 情况 A：匹配上了
                if pj < len(output_str) and in_char == output_str[pj]:
                    pj += 1
                
                # 情况 B：没匹配上 -> 那这个 in_char 只能是静音键！
                else:
                    if quiet is None:
                        quiet = in_char # 推导出静音键！
                        # 刚刚发现它是静音键，所以这次它不产出字符，pj 不动
                    elif in_char == quiet:
                         continue # 已知的静音键，跳过(其实应该进上面的 if quiet 分支，但防御性编程)
                    else:
                        # 既不是坏键，也不是静音键，又不匹配 -> 假设错误
                        possible = False; break
        
        # 循环结束，还要检查：
        # 1. 并没有中途失败 (possible is True)
        # 2. output_str 必须刚好被用完 (pj == len)
        if possible and pj == len(output_str):
            print(f"{silly} {wrong_char}")
            if quiet:
                print(quiet)
            else:
                print("-")
            return


def run_tests():
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
