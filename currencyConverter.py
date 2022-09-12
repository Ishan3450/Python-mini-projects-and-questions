with open('currencyConverterData.txt','r') as f:
    content = f.readlines()

currDict = {}

for line in content:
    parsed = line.split('\t')
    currDict[parsed[0]] = parsed[1]


amount = int(input("Enter INR Amount Which You want to Convert : "))

print("Available Option : \n")
[print(item) for item in currDict.keys()]

toWhich = input(f"Enter into Which You want to Convert {amount} INR : ")

print(f"{amount} INR will be {amount * float(currDict[toWhich])} {toWhich}") 

