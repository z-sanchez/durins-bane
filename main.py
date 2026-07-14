def characterReplacement(str, limit):
    result = 0

    left = 0
    charSet = set()

    for right in range(len(str)):
        while str[right] in charSet:
            charSet.remove(str[left])
            left += 1

        charSet.add(str[right])
        result = max(result, right - left + 1)

    return result


if "__main__" == __name__:
    s = "AABA"
    k = 2
    max = characterReplacement(s, k)
    print("result", max)
