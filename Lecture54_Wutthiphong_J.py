def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        print("usernuame or password is wrong!!")
        print("Try again!!")
        return login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = input(">>")
    if userSelected != "1" and userSelected != "2" :
        print("Please select 1 or 2 ")
        showMenu()
        return menuSelect()
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)
login()
showMenu()
if menuSelect()== "1":
    print(vatCalculator(int(input("Total Price :"))))
else:
    print(priceCalculator())
print("thank you")





