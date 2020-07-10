def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # 0(n^2)

    cache = dict()

    for arr in arrays:
        for num in arr:
            if num in cache:
                cache[num] += 1
            else:
                cache[num] = 1
    # With the counter set, if the number has a count equal to the len of the array then it means it is in all the arrays, getting the value we need
    result = [count[0] for count in cache.items() if count[1] == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
