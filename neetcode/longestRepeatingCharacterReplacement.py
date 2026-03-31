def characterReplacement(s: str, k: int) -> int:

    # map used to track frequency of specific chars
    count = {}
    result = 0

    # start of the window
    left = 0

    # right represents the end of our window
    for right in range(len(s)):
        # add 1 to the count of times the char right points at (or default 0)
        count[s[right]] = 1 + count.get(s[right], 0)

        # the condition can be explained with these variables
        # lengthOfWindow = (right - left + 1)
        # maxCharFrequency = max(count.values())
        # countOfDiffCharAllowed = lengthOfWindow - maxCharFrequency
        # validSubstringEnds = countOfDiffCharAllowed > k

        # while the count of diff chars than frequent is more than allowed (k)
        # adjust setup for next substring, adjust count map, move left pointer of window
        while (right - left + 1) - max(count.values()) > k:
            count[s[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result


if "__main__" == __name__:
    s = "XYYX"
    k = 2
    max = characterReplacement(s, k)
    print("result", max)
