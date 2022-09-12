cardsPostion = []

for position in range(20):
    cardsPostion.append(1)    
    
print(cardsPostion)

while True:
    try:
        n = int(input("Enter any Cards Position : "))
        
        if n > 20:
            print("Program Exit !!")
            exit()
        else:
            if cardsPostion[n] == 1:
                cardsPostion[n] = 0
                if cardsPostion[n+1] == 1:
                    cardsPostion[n+1] = 0
                else:
                    cardsPostion[n+1] = 1
                print(cardsPostion)
            else:
                print("Cards Position is Already Up Please select Another Card Position")
                
    except Exception as e:
        print('Enter Valid Number')