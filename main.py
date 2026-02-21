# Time Complexity: O(n^2), nested loops
# Space Complexity: O(n), creating a result array

# The idea here is that you focus on one value at a time. Take that value and find what other two summed with it = 0. Then move to next index.
# We don't have to worry about comparing results using previous array values because those have been exhausted and check for
# Rule of thumb: Once we've passed an index in the array, those values have been checked if there in play already, no need to compare back

def dailyTemperatures(temperatures):
    result = [0] * len(temperatures)

    stack = []

    for index, temp in enumerate(temperatures):
        while stack and stack[-1][1] < temp:
            stackIndex, stackTemp = stack.pop()
            result[stackIndex] = index - stackIndex
        stack.append([index, temp])

    return result


if "__main__" == __name__:
    temperatures = [30, 38, 30, 36, 35, 40, 28]

    result = dailyTemperatures(temperatures)
    print(result)
