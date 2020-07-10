def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # O(lenght + 2) - O(2length)
    cache = dict()

    # cache index at the weight value for each weight
    for i in range(length):
        cache[weights[i]] = i
    for i in range(length):
        # find the suppliment that ads with the weight to equal the limit
        suppliment = limit - weights[i]
        if suppliment in cache:
            # .index is the first occurence of the value so it takes care of duplicate occurances that add up to the limit
            return (cache[suppliment], weights.index(weights[i]))

    return None
