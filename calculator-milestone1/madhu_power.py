#function for power operation
def  calc_power(num,pow):
    return num**pow

#Taking  num and pow as inputs
num = int(input("Enter value of a : "))
pow = int(input("Enter value of b : "))

#get and display result
result = calc_power(num,pow)
print(result)
