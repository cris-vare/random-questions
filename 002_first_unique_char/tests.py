import sys
import time
from solution import first_unique_char

GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

test_cases = [
    # (description, input, expected)
    ("first char is unique",              "leetcode",          "l"),
    ("last char is unique",               "aabbc",             "c"),
    ("no unique chars",                   "aabb",              ""),
    ("single character",                  "z",                 "z"),
    ("all same character",                "aaaa",              ""),
    ("unique char in the middle",         "abacabad",          "c"),
    ("first of two uniques",              "abcd",              "a"),
    ("case sensitive — upper unique",     "aAaB",              "A"),
    ("case sensitive — lower unique",     "AaAb",              "a"),
    ("digits in string",                  "112233a",           "a"),
    ("symbols in string",                 "!!@@#",             "#"),
    ("long string, unique near end",      "ab" * 1000 + "c",  "c"),
    ("two chars alternating",             "ababab",            ""),
    ("unique is second char",             "aab",               "b"),
    ("empty-like: one repeated pair",     "cc",                ""),
]

def run_tests():
    print(f"\n{BOLD}{CYAN}{'─' * 60}{RESET}")
    print(f"{BOLD}{CYAN}  002 — First Unique Character{RESET}")
    print(f"{BOLD}{CYAN}{'─' * 60}{RESET}\n")

    passed = 0
    failed = 0
    errors = 0

    for i, (desc, s, expected) in enumerate(test_cases, 1):
        label = f"Test {i:02d}  {desc}"
        display = s if len(s) <= 20 else s[:20] + "..."
        try:
            start = time.perf_counter()
            result = first_unique_char(s)
            elapsed = (time.perf_counter() - start) * 1000

            if result == expected:
                print(f"  {GREEN}✔ PASS{RESET}  {label}")
                print(f"         input={repr(display)}  →  {repr(result)}  ({elapsed:.2f}ms)")
                passed += 1
            else:
                print(f"  {RED}✘ FAIL{RESET}  {label}")
                print(f"         input    = {repr(display)}")
                print(f"         expected = {YELLOW}{repr(expected)}{RESET}")
                print(f"         got      = {RED}{repr(result)}{RESET}")
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
