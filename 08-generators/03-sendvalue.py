# yield gives data but what if we want to send data
def chai_customer():
    print("Welcome! What chai would u like?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_customer()
next(stall) # start the generator

stall.send("masala chai")
stall.send("Lemon tea")