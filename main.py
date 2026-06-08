
# Time Complexity: O(n), iterates through string once
# Space Complexity: O(1), no extra space needed

from typing import List


def encode(strs):
    result = ""

    for char in strs:
        result += str(len(char)) + "#" + char

    return result


def decode(str):
    result = []

    cursor = 0

    while (cursor < len(str)):
        delimiter = cursor

        while (str[delimiter] != "#"):
            delimiter += 1

        length = int(str[cursor:delimiter])

        result.append(str[delimiter + 1: delimiter + 1 + length])

        cursor = delimiter + 1 + length

    return result


if __name__ == "__main__":

    strs = ["need", "code", "love", "you"]
    encodedOutput = encode(strs)

    print(decode(encodedOutput))
