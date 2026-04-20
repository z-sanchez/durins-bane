def subsWithoutDupes(s: str) -> int:

    charSet = set()
    left = 0
    result = 0

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        result = max(result, right - left + 1)
        charSet.add(s[right])

    return result


if "__main__" == __name__:
    s = "xyzxzyyzx"

    result = subsWithoutDupes(s)
    print(result)
