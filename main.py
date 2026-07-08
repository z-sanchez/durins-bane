def subsWithoutDupes(s: str) -> int:
    result = 0
    charSet = set()
    left = 0

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        result = max(result, right - left + 1)

    return result


if "__main__" == __name__:
    s = "xyzxzyyzx"

    result = subsWithoutDupes(s)
    print(result)
