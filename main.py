def subsWithoutDupes(s: str) -> int:

    charSet = set()
    result = 0
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
