def all_n(n):
    if n == 1:
        return "1"
    else:
        return str(all_n(n - 1)) + " " + str(n)


def all_range_n(a, b):
    if a == b:
        return str(a)
    elif b > a:
        return str(all_range_n(a, b - 1)) + " " + str(b)
    elif b < a:
        return str(a) + " " + str(all_range_n(a - 1, b))


def akkerman(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akkerman(m - 1, 1)
    else:
        return akkerman(m - 1, akkerman(m, n - 1))


def is_base2(x):
    if x == 2:
        return True
    elif 1 <= x < 2:
        return False
    return is_base2(x / 2.0)


def digit_sum(x):
    if x < 1:
        return 0
    elif x < 10:
        return x
    else:
        return x % 10 + digit_sum(int(x / 10))


def permutations(L, P, i=0):
    n = len(L)
    if i == n - 1:
        P.append(L.copy())
        return
    else:
        for k in range(i, n):
            L[i], L[k] = L[k], L[i]
            permutations(L, P, i + 1)
            L[i], L[k] = L[k], L[i]
