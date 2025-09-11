#mass to kg
kilogram=0.454
mass=float(input("Enter the mass in pounds: "))
kilograms=mass*kilogram
print('Mass in kg=',format(kilograms,'.2f'),"kg")



#miles,gallons
miles=float(input("enter the miles driven="))
gallons=float(input("enter the gallons used="))
MPG=miles*gallons
print("Miles per gallons= ",format(MPG,'.2f'),"mpg")



#subtotal,tax,total
item1=float(input("enter item1="))
item2=float(input("enter item2="))
item3=float(input("enter item3="))
item4=float(input("enter item4="))
item5=float(input("enter item5="))
subtotal=item1+item2+item3+item4+item5
print('subtotal= $',subtotal)
salesTax=0.07
tax=subtotal*salesTax
print('tax=',tax,'$')
total=tax+subtotal
print('Total= ',format(total,'.2f'),'$')





#tax,amount,monthly cost
purchase=float(input("Enter the purchased amount="))
instalment=int(input("Enter the instalment number="))
tax=0.05
totalTax=purchase*tax
print('total tax=',totalTax,'$')
totalAmount=totalTax+purchase
print("total purchase amount=",format(totalAmount,'.2f'),"$")
monthlyCost=totalAmount/instalment
print("total monthly cost=",format(monthlyCost,".2f"),"$")


#value
a=float(input("enter the value: "))
if a<10:
    b=0
else:
    b=99
print(b)


#rect1,rect2
length1=float(input("enter the length of rect1: "))
width1=float(input("enter the width of rect1: "))
length2=float(input("enter the length of rect2: "))
width2=float(input("enter the width of rect2: "))
area1=length1*width1
area2=length2*width2
if area1>area2:
    print("area of rect1 is greater than rect2")
elif area2>area1:
    print("area of rect2 is greater than rect1")
else:
    print("both area of the rect1 and rect2 are the same")


#integer 
x=int(input("enter integer: "))
if x>0:
    print("positive")
elif x<0:
    print("negative")
else:
    print("zero")
if x%2==1:
    print("odd")
else:
    print("even")


#month quater
month=int(input("enter month [1-12]: "))
if month>=1:
    print("the first quater")
elif month>=4:
    print("the second quater")
elif month>=7:
    print("the third quater")
elif month>=10:
    print("the fourth quater")
else:
    print("error")