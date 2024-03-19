def generator(start, step):
    number = start
    while True:
        yield number
        number *= step

start = -2
step = -5
gen = generator(start, step)

for _ in range(6):
    print(next(gen))

print("*" * 20)

start = 10
step = 3
gen = generator(start, step)

for _ in range(6):
    print(next(gen))