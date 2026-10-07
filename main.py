
# Time Complexity: O(n), iterates through string once
# Space Complexity: O(1), no extra space needed

from typing import List


def encode(strs):
    encodedStr = ''

    for word in strs:
        encodedStr += str(len(word)) + '#' + word

    return encodedStr


def decode(str):
    result = []
    pointer = 0

    while pointer < len(str):
        delimiter = pointer

        while str[delimiter] != "#":
            delimiter += 1

        length = int(str[pointer:delimiter])

        word = str[delimiter + 1: delimiter + 1 + length]

        result.append(word)

        pointer = delimiter + 1 + length

    return result


if __name__ == "__main__":

    strs = ["need", "code", "love", "you"]
    encodedOutput = encode(strs)

    print(decode(encodedOutput))
