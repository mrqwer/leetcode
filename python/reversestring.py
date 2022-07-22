def reverseStr(s: str, k: int) -> str:
    return s[:k][::-1] + s[k:2 * k] + reverseStr(s[2*k:], k) if s else ""

print(reverseStr("abcdefg", 2))
