def characterReplacement(str, limit):
    result = 0
    left = 0

    count = {}

    for right in range(len(str)):
        count[str[right]] = 1 + count.get(str[right], 0)

        if (right - left + 1) - max(count.values()) > limit:
            count[str[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result


if "__main__" == __name__:
    s = "AABA"
    k = 2
    max = characterReplacement(s, k)
    print("result", max)
