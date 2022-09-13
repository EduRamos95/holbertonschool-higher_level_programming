def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)
    first_a, second_a = 0, 0
    first_b, second_b = 0, 0
    if a > 0:
        first_a = tuple_a[0]
        if a > 1:
            second_a = tuple_a[1]
    if b > 0:
        first_b = tuple_b[0]
        if b > 1:
            second_b = tuple_b[1]
    tup = ((first_a + first_b), (second_a + second_b))
    return tup
