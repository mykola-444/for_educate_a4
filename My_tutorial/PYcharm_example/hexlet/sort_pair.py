def sort_pair(pair):
    (a, b) = pair
    if a > b:
        return (b, a)
    if b > a:
        return (a, b)
    if a == b:
        return (a, b)


def sort_pair1(pair1):
    (f, s) = pair1
    if f > s:
        return (s, f)
    return pair1


assert sort_pair((5, 1)) == (1, 5)
assert sort_pair((2, 2)) == (2, 2)
assert sort_pair((7, 8)) == (7, 8)
