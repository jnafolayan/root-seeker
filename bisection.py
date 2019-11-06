def bisection(a, b, epsilon):
    mid = 0
    while abs(a - b) > epsilon:
        mid = (a + b) / 2
        if a * mid < 0:
            b = mid
        else:
            a = mid
    return mid