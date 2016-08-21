def is_one_away(A, B):
    if len(A) == len(B):
        return one_replacement_away(A, B)
    elif abs(len(A) - len(B)) < 2:
        return one_insert_away(A, B)
    return False


def one_replacement_away(A, B):
    errors = 0
    for i in range(0, len(A)):
        if A[i] != B[i]:
            errors += 1
        if errors > 1:
            return False
    return True


def one_insert_away(A, B):
    a, b = 0, 0
    errors = 0
    while a < len(A) and b < len(B) and errors < 2:
        if A[a] != B[b]:
            errors += 1
            if a + 1 < len(A) and A[a + 1] == B[b]:
                a += 1
            elif b + 1 < len(B) and B[b + 1] == A[a]:
                b += 1
        else:
            a += 1
            b += 1
    return True


print(is_one_away("pale", "ale"))
print(is_one_away("ple", "pale"))
print(is_one_away("pale", "bake"))
print(is_one_away("pale", "gale"))
