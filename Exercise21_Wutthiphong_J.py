from tkinter import *
import math

def calculate(event):
    bmi = float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2)
    if bmi >=30:
        resultText = "อ้วนมาก"
    elif bmi >=25 :
        resultText = "อ้วน"
    elif bmi >= 23 :
        resultText = "น้ำหนักเกิน"
    elif bmi >= 18.6:
        resultText = "น้ำหนักปกติ เหมาะสม"
    else:
        resultText = "ผอมเกินไป"
    lableResult.configure(text =resultText )

MainWindow = Tk()
lableHeight =Label(MainWindow,text = "ส่วนสูง")
lableHeight.grid(row = 0, column =0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row = 0, column =1)
lableWeight =Label(MainWindow,text = "น้ำหนัก")
lableWeight.grid(row = 1, column =0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text="คำนวณ")
calculateButton.bind("<Button-1>",calculate)
calculateButton.grid(row=2)
lableResult =Label(MainWindow,text = "ผลลัพธ์")
lableResult.grid(row = 2, column =1)
MainWindow.mainloop()