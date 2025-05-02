def trappingRainwater(height):

    if not height:
        return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]

    result = 0

    # To Calculate Water Trapped:
    # wall bounded by          current wall
    # min(leftMax, rightMax) - height[i]
    # you cannot trap water any higher than the smallest wall

    while l < r:
        # solve with the smallest wall (bounded wall)
        if leftMax < rightMax:
            # advance wall to focus on a new spot
            l += 1

            # left max is basically the tallest wall prior to current one
            # here we find the 'ceiling'
            leftMax = max(leftMax, height[l])

            # then we subtract the height of our current wall from the ceiling
            result += leftMax - height[l]
        else:
            r -= 1
            # right max is basically the tallest wall prior to current one
            rightMax = max(rightMax, height[r])
            result += rightMax - height[r]

    return result


if "__main__" == __name__:
    height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    result = trappingRainwater(height)
    print(result)
