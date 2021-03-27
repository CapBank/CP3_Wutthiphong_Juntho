from forex_python.converter import *
from datetime import *
from statistics import *
from tkinter import *
from tkinter import ttk


def convert_currency():
    try:
        currency_rate = CurrencyRates()
        result_label2.configure(text=currency_rate.convert(currency_input_list.get(), currency_output_list.get(), float(amount.get())))
    except ValueError:
        error_label.configure(text='Amount must be number !!', fg='red')
    except:
        error_label.configure(text='Currency Input Or Currency Output Incorrect !!', fg='red')

def data_per_week():
    today = date.today()
    currency_rate = CurrencyRates()
    day_1 = timedelta(days=1)
    result_per_day = []
    try:
        for i in  range(7):
            result_per_day.append(currency_rate.get_rate(currency_input_list.get(), currency_output_list.get(),today))
            today -= day_1
        return result_per_day
    except:
        pass

def show_data():
    min_label2.configure(text=min(data_per_week()))
    avg_label2.configure(text=mean(data_per_week()))
    max_label2.configure(text=max(data_per_week()))

def left_click_button(event):
    error_label.configure(text='')
    convert_currency()
    data_per_week()
    show_data()

main_windown = Tk()

main_windown.title("Currency Exchang")
currency_list = ["USD","JPY","EUR","THB","IDR","BGN","ILS","GBP","AUD","CHF","HKD"]
currency_input_label = Label(main_windown, text='Currency Input')
currency_output_label = Label(main_windown, text='Currency Output')
currency_input_list = ttk.Combobox(main_windown, values=currency_list)
currency_input_list.current(0)
currency_output_list = ttk.Combobox(main_windown, values=currency_list)
currency_output_list.current(3)
to_lable = Label(main_windown, text='To')
amount_lable = Label(main_windown, text="Amount")
amount = Entry(main_windown)
exchang_button = Button(main_windown, text='Exchng !!')
exchang_button.bind('<Button-1>',left_click_button)
result_label1 = Label(main_windown, text='Result =')
result_label2 = Label(main_windown, text='')
lastweek_label = Label(main_windown, text='Exchang Rate Last Week')
min_label1 = Label(main_windown, text='min')
min_label2 = Label(main_windown, text='')
avg_label1 = Label(main_windown, text='avg')
avg_label2 = Label(main_windown, text='')
max_label1 = Label(main_windown, text='max')
max_label2 = Label(main_windown, text='')
error_label = Label(main_windown,)

currency_input_label.grid(column=0, row=0)
currency_output_label.grid(column=2, row=0)
currency_input_list.grid(column=0, row=1)
to_lable.grid(column=1, row=1)
currency_output_list.grid(column=2, row=1)
amount_lable.grid(column=0, row=4)
amount.grid(column=0, row=5)
exchang_button.grid(column=2, row=5)
result_label1.grid(column=0, row=6)
result_label2.grid(column=2, row=6)
error_label.grid(column=1, row=7)
lastweek_label.grid(column=1, row=10)
min_label1.grid(column=0, row=11)
min_label2.grid(column=0, row=12)
avg_label1.grid(column=1, row=11)
avg_label2.grid(column=1, row=12)
max_label1.grid(column=2, row=11)
max_label2.grid(column=2, row=12)

main_windown.mainloop()
