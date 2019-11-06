def secant(eqn, a, b, epsilon):
    def get_value(eqn, x):
        result = 0
        for coeff, power in eqn:
            result += coeff * (x ** power)
        return result

    while True:
        # compute function values at a and b
        f_a = get_value(eqn, a)
        f_b = get_value(eqn, b)

        x = (a * f_b - b * f_a) / (f_b - f_a)

        if abs(b - x) <= epsilon:
            return x

        a = b
        b = x

    return None
