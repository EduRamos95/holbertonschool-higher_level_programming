# C implementation of the last Pythonic loop
#
#    triangle = [[1]]
#    for rows in range(n-1):
#        l = [1]
#        for i in range(rows):
#            l.append(triangle[-1][i] + triangle[-1][i+1])
#        l.append(1)
#        triangle.append(l)
#    return triangle
