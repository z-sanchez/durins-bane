
def productsOfArrayExceptSelf(nums):
    result = []

    prefix = 1

    for index in range(len(nums)):
        if index == 0:
            result.append(prefix)
        else:
            prefix *= nums[index - 1]
            result.append(prefix)

    postfix = 1

    for index in range(len(nums))[::-1]:
        result[index] *= postfix

        postfix *= nums[index]

    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    print(productsOfArrayExceptSelf(nums))
