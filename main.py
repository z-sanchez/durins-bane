
def checkInclusion(s1, s2):

    count = [0] * 26

    for char in s1:
        count[ord(char) - ord('a')] += 1

    countsOfStr1 = tuple(count)

    left = 0
    newCount = [0] * 26

    for right in range(len(s2)):
        newCount[ord(s2[right]) - ord('a')] += 1

        testTuple = tuple(newCount)

        if testTuple == countsOfStr1:
            return True
        elif (right - left + 1) >= len(s1):
            newCount[ord(s2[left]) - ord('a')] -= 1
            left += 1

    return False


if "__main__" == __name__:

    s1 = "abc"
    s2 = "lecabee"

    print(checkInclusion(s1, s2))
