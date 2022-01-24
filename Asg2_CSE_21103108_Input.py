#Question 1 part a

inp_string = 'Python is a case sensitive language'

print('Length of the string is', len(inp_string))

#Question 1 part b

inp_string = 'Python is a case sensitive language' [::-1]

print('Reversed string is', inp_string)

#Question 1 part c

inp_string = 'Python is a case sensitive language'

new_string1 = inp_string[10:26]

#Question 1 part d

new_string2  = inp_string.replace('a case sensitive', 'object oriented')


#Question 1 part e

index = inp_string.find('a')

print("Index of 'a' is ", index)

#Question 1 part f

new_string3 = inp_string.replace(' ','')

print('The string after removing whitespaces is', new_string3)

#Question 2

name = 'Manik Bansal'
sid = 21103108
dep_name = 'Computer Science and Engineering'
cgpa = 9.9

print('Hey, %s'%name,'Here!')
print('My SID is %d'%sid)
print('I am from %s'%dep_name,'department and my CGPA is %.1f'%cgpa)

#Question 3

a = 56
b = 10

print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b<<2)
print(a>>2)
print(b>>4)

#Question 4

print('Please enter three numbers')

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if (a>b):
    if(a>c):
        print('The greatest number is a =',a)
    else:
        print('The greatest number is c =',c)

else:
    if(b>c):
        print('The greatest number is b =',b)
    else:
        print('The greatest number is c =',c)            

#Question 5

string = str(input('Please enter the string here \n'))

if 'name' in string:    
    print('Yes')
else:                 #Since, python is a case sensitive language, output for anything other 'name',
    print('No')       #for eg.Name,NAME,NaMe etc. will give No as output

#Question 6

print('Please enter three sides of a triangle')

side1 = int(input('Side 1 = '))
side2 = int(input('Side 2 = '))
side3 = int(input('Side 3 = '))

if (side1>side2+side3 or side2>side1+side3 or side3>side1+side2):
    print('No')

else:
    print('Yes')    

