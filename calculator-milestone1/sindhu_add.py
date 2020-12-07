#function for add operation
def  calc_add(a,b):
    c = a+b
    return c

#Taking  a and b as inputs
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))

#get and display result
result = calc_add(a,b)
print(result)
