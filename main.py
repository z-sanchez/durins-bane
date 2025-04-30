def encode(input):
    output = ''

    for x in input:
        output += str(len(x)) + '#' + x

    return output


def decode(key):
    output = []
    currentPoint = 0

    while currentPoint < len(key):
        delimiterPointer = currentPoint

        while key[delimiterPointer] != '#':
            delimiterPointer += 1

        strLength = int(key[currentPoint:delimiterPointer])
        delimiterPointer += 1
        string = key[delimiterPointer:delimiterPointer + strLength]
        output.append(string)

        currentPoint = delimiterPointer + strLength

    return output


if "__main__" == __name__:
    input = ["ziek", "loves", "bella", "alot"]
    encodedStr = encode(input)
    decodedList = decode(encodedStr)
    print(decodedList)
