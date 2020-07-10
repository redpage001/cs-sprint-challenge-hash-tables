def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # O(n)

    cache = dict()
    result = list()

    for i in range(len(a)):
        cache[a[i]] = True
        if a[i] != 0 and -a[i] in cache:
        # negative 0 equals positive 0 so we disregard zero.
        # the - sign changes the sign of the number to be the opposite and checks to see if it is in the cache
            result.append(abs(a[i]))
            # appending the absolute value of a[i]

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
