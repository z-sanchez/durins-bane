# Time Complexity: O(m * n)
# Space Complexity: O(m), uses a count map
# m = length of string, n = length of unique characters in string

def characterReplacement(s: str, k: int) -> int:
    # map used to track frequency of specific chars
    count = {}
    result = 0

    # start of the window
    left = 0

    # right represents the end of our window
    for right in range(len(s)):
        count[s[right]] = 1 + count.get(s[right], 0)

        if (right - left + 1) - max(count.values()) > k:
            count[s[left]] -= 1
            left += 1

        result = max(result, (right - left + 1))

    return result


if "__main__" == __name__:
    s = "AABA"
    k = 2
    max = characterReplacement(s, k)
    print("result", max)
