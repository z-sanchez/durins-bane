# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(1), no new data structure needed

def checkInclusion(s1, s2):

    s1Count = [0] * 26

    for char in s1:
        s1Count[ord(char) - ord('a')] += 1

    s1Key = tuple(s1Count)

    s2Count = [0] * 26
    left = 0

    for right in range(len(s2)):
        s2Count[ord(s2[right]) - ord('a')] += 1

        if (right - left + 1) > len(s1):
            s2Count[ord(s2[left]) - ord('a')] -= 1
            left += 1

        s2Key = tuple(s2Count)

        if s1Key == s2Key:
            return True

    return False


if "__main__" == __name__:
    s1 = "abc"
    s2 = "lecabee"

    print(checkInclusion(s1, s2))
