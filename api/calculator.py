from math import inf


def operation(calc: list, operator_str: str, operator_function) -> bool:
    if operator_str in calc:
        pos = calc.index(operator_str)
        calc[pos] = operator_function(calc[pos-1], calc[pos+1])
        del calc[pos+1]
        del calc[pos-1]
        return True
    else:
        return False


def calculate(calc: list) -> int:

    def firstpos(lst: list, val: str) -> int:
        return lst.index(val) if val in lst else inf

    def lastpos(lst: list, val: str):
        lst.reverse()
        i = lst.index(val)
        lst.reverse()
        return len(lst) - i - 1

    if len(calc) == 1:
        return calc[0]

    # brackets
    bstart = firstpos(calc, '(')
    if bstart < inf:
        bend = lastpos(calc, ')')
        inside_value = calculate(calc[bstart+1:bend].copy())
        del calc[bstart+1:bend+1]
        calc[bstart] = inside_value
        return calculate(calc)

    # multiplication
    m = firstpos(calc, '*')
    d = firstpos(calc, '/')
    if min(m, d) < inf:
        if m < d:
            operation(calc, '*', lambda x, y: x * y)
        else:
            operation(calc, '/', lambda x, y: x / y)
        return calculate(calc)

    # addition
    a = firstpos(calc, '+')
    s = firstpos(calc, '-')
    if min(a, s) < inf:
        if a < s:
            operation(calc, '+', lambda x, y: x + y)
        else:
            operation(calc, '-', lambda x, y: x - y)
        return calculate(calc)

    return calculate(calc)
