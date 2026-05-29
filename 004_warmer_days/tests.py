import sys
import time
from solution import warmer_days

GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

test_cases = [
    # (description, input, expected)
    ("basic mixed",                  [70, 72, 68, 75, 75],           2),
    ("always warming",               [60, 61, 62, 63],               3),
    ("always cooling",               [80, 79, 78],                   0),
    ("single day",                   [50],                           0),
    ("two days warmer",              [10, 20],                       1),
    ("two days colder",              [20, 10],                       0),
    ("equal stays flat",             [5, 5, 5, 5],                   0),
    ("negatives warming",            [-10, -5, 0, 5],                3),
    ("zigzag",                       [1, 2, 1, 2, 1, 2],             3),
    ("dip then climb",               [30, 28, 27, 40, 41],           2),
    ("all same except one warmer",   [3, 3, 4, 3],                   1),
    ("long ramp",                    list(range(100)),               99),
]

def run_tests():
    print(f"\n{BOLD}{CYAN}{'─' * 60}{RESET}")
    print(f"{BOLD}{CYAN}  004 — Warmer Days{RESET}")
    print(f"{BOLD}{CYAN}{'─' * 60}{RESET}\n")

    passed = 0
    failed = 0
    errors = 0

    for i, (desc, temps, expected) in enumerate(test_cases, 1):
        label = f"Test {i:02d}  {desc}"
        display = repr(temps) if len(repr(temps)) <= 30 else repr(temps)[:30] + "...]"
        try:
            start = time.perf_counter()
            result = warmer_days(temps)
            elapsed = (time.perf_counter() - start) * 1000

            if result == expected:
                print(f"  {GREEN}✔ PASS{RESET}  {label}")
                print(f"         input={display}  →  {result}  ({elapsed:.2f}ms)")
                passed += 1
            else:
                print(f"  {RED}✘ FAIL{RESET}  {label}")
                print(f"         input    = {display}")
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
