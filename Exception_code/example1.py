def calculator(a,b,operation):
    try:
        if operation == "add":
            return a + b
        if operation == "subtract":
            return a - b
        if operation == "multiply":
            return a * b
        if operation == "division":
            return a / b
        else:
            raise ValueError("Invalid Operator")
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except ArithmeticError:
        return "Math error occured"
    except Exception as e:
        return f"An error occured {e}"
    
print (calculator(5,2,"division"))
print (calculator(5,0,"division"))
print(calculator(5, 2, "unknown"))

            

        