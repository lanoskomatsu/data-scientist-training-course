def calc_fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return calc_fib(n - 1) + calc_fib(n - 2)

print("フィボナッチ数:", calc_fib(10))
