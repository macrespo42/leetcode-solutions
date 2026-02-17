def is_palindrome(s):
    text = [c.lower() for c in s if c.isalpha()]
    start = 0
    end = len(text) - 1
    while start < end:
        if text[start] != text[end]:
            return False
        start += 1
        end -= 1
    return True