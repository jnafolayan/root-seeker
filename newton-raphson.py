def newton_raphson(eqn, init, epsilon):

    def get_value(eqn, x):
        result = 0
        for coeff, power in eqn:
            result += coeff * (x ** power)
        return result

    def get_derivative_value(eqn, x):
        result = 0
        for coeff, power in eqn:
            result += coeff * power * (x ** max(power - 1, 0)) 
        return result

    x_prev = init
    while True:
        deriv = get_derivative_value(eqn, x_prev)
        if deriv == 0:
            break
        x_cur = x_prev - get_value(eqn, x_prev) / deriv
        if abs(x_prev - x_cur) <= epsilon:
            return x_cur
        x_prev = x_cur

    return None
