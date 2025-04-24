def encode(array):
    encodedStr = ""
    delimiter = "#"

    for x in range(len(array)):
        encodedStr += str(len(array[x])) + delimiter + str(array[x])

    return encodedStr


def decode(str):
    result = []
    pointer = 0

    while pointer < len(str):
        delimiterPosition = pointer

        while str[delimiterPosition] != '#':
            delimiterPosition += 1

        strLen = int(str[pointer:delimiterPosition])
        delimiterPosition += 1

        word = str[delimiterPosition: delimiterPosition + strLen]
        pointer = delimiterPosition + strLen
        result.append(word)

    return result


if "__main__" == __name__:
    input = ["ziek", "loves", "cheese", "alot"]

    print("Input: ", input)
    encodedStr = encode(input)
    print("Encoded: ", encodedStr)
    decodedArray = decode(encodedStr)
    print("Decoded: ", decodedArray)

    print("Result Matches: ", input == decodedArray)
