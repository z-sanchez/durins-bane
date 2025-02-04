def groupAnagrams(strs):
    result = {}

    for word in strs:
        countTable = [0] * 26
        for char in word:
            index = ord(char) - ord('a')
            countTable[index] += 1

        if (tuple(countTable) in result):
            result[tuple(countTable)].append(word)
        else:
            result[tuple(countTable)] = []
            result[tuple(countTable)].append(word)

    return result.values()


if __name__ == "__main__":
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]

    result = groupAnagrams(strs)

    print(result)


# create hash table (keys = count of letters in the form of tuples, values = list of words matching the tuples letter count)
# loop through words
# create the key a-z with all 0s
# calculate the index ord(char) - ord('a')
# append in the index
# use table.values() to return the values in table
