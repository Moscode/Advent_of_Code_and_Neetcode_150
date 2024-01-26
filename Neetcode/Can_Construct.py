def Can_Construct(target, arr):
    if target == "":
        return True
    for string in arr:
        suffix_start = target.find(string)
        if suffix_start == 0:
            suffix = target[len(string):]
            if Can_Construct(suffix, arr):
                return True
    return False

print(Can_Construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
