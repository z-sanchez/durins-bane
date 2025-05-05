# Time Complexity = O(n) we traverse the array once
# Space Complexity = O(1) No space needed

def encode(list):
    result = ""

    for x in list:
        result += str(len(x)) + "#" + x
    return result


def decode(encodedString):

    pointer = 0
    result = []

    while pointer < len(encodedString):

        delimiterPointer = pointer

        while encodedString[delimiterPointer] != "#":
            delimiterPointer += 1

        strLength = int(encodedString[pointer:delimiterPointer])

        delimiterPointer += 1

        str = encodedString[delimiterPointer: delimiterPointer + strLength]

        result.append(str)

        pointer = delimiterPointer + strLength

    return result


if "__main__" == __name__:
    list = ["ziek", "loves", "cheese", "alot"]
    encodedString = encode(list)
    decodedMessage = decode(encodedString)
    print(decodedMessage)
