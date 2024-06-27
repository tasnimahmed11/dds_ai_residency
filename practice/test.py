import itertools

def fibonacii():
    a, b = 0, 1
    while True: 
        yield a
        a, b = b, a + b

fib = fibonacii()
result = itertools.islice(fib, 10)
print(list(result))