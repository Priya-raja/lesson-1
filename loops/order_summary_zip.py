names = ["PRiya", "JOHN", "jane", "ALICE", "bob"]
bills = [25.50, 30.75, 15.00, 22.25, 18.90]


for name,bill in zip(names,bills):
    print(f"{name.title()} : ${bill:.2f}")