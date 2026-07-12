# Time Complexity = O(m * n) n for the number of elements, m for the length of each char
# Space Complexity = O(m) for the map we create

def characterReplacement(string, limit):

    count = {}
    result = 0
    left = 0

    for right in range(len(string)):
        count[string[right]] = 1 + count.get(string[right], 0)

        if (right - left + 1) - max(count.values()) > limit:
            count[string[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result


if "__main__" == __name__:
    s = "ABAA"
    k = 0
    max = characterReplacement(s, k)
    print("result", max)
