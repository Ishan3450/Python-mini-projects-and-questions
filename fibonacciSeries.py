a = 0
b = 1
sum = 0
count = 0

number = int(input("Enter any Number : "))

while (count <= number):
    print(sum,end =" ")
    a = b
    b = sum
    sum = a+b
    count += 1