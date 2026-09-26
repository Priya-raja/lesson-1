# def prepare_chai(*ingrediants, **extras):

#     print("these are the ingrediants", ingrediants)
#     print("This is the extras", extras)

# prepare_chai("milk","tea","sugar", elem="elaichi",leaf="mint")

def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)

make_chai("Darjeeling","Yes","No")  #positional
make_chai(tea="Darjeeling", sugar="Less", milk="No") #keywords


def chai_order(order=None):

    if order is None:
        order = []
    order.append("Masala")
    print(order)

chai_order()
