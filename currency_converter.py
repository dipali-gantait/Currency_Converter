# Currency rates compared to 1 INR (approx, Oct 2025)
import os
import sys
import time

"""
1. \033 -> used to start ANCI logic
2. \033[y;xH -> move curser to (x,y) position
3. \033[38;5;0 to \033[38;5;256 -> used for color
4. \033[0m -> used to turn off ANCI code logic
Example : print("\033[38;5;1m Hello World \033[0m")
Here \033[38;5;1m says that turn on Red color and \033[0m says that
turn off all color and turn on normal command color
""" 
def move(x,y):
    print(f"\033[{y};{x}H",end="")

def box_maker(column,row,position=[1,1]):
    for i in range(1,row+1):#2
        move(position[0],position[1]+(i-1))
        if i==1 or i== row:
            print("+",end="")
            for j in range(column-2):
                print("-",end="")
            print("+")
        else:
            print("|",end="")
            for i in range(column-2):
                print(" ",end="")
            print("|")

def aviable_country():
        print("Aviable country")
os.system("cls")
column = os.get_terminal_size().columns
x=(column-len("Currency Converter"))//2
move(x,1)
print("\033[4m\033[38;5;226mCurrency Converter\033[0m")
x_of_box = (column-40)//2
box_maker(40,5,[x_of_box,4])
while True:
    try:
        move(x_of_box+1,5)
        amount=float(input("Enter amount :"))
        break
    except:
        text_length=len("Give only floating point value")
        move((column-text_length)//2,9)
        print("\033[31m\033[5mGive only floating point value\033[0m")
        move(x_of_box+1,5)
        print(" "*38,end="")
move(x_of_box+1,6)
from_cur = input("Want to conver from:").upper()
move(x_of_box+1,7)
to_cur = input("Want convert to:").upper()
move(0,16)






# move(x-10,4)
# print("Enter amount :",end="")
# amount=input()













# box_maker(30,5,[10,7])
# move(11,8)
# print("Enter name:",end="")
# name=input()
# move(11,9)
# print("Enter adress:",end="")
# addr=input()
# move(11,10)
# print("Enter pincode:",end="")
# pin=input()
# move(11,12)













# print_in_middle("\033[4m\033[38;5;226mCurrency Converter\033[0m")
# print_in_middle("Enter the amount:")
# def print_in_middle(value):
    # column = os.get_terminal_size().columns
    # space = (column-len(value))//2
    # for i in range(space):
        # print(" ",end="")
    # print(value,end="")

# rates_vs_inr = {
    # "USD": 88.73,     # US Dollar
    # "EUR": 103.77,    # Euro
    # "GBP": 118.43,    # British Pound
    # "JPY": 0.60,      # Japanese Yen (~1 INR = 1.67 JPY)
    # "CNY": 12.20,     # Chinese Yuan
    # "AUD": 57.8,      # Australian Dollar
    # "CAD": 63.6,      # Canadian Dollar
    # "RUB": 1.06,      # Russian Ruble
    # "SAR": 23.65,     # Saudi Riyal
    # "AED": 24.15,     # UAE Dirham
    # "BDT": 1.07,      # Bangladeshi Taka
    # "NPR": 0.63,      # Nepalese Rupee
    # "PKR": 0.32,      # Pakistani Rupee
    # "LKR": 0.30,      # Sri Lankan Rupee
    # "CHF": 101.22,    # Swiss Franc
    # "ZAR": 4.85,      # South African Rand
    # "KRW": 0.066,     # South Korean Won (~1 INR = 15.15 KRW)
    # "THB": 2.47,      # Thai Baht
    # "SGD": 66.05,     # Singapore Dollar
    # "MYR": 18.77,      # Malaysian Ringgit
    # "INR": 1           # Indian rupiee
# }

# def currency_converter( amount , from_cur , to_cur):
    # if from_cur not in rates_vs_inr or to_cur not in rates_vs_inr:
        # return "Invalid currency"
    # else:    
        # in_INR = amount*rates_vs_inr[from_cur]   
        # result = in_INR / rates_vs_inr[to_cur]
        # return result 


# 
# print("Enter the name of currency that you want to convert this amount ? avilable option \n")
# print(rates_vs_inr.keys())
# from_cur = input("from currency:  ").upper()
# to_cur = input("to currency:   ").upper()
# converted = currency_converter( amount , from_cur , to_cur)
# if isinstance( converted , str):
    # print(converted)
# else:
    # print(f"\n{amount} {from_cur} = {converted:.2f} {to_cur}")
