num = int(input("Enter anu Number to Find it's Factorial : "))
fact = 1
i=1
trailingzero = 0
for i in range(num+1):
    if i>=1:
        fact = fact * i
    if(fact%10==0):
        trailingzero += 1
print(f"Your Factorial of {num} is {fact} having trailing zeroes {trailingzero}")

