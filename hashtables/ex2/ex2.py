#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # O(len(tickets) + length)

    route = [None] * length

    cache = dict()

    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    destination = cache["NONE"]
    # sets up the initial flight since the source is NONE

    for i in range(length):
        route[i] = destination
        destination = cache[destination]
        # recalculating the destination to be the new destination of the current destination

    return route
