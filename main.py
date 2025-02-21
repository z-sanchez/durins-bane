def productsOfArrayExceptSelf(nums):
    result = []
    product = 1

# pre products
    for x in range(len(nums)):
        if x == 0:
            result.append(product)
        else:
            product = product * nums[x - 1]
            result.append(product)

    postfix = 1

    for x in range(len(nums) - 1, -1, -1):
        result[x] *= postfix
        postfix *= nums[x]

    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    print(productsOfArrayExceptSelf(nums))
