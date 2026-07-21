def characterReplacement(string, limit):

    left = 0
    result = 0
    count = {}

    for right in range(len(string)):
        count[string[right]] = 1 + count.get(string[right], 0)

        if (right - left + 1) - max(count.values()) > limit:
            count[string[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result


if "__main__" == __name__:
    s = "AABA"
    k = 2
    max = characterReplacement(s, k)
    print("result", max)
