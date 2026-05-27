import sys
import time
from solution import max_pair_product

GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

test_cases = [
    # (description, input, expected)
    ("basic positive numbers",          [3, 5, 2, 8],           40),
    ("two negatives win",               [-5, -3, 1, 2],         15),
    ("all zeros",                       [0, 0, 0],              0),
    ("zeros bring down the best",       [0, 0, 5],              0),
    ("two elements only",               [4, 7],                 28),
    ("two elements, one negative",      [-4, 7],                -28),
    ("both negative, two elements",     [-4, -7],               28),
    ("large mixed",                     [3, 1, 4, 1, 5, 9, 2, 6], 54),
    ("negatives and positives mixed",   [-10, 2, 3, -4],        40),
    ("all same value",                  [6, 6, 6],              36),
    ("single large negative pair",      [-100, -1, 0, 1],       100),
    ("one zero one negative",           [-5, 0],                0),
    ("large values",                    [10000, 9999, -10000],  99990000),
    ("includes duplicates",             [2, 2, 3],              6),
    ("all negatives",                   [-1, -2, -3, -4],       12),
]

def run_tests():
    print(f"\n{BOLD}{CYAN}{'─' * 60}{RESET}")
    print(f"{BOLD}{CYAN}  001 — Max Pair Product{RESET}")
    print(f"{BOLD}{CYAN}{'─' * 60}{RESET}\n")

    passed = 0
    failed = 0
    errors = 0

    for i, (desc, nums, expected) in enumerate(test_cases, 1):
        label = f"Test {i:02d}  {desc}"
        try:
            start = time.perf_counter()
            result = max_pair_product(nums[:])  # pass a copy so solution can't mutate
            elapsed = (time.perf_counter() - start) * 1000

            if result == expected:
                print(f"  {GREEN}✔ PASS{RESET}  {label}")
                print(f"         input={nums}  →  {result}  ({elapsed:.2f}ms)")
                passed += 1
            else:
                print(f"  {RED}✘ FAIL{RESET}  {label}")
                print(f"         input    = {nums}")
                print(f"         expected = {YELLOW}{expected}{RESET}")
                print(f"         got      = {RED}{result}{RESET}")
                failed += 1

        except NotImplementedError:
            print(f"  {YELLOW}? SKIP{RESET}  {label}  (not implemented yet)")
            errors += 1
        except Exception as e:
            print(f"  {RED}✘ ERR {RESET}  {label}")
            print(f"         {type(e).__name__}: {e}")
            errors += 1

        print()

    print(f"{BOLD}{CYAN}{'─' * 60}{RESET}")
    total = len(test_cases)
    if failed == 0 and errors == 0:
        print(f"  {GREEN}{BOLD}All {passed}/{total} tests passed!{RESET}")
    else:
        print(f"  {GREEN}Passed:{RESET} {passed}   {RED}Failed:{RESET} {failed}   {YELLOW}Errors:{RESET} {errors}   Total: {total}")
    print(f"{BOLD}{CYAN}{'─' * 60}{RESET}\n")

    return failed == 0 and errors == 0

if __name__ == "__main__":
    ok = run_tests()
    sys.exit(0 if ok else 1)
