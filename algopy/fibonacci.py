from time import monotonic as tempo
# from time import clock as tempo
# from time import process_time as tempo
f = [0, 1];

def my_fib(num):
    if num > 1:
        f.append(f[-1] + f[-2])
        my_fib(num - 1)
    elif num == 1:
        return f[num]
    elif num <= 0:
        return None
    return f


def fib(n):
    if n in (1, 0):
        return n
    return fib(n-1) + fib(n-2)


seq = 30


print('\n', my_fib(seq)[-1], f"{tempo():.4f}")
# print('\n', my_fib(seq)[-1], f"{tempo():.4f}")
# print('\n', fib(seq), f"{tempo():.4f}")
