# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(1), no new data structure needed

def subsWithoutDupes(s):

    left = 0
    charSet = set()

    result = 0

    for right in range(len(s)):

        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1

        charSet.add(s[right])

        result = max((right - left + 1), result)

    return result


if "__main__" == __name__:
    s = "xyzxzyyzx"

    result = subsWithoutDupes(s)
    print(result)
