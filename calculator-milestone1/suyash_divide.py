#function for divide operation
def  calc_divide(a,b):
    c = a/b
    return c

#Taking  a and b as inputs
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))

#get and display result
result = calc_divide(a,b)
print(result)
