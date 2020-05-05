(lambda a, b: print(a * b))(3, 10)

def calc_double(x):
    return x * 2

print(list(map(calc_double, [1, 2, 3, 4])))

print(list(map(lambda x: x * 2, [1, 2, 3, 4])))
