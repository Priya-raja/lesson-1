def serve_chai():
    yield "cup1: Masala chai"
    yield "cup2: Ginger chai"
    yield "cup3: Lemon chai"

stall = serve_chai()
print(next(stall))
print(next(stall))

# for cup in stall:
#     print(cup)