# iterative Algo

def exp_iter(base, power):
    exp = 1

    for i in range(1, power):
        exp = exp * base

    return exp

# Recursive Algo

def exp_recur(base, power):
    if power == 0:
        return 1
    else:
        return base * exp_recur(base, power - 1)