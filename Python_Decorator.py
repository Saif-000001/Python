# Function as objects
"""
def f1():
    print('Called f1')
def f2(f):
    f()
f2(f1)
"""

# Wrapper functions
"""
def f1(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper
# method - 1
def f():
    print("Hello")
f1(f)()

# method - 2
@f1
def f():
    print("Hello")
f()

# method - 3
def f():
    print("HELLO")
x = f1(f)
x()

"""

# args and kwargs
"""
def f1(func):
    def wrapper(*args, **kwargs):
        print("Start")
        x = func(*args, **kwargs)
        print("End")
        return x
    return wrapper
@f1
def add(a, b = 9):
    print(a, b)
add("Hi")

@f1
def add(a, b):
    return a + b
print(add(9,5))
"""
# Example - 1
"""
import time
def befor_after(func):
    def wrapper(*args):
        print("Before")
        func(*args)
        print("After")
    return wrapper

class Test:
    @befor_after
    def decoreted_method(self):
        print("run")
t = Test()
t.decoreted_method()
"""

# Example - 2
"""
import time
def timer(func):
    def wrapper():
        before = time.time()
        func()
        print("Function Took :", time.time()-before, "Second")
    return wrapper

@timer
def run():
    time.sleep(2)
run()
"""

# Example - 3
"""
import datetime
def log(func):
    def wrapper(*args, **kwargs):
         with open("logs.txt", "a") as f:
              f.write("Called function with "+" ".join([str(arg) for arg in args])+ " at "+str(datetime.datetime.now())+"\n") 
         x = func(*args, **kwargs)
         return x
    return wrapper

@log
def run(a, b, c = 9):
     print(a+b+c)
run(1,3,c=9)
"""

# Nested Decorator
"""
def first(fn):
    def wrapper():
        print("This is the first decorator")
        fn()
    return wrapper

def second(fn):
    def wrapper():
        print("This is the second decorator")
        fn()
    return wrapper

@first
@second
def f():
    print("Hello World")
f()

#or
def f():
    print("Hello World")
x = first(second(f))
x()
"""

# Passing Arguments to the Decorator
"""
def dector_factor(Flag = True):
    def dector_func(fn):
        from functools import wraps
        @wraps(fn)
        def wrapper_func(*args, **kwargs):
            if Flag :
                print("Flag is True")
            else : 
                print("Flag is False")
            return fn(*args, **kwargs)
        return wrapper_func
    return dector_func

@dector_factor(False)
def orig_func(a,b,c):
    return (print("This is the product : ", a*b*c))
orig_func(7,9,11)
"""
# Passing Arguments to the Function
"""
def pasing_argument(fn):
    def wrapper_argument(a, b):
        print("Argument are pass :", a, b)
        fn(a, b)
    return wrapper_argument
@pasing_argument
def orig_argument(a, b):
    print("city is ",a)
    print("state is ",b)
orig_argument("Barisal", "H S")
"""

# @Logged Decorator
"""
def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone
    @wraps(fn)
    def wrapper(*args, **kwargs):
        run = datetime.now(timezone.utc)
        res = fn(*args, **kwargs)
        print('{0}: called {1}'.format(fn.__name__,run))
        return res
    return wrapper
@logged
def product(a, b, c):
    print("The product is a*b*c = ", a*b*c)
product(7,9,11)
"""
# @Time Decorator
"""
def time(fn):
    from functools import wraps
    from time import perf_counter
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        res =fn(*args, **kwargs)
        end = perf_counter()
        print('{0}: called {1}'.format(fn.__name__, end-start))
        return res
    return wrapper
@logged
@time
def product(a,b,c):
    print("The product of a*b*c :", a*b*c)
product(3,5,6)
"""

# @functools.lru_cache(Memoize)

"""
# without cache
def factor(n):
    print("Factor{0}!".format(n))
    return 1 if n<2 else n*factor(n-1)
factor(5)
"""
# with cache
from functools import lru_cache
@lru_cache()
def factor(n):
    print("Factor{0}!".format(n))
    if n<2:
        return 1
    else : 
        return n*factor(n-1)
factor(5)



