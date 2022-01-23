from time import time
  
  
def function_timer(func):

    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f} sec')
        return result
    return wrap_func
  
  
@function_timer
def long_time(n):
    for i in range(n):
        for j in range(80000):
            i*j
  
  
long_time(2)