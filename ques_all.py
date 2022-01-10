#Question 1

a = int(input('Enter the value of a:'))
b = int(input('Enter the value of b:'))
c = int(input('Enter the value of c:'))

d = int((a+b+c)/3)

print('The average of the given numbers = ', d)

#Question 2

a = float(input('Please enter your gross income to the nearest penny '))
b = int(input('Please enter the number of dependents '))

taxable_income = float(a-10000-(3000*b))

tax = float(taxable_income*0.2)
print('Total Payable Tax = ', tax)

#Question 3

sid = input('Please enter your Student ID: ')
name = input('Please enter your name: ')
gender = input('Gender : M/F/U ')
branch = input('Please enter your branch name: ')
cgpa = input('Please enter your cgpa ')

L = [sid, name, gender, branch, cgpa]

print(L)

#Question 4 

std1 = int(input('Student 1: '))
std2 = int(input('Student 2: '))
std3 = int(input('Student 3: '))
std4 = int(input('Student 4: '))
std5 = int(input('Student 5: '))

L = [std1, std2, std3, std4, std5]

print('List of marks of the students: ',L)

L.sort()

print('List of marks of the students in the ascending order: ',L)

L.sort(reverse = True)

print('List of marks of the students in the descenind order: ',L)

#Question 5(a)

list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

del list[3]

print(list)

#Question 5(b)

list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

list[3:5] = ['purple']

print(list)


