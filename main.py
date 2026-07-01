# Time Complexity: O(m * n)
# Space Complexity: O(m), uses a count map
# m = length of string, n = length of unique characters in string

def characterReplacement(s: str, k: int) -> int:
    charSet = set()
    result = 0
    left = 0

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        result = max(result, right - left + 1)
        charSet.add(s[right])

    return result


if "__main__" == __name__:
    s = "AABA"
    k = 2
    max = characterReplacement(s, k)
    print("result", max)
