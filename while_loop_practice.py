#..............while loop()........................
#practice on while loop().......................
'''a=10
while a>1:
    print(a)
    a-=1'''

'''a=10
while a>=1:
    print(a)
    a-=1'''

'''a=10
while a<=15:
    print(a)
    a+=1'''

'''a=10
while a>=1:
    print(a)
    a+=1'''
'''a=10
while a>=1:
    print(a)
    a-=2'''

'''a=10
while a>=1:
    a-=2
    print(a)'''

'''a=30
while a>=1:
    print(a)
    a-=1'''

'''a=4
while a<30:
    print(a)
    a+=1'''

'''a=0
while a<=30:
    print(a,end=" ")
    a+=1'''

#task-1
'''while True:
    age=int(input("Enter age:"))
    if age>=18:
        print("Eligible for vote")
        if age==50:
            break
    else:
        print("Not eligible for vote")'''
    
#................range()........................
'''for i in range(21):
    print(i,end=" ")'''

'''for i in range(5,21):
    print(i,end=" ")'''
'''
for i in range(1,20,2):
    print(i,end=" ")'''

'''for i in range(20,30,1):
    print(i)'''
#task-2...print 1 to 100 numbers
'''for i in range(1,101,1):
    print(i,end=" ")'''

#task-2...print 1 to 100 even numbers
'''for i in range(0,101,2):
    print(i,end=" ") '''

'''for i in range(5,501,5):
    print(i,end=" ")'''

#task-3......students grade based on marks
'''while True:
    marks=int(input("Enter your original marks"))
    if marks in range(91,101):
        print("Grade-A")
    elif marks in range(81,91):
        print("Grade-B")
    elif marks in range(71,81):
        print("Grade-C")
    elif marks in range(51,71):
        print("Grade-D")
    else:
        print("Sorry you are Failed the exam")
    if marks<20:
        break; '''

#task-4........Attandance based report..............
'''students=int(input("Enter the number of students:"))
p=0
a=0
for i in range(1,students+1):
    print(f"the student {i} p or a")
    status=input("Enter student is present or absent:")
    if status=="p":
        p+=1
    elif status=="a":
        a+=1
print("....................Student Attandance Report...................")
print("Total number of students:",students)
print("Total presenties:",p)
print("Total Absenties:",a)'''

#..................................................................
#practice for problem solving of break,continue and pass
#.............................break()...................
'''a=2
while a<=18:
    a+=1
    if a==5:
        break
    print(a,end=" ")'''

'''a=20
while a>=10:
    a-=1
    print(a,end=" ")
    if a==15:
        break'''

'''for i in range(-7,1,1):
    print(i,end=",")
    if i==-2:
        break'''
'''for i in range(-3,-5):
    print(i)'''

'''for i in range(3,10,-2):
    print(i)'''
#................continue()...............
'''a=2
while a<=18:
    a+=1
    if a==5:
        continue
    print(a,end=" ")'''

'''a=30
while a>2:
    a-=1
    if a==28:
        continue
    print(a,end=" ")'''    

'''a=20
while a<=50:
    a+=1
    if a==28:
        continue
    print(a,end=" ")'''


