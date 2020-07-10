# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    # O(len(files) + (len(queries) * len(cache[query])))

    cache = dict()
    result = list()

    for file in files:
        split_file = file.split("/")
        filename = split_file[-1]
        # Taking the last index value and having that value equal the filename

        if filename not in cache:
            cache[filename] = list()
        cache[filename].append(file)
        # Multiple files can end in the same filename so we place all the files in the same list

    for query in queries:
        if query in cache:
            for i in cache[query]:
                result.append(i)
                # There is a list of files associated with the query so we iterate over the list and append the results

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
