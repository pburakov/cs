def get_bit(num, i):
    return (num & (1 << i)) != 0


def set_bit(num, i):
    return num | (1 << i)


def clear_bit(num, i):
    mask = ~(1 << i)
    return num & mask


def update_bit(num, i, bit_value):
    mask = ~(1 << i)
    return (num & mask) | (bit_value << i)


print(get_bit(1, 0))
print(get_bit(3, 1))
print(get_bit(8, 1))

print(set_bit(1, 2))
print(set_bit(3, 2))
print(set_bit(8, 1))

print(clear_bit(1, 0))
print(clear_bit(3, 0))
print(clear_bit(123, 6))
