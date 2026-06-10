# 3 important decorators in Python are:@staticmethod, @classmethod, and @property.

# class Total:
#     def __init__(self):
#         #private attribute
#         self._amount = 10

#     def amount(self):
#         return self._amount


# total1 = Total()
# print(total1.amount())  # Output: 10        

# Using @property decorator to make the method act like an attribute
class Total:
    def __init__(self):
        #private attribute
        self._amount = 10

    @property
    def amount(self):
        return self._amount
total1 = Total()
print(total1.amount)  # Output: 10    

     