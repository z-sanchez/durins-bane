def subsWithoutDupes(s: str) -> int:

    charSet = set()
    maxCount = 0
    left = 0

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1

        charSet.add(s[right])
        maxCount = max(maxCount, right - left + 1)

    return maxCount


if "__main__" == __name__:
    s = "xyzxzyyzx"

    result = subsWithoutDupes(s)
    print(result)
