def characterReplacement(str, limit):

    charSet = {}
    left = 0
    result = 0

    for right in range(len(str)):
        charSet[str[right]] = 1 + charSet.get(str[right], 0)

        if (right - left + 1) - max(charSet.values()) > limit:
            charSet[str[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result


if "__main__" == __name__:
    s = "AABA"
    k = 2
    max = characterReplacement(s, k)
    print("result", max)
