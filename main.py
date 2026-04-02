def subsWithoutDupes(s: str) -> int:
    left = 0
    maxCount = 0
    charSet = set()

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1

        maxCount = max(maxCount, right - left + 1)
        charSet.add(s[right])

    return maxCount


if "__main__" == __name__:
    s = "xyzxzyyzx"

    result = subsWithoutDupes(s)
    print(result)
