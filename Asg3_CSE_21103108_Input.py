#Question 1

a=str(input("ENTER ANY STRING: "))
list=a.split() 
dict={} 
if list.__len__()==1:   
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
else:                   
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")


#Question 2

list1 = [1,3,5,7,8,10]
list2 = [4,6,9,11]
list3 = [2]
list4 = [12]

day = int(input('Please enter the day: '))
month = int(input('Please enter the month:'))
year = int(input('Please enter the year: ')) 


while True:
    if month in list1:
        if day in range(1,31):
            day+=1
            print('Next date is:', day, '/',month, '/', year) 
        elif day == 31:
            day = 1
            month+=1
            print('Next date is:', day, '/',month, '/', year)     
        else:
            print('Enter valid date!')
    break   
        
while True:
    if month in list2:
        if day in range(1,30):
            day+=1
            print('Next date is:', day, '/',month, '/', year) 
        elif day == 30:
            day = 1
            month+=1
            print('Next date is:', day, '/',month, '/', year)     
        else:
            print('Enter valid date!')
    break    

while True:
    if month in list3:
        if year%4 !=0:
            if day in range(1,28):
                day+=1
                print('Next date is:', day, '/',month, '/', year)
            elif day == 28:    
                day = 1
                month+=1
                print('Next date is:', day, '/',month, '/', year)
            else:
                print('Enter valid date!')    
        elif year%4 == 0:
            if day in range(1,29):
                day+=1
                print('Next date is:', day, '/',month, '/', year)
            elif day == 29:    
                day = 1
                month+=1
                print('Next date is:', day, '/',month, '/', year)
            else:
                print('Enter valid date!')
    break    

while True:
    if month in list4:
        if day in range(1,31):
            day+=1
            print('Next date is:', day, '/',month, '/', year) 
        elif day == 31:
            day = 1
            month = 1
            year += 1
            print('Next date is:', day, '/',month, '/', year)     
        else:
            print('Enter valid date!')
    break       


#Question 3

  list = []
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = int(input('Enter the element: '))
 
    list.append(ele) # adding the element
     
list2 = ()
for x in range(n):
    list2 = [(list[x],list[x]**2) for x in range(n)]

print(list2)      


#Question 4

  grade = int(input('Please enter your grade: '))

if (grade > 0 and grade <4) or grade>10:
    print('Error!')

elif grade >=4 and grade<=10:
    if grade == 4:
        print("Your Grade is 'D' and Poor Performance.")  
    elif grade == 5:
        print("Your Grade is 'C' and Below Average Performance.") 
    elif grade == 6:
        print("Your Grade is 'C+' and Average Performance.") 
    elif grade == 7:
        print("Your Grade is 'B' and Good Performance.") 
    elif grade == 8:
        print("Your Grade is 'B+' and Very Good Performance.") 
    elif grade == 9:
        print("Your Grade is 'A' and Excellent Performance.") 
    elif grade == 10:
        print("Your Grade is 'A+' and Outstanding Performance.") 
                           

#Question 5

  list = ['A','B','C','D','E','F','G','H','I','J','K']

x = 6
for i in range(x):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2*(x-i)-1):
        print(list[j], end='')  
    print()
print("\n")


#Question 6

dict = {}

sid = int(input('Please enter the SID: '))
name = input('Please enter the name: ')
dict.update({sid:name})

while True:
    x = input('Do you want to continue, answer with Y or N?: ').upper()

    if x == 'Y':
       sid = int(input('Please enter the SID: '))
       name = input('Please enter the name: ')
       dict.update({sid:name})
    
    elif x == 'N':
       break
    
    else:
        print('Please choose a valid option')

#Part a
print(dict)    

#Part b
print({k:v for k,v in sorted(dict.items(), key= lambda x:x[1])})

#part c
print({k:v for k,v in sorted(dict.items())})

#part d.
sid = int(input("Search Name with SID: "))
print(dict[sid])


#Question 7

n = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0
sum = 0

if n <= 0:
   print("Please enter a positive integer")

elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nth = n1 + n2 
       n1 = n2
       n2 = nth
       count += 1
       sum = nth - 1
print('Average = ',sum/n)   




#Question 8

Set1 = {1,2,3,4,5}
Set2 = {2,4,6,8}
Set3 = {1,5,9,13,17}

#Part a
Seta = (Set1.union(Set2)) - (Set1.intersection(Set2))
print(Seta)

#Part b
Setb = (Seta.union(Set3)) - (Seta.intersection(Set3))
print(Setb)

#Part c
Setc = ((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print(Setc)

#Part d
new_set1 = set()
for i in range(1,11):
    new_set1.add(i)

Setd = (new_set1 - Set1) 
print(Setd)

#Part e
new_set2 = set()
for i in range(1,11):
    new_set2.add(i)

Sete1 = Set1.union(Set2)
Sete2 = Sete1.union(Set3)
Sete3 = new_set2 - Sete2   
print(Sete3)   