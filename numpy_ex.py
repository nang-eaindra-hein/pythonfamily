# Numpy
import numpy as np
a = np.array([10,20,30,40])     #array
c = np.arange(1,7)   #will arange 1 to 6
f = np.arange(0,9,3)  #start=0,end=9,step=3

b = np.array([[100,200,300,400],
              [500,600,700,800]])    #array as matrix( first row ,sec col)

d = np.zeros([3,3])  #rows,cols filled with zero
e = np.ones([3,])   #rows 3 ,no col  filled with 1
g = np.linspace(0,1,5)  #start=0 end=1 step=5 (0 0.25 0.5 0.75 1)  space evenly


x = a >35

print(a)
print(a[0]) #first value
print(a[-1])#last value

print(a ** 2) # all array power up to 2
print (a[:4])  #from first value to 4th value
print(a * b)  #array a and array b math

print(b.shape)   #total rows,cols
print(b.dtype)   #datatype int64
print(b[:,1])  #all rows,col 2
print(b[0,1])  #row 3,col 2
print(b.sum())    # all value sum
print(b.sum(axis=0)) #all rows sum 
print(b.sum(axis=1))  #all cols sum
print(b.mean(),b.max(),b.min())  #average num,max ,min
print(b[:2,1:])   #rows from start to 2 rows,cols from sec to last 

print(x) #boolean (true false)
print(a[x]) #true answer value

print(c.reshape(2,3))  #reshape the value into matrix
print(c.reshape(2,3).T)  # transpose,flip row and col
print(np.eye(3))  #matrix start to end with 3 in middle must be 3

print("\n\n\n\n EXERCISE \n\n\n")
print("exer 1.\n\n")
#Exercise 1: Student Scores,You have exam scores: [55, 72, 90, 38, 84].
# Find the average score.Print only the scores ≥ 60 (passing students)Find the highest and lowest score.

exam_score = np.array([55,72,90,38,84])

passing_student = exam_score >= 60 

print(exam_score.mean()) #avg score
print(exam_score[passing_student])  #>=60
print(exam_score.max(), exam_score.min())  #max and min

print("\n\nexer 2.\n\n")
#Exercise 2: Temperature Tracking,Temperatures recorded in a week (°C): [30, 32, 29, 28, 31, 33, 27].
# Convert all temperatures to Fahrenheit (F = C * 9/5 + 32).Find the hottest day.find the average temperature.
Tempreture = np.array([30, 32, 29, 28, 31, 33, 27])

Fahrenheit = Tempreture * 9 / 5 +32

print(Fahrenheit)
print (Tempreture.max(), Tempreture.mean() )

print("\n\nexer 3.\n\n")
#Exercise 3: Sales Data,A shop sold items over 6 months: [120, 150, 100, 180, 90, 200].Find the total sales.
# Reshape this into a 2x3 matrix (2 rows, 3 months each).Print the second row (last 3 months).
sold_items = np.array([120, 150, 100, 180, 90, 200])
reshaped_items = sold_items.reshape(2,3)

print(sold_items.sum())
print(reshaped_items)
print(reshaped_items[1])