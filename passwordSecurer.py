SECURE = (('s','$'),('i','!'),('a','@'),('I','|'),('and','&'),('h','#'),('o','0'))

def secureMyPassword(password):
    for a,b in SECURE:
        password = password.replace(a,b)
    return password

if __name__ == '__main__':
    password = input("Enter Your Password : ")

    securedPassword = secureMyPassword(password)

    print(f"Your Secured Password is {securedPassword}")

    with open('securedPassword.txt','a') as f:
        f.write(f"{securedPassword}\n")
