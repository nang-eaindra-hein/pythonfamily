#info
def studentname(MyName,MyEmail,MyBBUsername):
    MyName = 'Nang Eaindra Hein@Nang Inn Hein'
    MyEmail = 'eaindraann@gmail.com'
    MyBBUsername = '=944QFHUG'
    return MyName,MyEmail,MyBBUsername

################################################################
print("\nQuestion 1")#number,total

def calAverage(numbers):
    total=sum(numbers)
    length=len(numbers)
    result=total/length
    return result

numbers=[5,3,2,9,33,7]
result=calAverage(numbers)

print("The total of",numbers,">>>>>:",format(result,'.2f'),'\n\n\n')

#######################################################################
    
print("Question 2") #count char in sentence

def countCharacter(sentence):
    tletter=0
    tup=0
    tlow=0
    tdigit=0
    tchar=0

    for char in sentence:
        if char.isalpha():
            tletter +=1
            if char.isupper():
               tup +=1
            else:
               tlow +=1
        elif char.isdigit():
            tdigit +=1
        else:
            tchar +=1
             
                
    return[tletter,tup,tlow,tdigit,tchar]
sentence=("33333*&^%%^I eat applLE")
result=countCharacter(sentence)

print("The total number of' ",sentence," 'are= ",result)
#############################################################################

print("\n\n\nQuestion 3")   #common

def excludeItem (item1,item2):
    result = []
    for item in item1:
        if item in item2 and item not in result:
            result.append(item)
    return result
item1=[2,7,6,8,6,8,5]
item2=[2,4,6,4,6,8,7,5]
result=excludeItem(item1,item2)
print("the value are= ",result)

##########################################################################
print("\n\n\nQuestion 4")     #sec large num

def secondLarge(numbers):
    if not isinstance(numbers,list):
        return -999
    for num in numbers:
        if not isinstance(num,int):
            return -999
    if len(numbers)<2:
        return numbers [0] if numbers else -999
    number1 = list(set(numbers))
    if len(number1)==1:
        return number1[0]
    number1.sort()
    return number1[-2]
print("the second large number >>>> ",secondLarge([1,6,2,7,9,4]))
print(secondLarge([79.,]))
###########################################################################
print("\n\n\nQuestion 5")    #password making

def isValidPassword(password):
    if len(password)<10:
        return False #atleast 10 char
    
    if not any(char.isupper()for char in password)or not any (char.islower()for char in password):
        return False#must include up and low case
    
    if sum (char.isdigit() for char in password)<3:
        return False#must include atleast 3 digits

    special_characters="!@#$%^&*()_+-=[]{};:'\"|,.<>/? "
    if sum(char in special_characters for char in password)<2:
         return False#must include atleast 2 special char
    return True
print(isValidPassword("bgioihr574[';/;."))
print(isValidPassword("Abcdtsa8998<> /"))
                   




