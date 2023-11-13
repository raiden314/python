def mul_func(a,b): return a*b
def add_func(a,b): return a+b
def calc_53( func ):
    return func(5,3)

result = calc_53(mul_func)
print(result)