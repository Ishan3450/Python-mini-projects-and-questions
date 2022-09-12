# solved by self

if __name__ == "__main__":
    
    number = input("Enter any Number here : ")
    length = len(number)

    l = []
    for item in range(length):
        l.append(int(number[item]))
        
    l2=[]
    for item in l:
        l2.append(item ** length)

    armstrongNumber = sum(l2)

    summary = f'''
    Summary : 
    Entered Number : {number}
    Length of That Number : {length}
    Armstrong of That Number : {armstrongNumber}
    '''
    print(summary)

    if int(number) == armstrongNumber:
        print(f"{number} is an Armstrong Number !!")
    else:
        print(f"{number} is not an Armstrong Number !!")