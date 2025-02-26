def isPalindrome(strInput):
    i = 0
    j = len(strInput) - 1

    while (i < j):
        while (i < j and not strInput[i].isalpha() and not strInput[i].isdigit()):
            i += 1
        while (j > i and not strInput[j].isalpha() and not strInput[j].isdigit()):
            j -= 1

        print(i, j)

        if (strInput[i].lower() != strInput[j].lower()):
            return False

        i = i + 1
        j = j - 1

    return True


if __name__ == "__main__":
    s = "0P"

    s = s.lower().replace(" ", "")

    print(s[0].isdigit())
    print(isPalindrome(s))
