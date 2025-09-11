
#tuition
RATE=1.03
YEARS=5
tuition=8000.0
annual_cost=tuition
print("year 0:tuition =${}".format(annual_cost))
for i in range (YEARS):
 annual_cost=annual_cost*RATE
 print("year {}: tuition=${}".format(i+1,format(annual_cost,'.2f')))


#times
def say_n_times(text,n):
    result=text*n
    return result
x=say_n_times("i love you 3000 ",50)
print(x)


#times
def say_n_times(text,n):
    result=''
    for i in range (n):
      result +=text
    return result
x=say_n_times("sorry",50)
print(x)


#base power
def power(base,exponent):
   result=base**exponent
   return result
x=power(3,9)
y=power(9,8)
print(x,"and",y)

base=int(input("enter the base: "))
power=int(input("enter the power: "))
z=base**power
print(z)
          
