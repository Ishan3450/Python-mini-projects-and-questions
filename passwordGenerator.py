import string
import random

s = []
s.extend(list(string.ascii_lowercase))
s.extend(list(string.ascii_uppercase))
s.extend(list(string.digits))
s.extend(list(string.punctuation))

# try catch is used for if used inputed any other password length value apart from integet
try:
    passLen = int(input("Enter Your Password Length : "))
        # this will shuffle all the elements in the s list
    random.shuffle(s)

    # after shuffling we have to just fetch the lenght entered by the user from the list s
    password = "".join(s[0:passLen])
    print(password)

    with open('GeneratedPasswords.txt','a') as f:
        f.write(f"{password}\n")

except Exception as e:
    print("Enter Only Inegers no any Other Value will be Accepted")

