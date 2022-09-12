a = int(input("Enter Number 1 : "))
b = int(input("Enter Number 2 : "))

mx = max(a, b)

for i in reversed(range(mx)):
    if (a%i==0 and b%i==0):
        print(f"HCF of {a} and {b} is {i}")
        exit()
