
def checkInclusion(s1, s2):
    s1Count = [0] * 26

    for char in s1:
        s1Count[ord(char) - ord('a')] += 1

    s1Key = tuple(s1Count)

    left = 0
    s2Count = [0] * 26

    for right in range(len(s2)):
        if tuple(s2Count) == s1Key:
            return True

        s2Count[ord(s2[right]) - ord('a')] += 1

        if (right - left + 1) > len(s1):
            s2Count[ord(s2[left]) - ord('a')] -= 1
            left += 1

    return False


if "__main__" == __name__:

    s1 = "abc"
    s2 = "lecabee"

    print(checkInclusion(s1, s2))
