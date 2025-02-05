# Time Complexity = O(m * n) n for the number of elements, m for the length of each char
# Space Complexity = O(m) for the map we create

def groupAnagrams(strs):

    # map will have a tuple as a key, then a list of strings for values
    map = {}

    # loop through list of words
    for word in strs:
        # this count will hold 0s for each char of the alphabet
        count = [0] * 26

        # loop through each char of a word
        for char in word:
            # ascii calculation to bump the count of the current char
            count[ord(char) - ord('a')] += 1

        # this key is now a tuple that has the count of each char in the word
        key = tuple(count)

        # do this or else error
        if key not in map:
            map[key] = []

        # append word to the matching tuple key
        map[key].append(word)

    return map.values()


if __name__ == "__main__":
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]

    result = groupAnagrams(strs)
    print(result)
