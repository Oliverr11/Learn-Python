def decorate(orignal_func):
    def wrap():
        func_a()
        return orignal_func()
    return wrap

def func_a():
    print("A")

def func_b():
    print("B")

@decorate
def func_c():
    print("C")


func_c()


# decor = decorate(func_c)
# decor()