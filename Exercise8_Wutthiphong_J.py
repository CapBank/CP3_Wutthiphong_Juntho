Apple = 10
Papaya = 5
Banana =8
usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput  == "Customer"  and passwordInput == "asdf":
    print("--------ร้านผลไม้--------")
    print("1. แอปเปิ้ล         ",Apple,"฿")
    print("2. มะละกอ         ",Papaya  ,"฿" )
    print("3. กล้วย           ",Banana,"฿")
    userSelected = int(input("วันนี้รับผลไม้อะไรดี >>"))
    if userSelected == 1:
        fruit = "แอปเปิ้ล"
        Number = int(input("จำนวน  : "))
        price =Number*Apple
    elif userSelected == 2:
        fruit = "มะละกอ"
        Number = int(input("จำนวน  : "))
        price =Number*Papaya
    elif userSelected == 3:
        fruit = "กล้วย"
        Number = int(input("จำนวน  : "))
        price =Number*Banana
    print(fruit, "จำนวน", Number, "ทั้งหมดราคา", price, "฿")
    print("ขอบคุณที่ใช้บริการ")
else:
    print("error")