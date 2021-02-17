def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
 
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm_result = greater
            break
        greater += 1
 
    return lcm_result

def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf
 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter second number: "))
 
print("The L.C.M. of", num1, "and", num2, "is", lcm(num1, num2))
print("The H.C.F. is", compute_hcf(num1, num2))