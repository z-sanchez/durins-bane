
# Time Complexity: O(n), iterates through string once
# Space Complexity: O(1), no extra space needed

from typing import List


def encode(strs):

    result = ""

    for string in strs:
        result += str(len(string)) + "#" + string

    return result


def decode(str):
    pointer = 0
    result = []

    while pointer < len(str):
        delimiterPointer = pointer

        while str[delimiterPointer] != "#":
            delimiterPointer += 1

        stringLength = int(str[pointer:delimiterPointer])

        delimiterPointer += 1

        string = str[delimiterPointer: delimiterPointer + stringLength]

        result.append(string)

        pointer = delimiterPointer + stringLength

    return result


if __name__ == "__main__":

    strs = ["need", "code", "love", "you"]
    encodedOutput = encode(strs)

    print(encodedOutput)
    print(decode(encodedOutput))
