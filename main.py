def subsWithoutDupes(s: str) -> int:
    charSet = set()
    maxLength = 0

    left = 0

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1

        charSet.add(s[right])
        maxLength = max(maxLength, right - left + 1)

    return maxLength


if "__main__" == __name__:
    s = "xyzxzyyzx"

    result = subsWithoutDupes(s)
    print(result)
