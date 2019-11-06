import re
import time

# computes the value of a function at x
def get_function_value(eqn, x):
    return sum([coeff * (x ** power) 
        for coeff, power in eqn])

# computes the value of the first derivative of a function 
# at x
def get_derivative_value(eqn, x):
    return sum([coeff * power * (x ** max(power - 1, 0)) 
        for coeff, power in eqn])

def bisection(eqn, a, b, epsilon):
    mid = 0
    while abs(a - b) > epsilon:
        mid = (a + b) / 2
        if get_function_value(eqn, a) * get_function_value(eqn, mid) < 0:
            b = mid
        else:
            a = mid
    return mid

def newton_raphson(eqn, init, epsilon):
    x_prev = init
    while True:
        deriv = get_derivative_value(eqn, x_prev)
        if deriv == 0:
            break
        x_cur = x_prev - get_function_value(eqn, x_prev) / deriv
        if abs(x_prev - x_cur) <= epsilon:
            return x_cur
        x_prev = x_cur

    return None

def secant(eqn, a, b, epsilon):
    while True:
        # compute function values at a and b
        f_a = get_function_value(eqn, a)
        f_b = get_function_value(eqn, b)

        x = (a * f_b - b * f_a) / (f_b - f_a)

        if abs(b - x) <= epsilon:
            return x

        a = b
        b = x

    return None

# derives an equation from a string to produce an 
# array of (coefficient, power) pairs
def extract_equation(string):
    rx = re.compile(r'([\+\-]?\d*)([a-z]*)(\d*)')
    matches = rx.findall(string.replace(' ', ''))
    result = []

    for coeff, variable, power in matches:
        if not coeff:
            if not variable:
                continue
            else:
                coeff = '1'
        elif coeff == '-' or coeff == '+':
            coeff += '1'

        if not power:
            power = '1' if variable else '0'

        result.append((float(coeff), float(power)))

    return result

def main():    
    print("")
    print("*******************************************************")
    print("* CSC 225 - Computational Methods")
    print("*")
    print("* Author: John Afolayan (https://github.com/jnafolayan)")
    print("*")
    print("* ----------------------------------------------------")
    print("* Solve any polynomial equation using the Bisection, ")
    print("* Newton Raphson, or Secant method")
    print("*******************************************************")
    print("")

    raw_eqn = input('(?) Enter the polynomial you want to solve:\n> ')
    methods_map = {
        'bisection':      { 'args': 'a, b, epsilon', 'func': bisection },
        'newton_raphson': { 'args': 'start, epsilon', 'func': newton_raphson },
        'secant':         { 'args': 'a, b, epsilon', 'func': secant }
    }

    while True:
        method_str = input('(?) What method do you want to use? (bisection / newton_raphson / secant)\n> ')
        if method_str not in methods_map:
            print('Method not supported! Try again')
            continue

        method = methods_map[method_str]
        method_args = method.get('args')
        method_func = method.get('func')
        args = eval(input(f'(?) Supply arguments ({method_args}):\n> '))
        eqn = extract_equation(raw_eqn)

        millis = lambda: int(round(time.time() * 1000))
        
        start_time = millis()
        result = method_func(eqn, *args)
        for i in range(1000000):
            continue
        duration = millis() - start_time

        print('The solution to the equation is:', result)
        print('-----')
        print(f'The {method_str} algorithm ran in {duration} milliseconds')

        break

if __name__ == '__main__':
    main()