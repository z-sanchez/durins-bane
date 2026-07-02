# Time Complexity: O(m * n)
# Space Complexity: O(m), uses a count map
# m = length of string, n = length of unique characters in string


def subsWithoutDupes(s: str) -> int:

    result = 0

    left = 0

    strSet = set()

    for right in range(len(s)):
        while s[right] in strSet:
            strSet.remove(s[left])
            left += 1
        strSet.add(s[right])
        result = max(result, right - left + 1)

    return result


if "__main__" == __name__:
    s = "xyzxzyyzx"

    result = subsWithoutDupes(s)
    print(result)
