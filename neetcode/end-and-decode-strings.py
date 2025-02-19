
# Time Complexity: O(n), iterates through string once
# Space Complexity: O(1), no extra space needed

from typing import List


def encode(strs):

    result = ""

    # we can't use any state so they trick is to store it in string using delimiter
    # length + # + actual string (ex. 4#love3#the)
    for x in strs:
        result += str(len(x)) + "#" + x

    return result


def decode(str):

    result = []
    i = 0

    # iterate through string
    while (i < len(str)):
        j = i
        # set j to the end delimiter
        while (str[j] != "#"):
            j += 1
        # capture length of string, doesn't include j
        length = int(str[i: j])

        # append from j + 1 (first letter of word) to length of word
        result.append(str[j + 1: j + 1 + length])

        # advance i to the index of the first part of delimiter
        i = j + 1 + length

    return result


if __name__ == "__main__":

    strs = ["need", "code", "love", "you"]
    encodedOutput = encode(strs)

    print(decode(encodedOutput))
