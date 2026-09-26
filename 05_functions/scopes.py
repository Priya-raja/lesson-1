def serve_chai():
    chai_type = "MAsala"
    print(f"Inside function {chai_type}")

chai_type ="Lemon"
serve_chai()
print(f"Outside function:{chai_type}")

 
# Demo of enclosing 

def chai_counter():
    chai_flav = "Tulsi"
    # print(f"The outer:", {chai_flav})

    def ginger_tea():
        chai_flav = "ginger"
        print("This is inner:", chai_flav)
    ginger_tea()
    print("This is outer", chai_flav)

chai_counter()
chai_flav = "Wagh Bhaker"
print("This is Global", chai_flav)