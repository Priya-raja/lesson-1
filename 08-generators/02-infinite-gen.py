# Used in streams

def infinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1

refill = infinite_chai()

for _ in range(10):
    print(next(refill))