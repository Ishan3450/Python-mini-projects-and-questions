i=0
sum = 0
itemName = []
itemPrice = []
while (True):
    name = input("Enter Name of the Item : ")
    price = input("Enter Price of Item : ")
    if price == 'q' or name == 'q':
        print("Thank You ! Visit Again.")
        break
    else:
        itemName.append(name)
        itemPrice.append(price)
        sum = sum + int(price)
    i += 1
print("\nOrder Summary : \n")
for item in range(i):
    print(f'''
    Item Name : {itemName[item]}
    Item Price : {itemPrice[item]}''')


print("\nYour Total Bill is :" ,sum)