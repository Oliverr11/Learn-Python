def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
gen = my_generator()

print(next(gen))

print("-"*20)

for myGen in gen:
    print(myGen)
    
for num in range(1,10):
    print(num)
    
print("-"*20)
def my_rang(min,max):
    while min < max:
        yield min
        min +=1
    
for num in my_rang(1,10):
    print(num)
        