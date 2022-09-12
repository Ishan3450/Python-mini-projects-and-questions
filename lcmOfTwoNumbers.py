num1 = int(input("Enter Number 1 :"))
num2 = int(input("Enter Number 2 : "))

maxNum = max(num1,num2)

while True:
    if maxNum%num1==0 and maxNum%num2==0:
        print(f"Lcm of {num1} and {num2} is {maxNum}")
        exit()        
    else:
        maxNum+=1

print("Done!")