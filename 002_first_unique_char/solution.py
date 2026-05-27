def first_unique_char(s: str) -> str:
    # Write your solution here
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return s[i]
            
    return ""
