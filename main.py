
# Time Complexity: O(n), iterates through string once
# Space Complexity: O(1), no extra space needed

from typing import List


def encode(strs):

    result = ""

    for word in strs:
        result += str(len(word)) + "#" + word

    return result


def decode(str):

    result = []
    cursor = 0

    while cursor < len(str):
        delimiter = cursor

        while str[delimiter] != "#":
            delimiter += 1

        length = int(str[cursor:delimiter])

        word = str[delimiter + 1:delimiter + 1 + length]

        result.append(word)
        cursor = delimiter + 1 + length

    return result


if __name__ == "__main__":

    strs = ["need", "code", "love", "you"]
    encodedOutput = encode(strs)

    print(decode(encodedOutput))
