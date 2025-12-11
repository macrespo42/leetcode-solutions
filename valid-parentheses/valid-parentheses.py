def is_valid(s: str):
    stack = []
    open = ["(", "[", "{"]
    closed = [")", "]", "}"]
    for elt in s:
        if (elt in open):
            stack.append(elt)
        elif elt in closed:
            if len(stack) == 0:
                return False
            popped = stack.pop()
            if (closed.index(elt) != open.index(popped)):
                return False
    return len(stack) == 0

if __name__ == "__main__":
    print(is_valid("()")) # True
    print(is_valid("()[]{}")) # True
    print(is_valid("(]")) # False
    print(is_valid("({})")) # True
    print(is_valid("([)]")) # False