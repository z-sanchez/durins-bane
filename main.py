

def dailyTemperatures(temperatures):

    result = [0 for x in range(len(temperatures))]
    tempTracker = []

    for index, temp in enumerate(temperatures):

        while len(tempTracker) > 0 and temp > tempTracker[-1][1]:
            tempTrackerIndex, tempTrackerTemp = tempTracker.pop()
            result[tempTrackerIndex] = index - tempTrackerIndex

        tempTracker.append([index, temp])

    return result


if "__main__" == __name__:
    temperatures = [30, 38, 30, 36, 35, 40, 28]

    result = dailyTemperatures(temperatures)
    print(result)
