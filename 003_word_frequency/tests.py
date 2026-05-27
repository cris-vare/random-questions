import sys
import time
from solution import word_frequency

GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

test_cases = [
    # (description, input, expected)
    ("basic sentence",               "the cat sat on the mat",       {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}),
    ("all same word",                "hello hello hello",            {"hello": 3}),
    ("single word",                  "one",                          {"one": 1}),
    ("case insensitive",             "The the THE",                  {"the": 3}),
    ("mixed case different words",   "Cat cat DOG dog",              {"cat": 2, "dog": 2}),
    ("two words",                    "hi there",                     {"hi": 1, "there": 1}),
    ("all unique words",             "one two three four",           {"one": 1, "two": 1, "three": 1, "four": 1}),
    ("one word repeated many times", "go " * 5 + "go",              {"go": 6}),
    ("longer sentence",              "to be or not to be",           {"to": 2, "be": 2, "or": 1, "not": 1}),
    ("uppercase sentence",           "HELLO WORLD HELLO",            {"hello": 2, "world": 1}),
]

def run_tests():
    print(f"\n{BOLD}{CYAN}{'─' * 60}{RESET}")
    print(f"{BOLD}{CYAN}  003 — Word Frequency{RESET}")
    print(f"{BOLD}{CYAN}{'─' * 60}{RESET}\n")

    passed = 0
    failed = 0
    errors = 0

    for i, (desc, sentence, expected) in enumerate(test_cases, 1):
        label = f"Test {i:02d}  {desc}"
        display = sentence if len(sentence) <= 30 else sentence[:30] + "..."
        try:
            start = time.perf_counter()
            result = word_frequency(sentence)
            elapsed = (time.perf_counter() - start) * 1000

            if result == expected:
                print(f"  {GREEN}✔ PASS{RESET}  {label}")
                print(f"         input={repr(display)}  →  {result}  ({elapsed:.2f}ms)")
                passed += 1
            else:
                print(f"  {RED}✘ FAIL{RESET}  {label}")
                print(f"         input    = {repr(display)}")
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
