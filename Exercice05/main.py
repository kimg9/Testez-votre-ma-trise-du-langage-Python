def sum(a, b):
    """
    return the result of the sum of two numbers.
    
    Attributes
    -----------
    :attr a: first number of sum
    :type a: int
    :attr b: second number of sum
    :type b: int
    """
    return a + b
 
def subtraction(a, b):
    """
    return  the result of the substration of two numbers.
    
    Attributes
    -----------
    :attr a: first number of sum
    :type a: int
    :attr b: second number of sum
    :type b: int
    """
    return a - b

print(f"\nResult of sum of 4 + 5 is :{sum(4, 5)}")
print(f"\nDocstring of sum function is: {sum.__doc__}")
print(f"\nResult of substraction of 10 - 6 is: {subtraction(10, 6)}")
print(f"\nDocstring of substraction function is: {subtraction.__doc__}")
