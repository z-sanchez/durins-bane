# Time Complexity: O(n), nested loops
# Space Complexity: O(1), creating nothing

def encode(array):
    encodedStr = ""
    for x in array:
        encodedStr += str(len(x)) + '#' + x
    return encodedStr


def decode(str):
    result = []
    startingPlace = 0
    while startingPlace < len(str):
        cursor = startingPlace
        while str[cursor] != '#':
            cursor += 1

        strLen = int(str[startingPlace: cursor])
        result.append(str[cursor + 1: cursor + 1 + strLen])
        startingPlace = cursor + 1 + strLen

    return result


if "__main__" == __name__:
    # must be in order for it to work
    array = ["Ziek", "Loves", "Cheese"]
    print("Input", array)
    encodedResult = encode(array)
    print("Encoded Result", encodedResult)
    decodedResult = decode(encodedResult)
    print("Decoded Result", decodedResult)
    print("Solved: ", array == decodedResult)
