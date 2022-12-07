print("Country List:1.Indian Rupee, 2.US Dollar, 3.Canadian Dollar, 4.Pounds, 5.Euros, 6.ChineseYuan, 7.RussiaRubal")
a=int(input("From Country: "))
b=int(input("To Country: "))
amount=float(input("Enter Amount: "))
if a==1:
    if b==2:
        print(amount*0.012,"USD")
    elif b==3:
        print(amount*0.016,"CAD")
    elif b==4:
        print(amount*0.010,"GBP")
    elif b==5:
        print(amount*0.012,"EUR")    
    elif b==6:
        print(amount*0.087,"CNY")
    elif b==7:
        print(amount*0.74,"RUB")
if b==1:
    if a==2:
        print(amount*81.25,"INR")
    elif a==3:
        print(amount*61.11,"INR")
    elif a==4:
        print(amount*95.49,"INR")
    elif a==5:
        print(amount*83.58,"INR")
    elif a==6:
        print(amount*11.49,"INR")
    elif a==7:
        print(amount*1.35,"INR")
else:
    print("Invalid")

