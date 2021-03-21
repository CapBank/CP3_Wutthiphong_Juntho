menuList = []
systemMenu = {"kfc":100,"pizza":200,"donut":50}

def showBill():
    print("----My Food----")
    totalPrice = 0
    for number in range(len(menuList)):
        totalPrice += int(menuList[number][1])
        print(menuList[number][0],menuList[number][1])
    print("Total :",totalPrice)

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

showBill()
