from typing import List


def encode(strs):
    encoded = ""

    for word in strs:
        encoded += str(len(word)) + "#" + word

    return encoded


def decode(str):

    pointer = 0

    result = []

    while pointer < len(str):
        delimiter = pointer

        while str[delimiter] != "#":
            delimiter += 1

        wordLength = int(str[pointer:delimiter])

        word = str[delimiter + 1: delimiter + 1 + wordLength]

        result.append(word)

        pointer = delimiter + 1 + wordLength

    return result


if __name__ == "__main__":

    strs = ["need", "code", "love", "you"]
    encodedOutput = encode(strs)

    print(decode(encodedOutput))
