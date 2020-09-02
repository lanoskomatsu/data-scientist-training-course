def calc_multi(a, b):
    return a * b
x = calc_multi(3, 10)
print(x)

y = (lambda a, b: a * b)(3, 10)
print(y)

def calc_double(x):
    return x * 2
for num in [1,2,3,4]:
    print(calc_double(num))

print(list(map(calc_double, [1,2,3,4])))

print(list(map(lambda x : x * 2, ([1,2,3,4]))))