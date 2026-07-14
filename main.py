# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(n), we make a set here

def subsWithoutDupes(str):
    result = 0

    charSet = set()

    left = 0

    for right in range(len(str)):
        while str[right] in charSet:
            charSet.remove(str[left])
            left += 1

        charSet.add(str[right])
        result = max(result, right - left + 1)

    return result


if "__main__" == __name__:
    s = "xyzxzyyzx"

    result = subsWithoutDupes(s)
    print(result)
