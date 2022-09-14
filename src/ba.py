"""Module for computing border arrays."""


def border_array(x:str):
    """
    Construct the border array for x.

    >>> border_array("aaba")
    [0, 1, 0, 1]
    >>> border_array("ississippi")
    [0, 0, 0, 1, 2, 3, 4, 0, 0, 1]
    >>> border_array("")
    []
    """
    if x == '' or x == None:
        return []
        
    ba = [0]
    j = 0
    for i in range(1,len(x)):
        while x[i] != x[j] and j > 0:
            j = ba[j-1]
        if x[i] == x[j]:
            ba.append(j+1)
            j+=1
        if j == 0:
            ba.append(j)      
    return ba


def strict_border_array(x:str):
    """
    Construct the strict border array for x.

    A strict border array is one where the border cannot
    match on the next character. If b is the length of the
    longest border for x[:i+1], it means x[:b] == x[i-b:i+1],
    but for a strict border, it must be the longest border
    such that x[b] != x[i+1].

    >>> strict_border_array("aaba")
    [0, 1, 0, 1]
    >>> strict_border_array("aaaba")
    [0, 0, 2, 0, 1]
    >>> strict_border_array("ississippi")
    [0, 0, 0, 0, 0, 0, 4, 0, 0, 1]
    >>> strict_border_array("")
    []
    """
    if x == '' or x == None:
        return []

    ba = border_array(x)
    for i in range(len(ba)-1):
        if ba[i+1] > ba[i]:
            ba[i]=0
        if ba[i+1] < ba[i]:
            ba[i+1] = 0
    return ba
