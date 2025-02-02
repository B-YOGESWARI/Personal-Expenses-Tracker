def my_generator():
    for i in range(1,6):
        yield i*i
gen=my_generator()
for num in gen:
    print(num)