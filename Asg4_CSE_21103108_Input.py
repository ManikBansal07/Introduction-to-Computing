#Question 1

def moveTower(n, source, dest, temp):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", dest+".")
        return
    moveTower(n-1, source, temp, dest) 
    print('Move disk',n,'from source',source,'to destination',dest+'.')
    moveTower(n-1,temp,dest,source)
    
n=3
moveTower(n,'A','B','C')



#Question 2

from math import factorial, remainder
from tracemalloc import start
n=int(input('Enter the size of pascals triangle '))

print("USING FOR LOOP")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ") #for spacing

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	# nCr = n!/((n-r)!*r!)
	print()	# for new line
print("\n\n")

print("USING WHILE LOOP")

i=0
while(i<n):
    z=n-i+1
    while(z>0):
        print(end=" ")
        z-=1
    y=0
    while(y<i+1):
        print(factorial(i) // (factorial(y) * factorial(i - y)), end=" ")
        y+=1
    i+=1
    print()
print("\n\n")

print("USING RECURSSIONS")

def pascal_triangle(n,originalength=n):
    if n == 0:
        return
    pascal_triangle(n-1,originalength)
    #printing the spaces
    print('  '*(originalength-n), end='')

    #first number is always 1
    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')
        
        #using Binomial Coefficient
        start = start * (n - i) // i
    print()
pascal_triangle(n)
print("\n")



#Question 3

int1, int2 = map(int,input("Enter 2 numbers: ").split())
Quotient = int1 // int2
Remainder = int1 % int2

#part <a>
print("a. Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))

#part <b>
if (Quotient == 0):
    print("b. The quotient is zero")
if (Remainder == 0):
    print("b. The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("b. All the values are non zero")

#part <c>
partClist = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(partClist)):
    if partClist[i] > 4:
        result.append(partClist[i])
print(f"c. Filtered out numbers that are greater than 4 are : {result}")

#part <d>
setresult = set(result)
print("d. Set:",setresult)

#part <e>
immutableSet = frozenset(setresult) #frozen Set is used to make the set immutable
print("e. Immutable set:",immutableSet)

#part <f>
print("f. Hash value of the max value from the above set:", hash(max(immutableSet)))
print("\n")


#Question 4

class Student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
    
    def __del__(self):
        print("Object destroyed")


student1 = Student("Manik Bansal", 21103108)
print("Object created")

print(f"The name of the student is {student1.name} and SID is {student1.roll_no}.")

del student1
print("\n")


#Question 5

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
#creating employee records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#part <a> updating salary
employee1.salary = 70000
print(f"a. The updated salary of {employee1.name} is {employee1.salary} ")
#part <b> deleting a record
print("b. Record of Viren deleted", end='')
del employee3
print("\n")



#Question 6

word =input("Enter the word: ")
word=word.lower()


test_word = input("Enter a new meaningful word using the exact same letters to test your friendship: ")
test_word=test_word.lower()

def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

def userinput():
    if count_in_dict(word) != count_in_dict(test_word):
        print("The letters aren't exact, friendship is fake")
        return
    ans = input("Does the word makes sense?(y/Y or n/N ) ")

    if ans == 'y' or ans=='Y':
        print("The friends pass the friendship test")
    elif ans == 'n' or ans=='N':
        print("The word doesn't have a meaning, friendship is fake")
    else:
        print("Invalid input, try again with y/Y or n/N ")
        userinput()
userinput()