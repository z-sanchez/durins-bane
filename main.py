# Time Complexity: O(n^2), nested loops
# Space Complexity: O(n), creating a result array

# The idea here is that you focus on one value at a time. Take that value and find what other two summed with it = 0. Then move to next index.
# We don't have to worry about comparing results using previous array values because those have been exhausted and check for
# Rule of thumb: Once we've passed an index in the array, those values have been checked if there in play already, no need to compare back

def subsWithoutDupes(s):

    result = 0
    charSet = set()

    left = 0
    right = 0

    for letter in s:
        while letter in charSet:
            charSet.remove(s[left])
            left += 1

        charSet.add(letter)
        right += 1

        result = max((right - left), result)

    return result


if "__main__" == __name__:
    s = "zxyzxyz"

    result = subsWithoutDupes(s)
    print(result)
