#Question 1

from tkinter import*

def find_gst():
    org_cost=int(org_entry.get())
    net_cost=int(net_entry.get())
    gst_rate=((net_cost - org_cost) * 100) / org_cost
    print("the original cost is: ",org_cost)
    print("the net cost is : ",net_cost)
    print("the gst rate is : ",gst_rate)
    gst_entry.insert(12, str(gst_rate) + "%")

#function for clearing all the enteries
def clear_all():
    org_entry.delete(0,END)
    net_entry.delete(0,END)
    gst_entry.delete(0,END)

#driver code
win=Tk()
win.configure(background='silver')
win.geometry('500x500')
win.title("GST RATE FINDER")
lbl_1=Label(win,text='ENTER ORIGINAL PRICE',relief='raised',padx=3,pady=3,bd=3,font=('times new roman',12,'bold'))
lbl_1.grid(row=1,column=1,padx=10,pady=10)
lbl_2=Label(win,text="ENTER NET PRICE",relief='raised',padx=3,pady=3,bd=3,font=('times new roman',12,'bold'))
lbl_2.grid(row=2,column=1,padx=10,pady=10)
but_1=Button(win,text="Calculate",padx=3,pady=3,bg='light grey',relief='sunken',bd=3,font=('times new roman',12),command=find_gst,activebackground='red')
but_1.grid(row=3,column=2,padx=10,pady=10)
lbl_3=Label(win,text="GST RATE IS",relief='raised',padx=3,pady=3,bd=3,font=('times new roman',12,'bold'))
lbl_3.grid(row=4,column=1,padx=10,pady=10)
but_2=Button(win,text="Clear",padx=3,pady=3,bg='light grey',relief='sunken',bd=3,font=('times new roman',12),command=clear_all,activebackground='red')
but_2.grid(row=5,column=2,padx=10,pady=10)
org_entry=Entry(win)
org_entry.grid(row=1,column=2,padx=10,pady=10)
net_entry=Entry(win)
net_entry.grid(row=2,column=2,padx=10,pady=10)
gst_entry=Entry(win)
gst_entry.grid(row=4,column=2,padx=10,pady=10)
win.mainloop()


#Question 2

from tkinter import *
import calendar
# Function for showing the calendar of the given year
def Cal() :

	# Create a GUI window
	root = Tk()
	root.configure(background = "black")
	root.title("CALENDAR")
	root.geometry("650x650")

	
	year = int(year_field.get())
	cal_content = calendar.calendar(year)

	cal_year = Label(root, text = cal_content, font = "Consolas 10 bold")
	cal_year.grid(row = 5, column = 1, padx = 30, ipadx = 30, ipady = 30)
	cal_year.pack(side="Middle")
	root.mainloop()

	
# Driver Code
if __name__ == "__main__" :

	
	gui = Tk()
	gui.config(background = "turquoise")
	gui.title("CALENDAR")
	gui.geometry("550x400")

	cal = Label(gui, text = "CALENDAR", bg = "Purple",fg = 'Yellow', font = ("calibre", 40, 'bold'),padx=5,pady=5)
    
	year = Label(gui, text = "ENTER YEAR", bg = "Purple", fg = 'Yellow',font = ("calibre", 28, 'bold'),padx=5,pady=5)
	year_field = Entry(gui)

	Show = Button(gui, text = "Show Calendar", fg = "Black", bg = 'silver', command = Cal)

	Exit = Button(gui, text = "Exit", fg = "Black", bg = 'silver', command = exit)

	cal.grid(row = 1, column = 1,padx=140,pady=10)

	year.grid(row = 2, column = 1,padx=140,pady=0)

	year_field.grid(row = 3, column = 1,pady=5)

	Show.grid(row = 4, column = 1)

	Exit.grid(row = 6, column = 1)
	
	gui.mainloop()


#Question 3

from tkinter import *

expression = ""

def press(num):
	
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():
	try:

		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""

	except:

		equation.set(" error ")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")



if __name__ == "__main__":
	
	root = Tk()
	root.configure(background="silver")
	root.title("Simple Calculator")
	root.geometry("270x150")
	equation = StringVar()
	
	expression_field = Entry(root, textvariable=equation)
	expression_field.grid(columnspan=4, ipadx=70)

	button1 = Button(root, text=' 1 ', fg='black',command=lambda: press(1), height=1, width=7)
	button1.grid(row=2, column=0)

	button2 = Button(root, text=' 2 ', fg='black',command=lambda: press(2), height=1, width=7)
	button2.grid(row=2, column=1)

	button3 = Button(root, text=' 3 ', fg='black',command=lambda: press(3), height=1, width=7)
	button3.grid(row=2, column=2)

	button4 = Button(root, text=' 4 ', fg='black',command=lambda: press(4), height=1, width=7)
	button4.grid(row=3, column=0)

	button5 = Button(root, text=' 5 ', fg='black',command=lambda: press(5), height=1, width=7)
	button5.grid(row=3, column=1)

	button6 = Button(root, text=' 6 ', fg='black',command=lambda: press(6), height=1, width=7)
	button6.grid(row=3, column=2)

	button7 = Button(root, text=' 7 ', fg='black',command=lambda: press(7), height=1, width=7)
	button7.grid(row=4, column=0)

	button8 = Button(root, text=' 8 ', fg='black',command=lambda: press(8), height=1, width=7)
	button8.grid(row=4, column=1)

	button9 = Button(root, text=' 9 ', fg='black',command=lambda: press(9), height=1, width=7)
	button9.grid(row=4, column=2)

	button0 = Button(root, text=' 0 ', fg='black',command=lambda: press(0), height=1, width=7)
	button0.grid(row=5, column=0)

	plus = Button(root, text=' + ', fg='black',command=lambda: press("+"), height=1, width=7)
	plus.grid(row=2, column=3)

	minus = Button(root, text=' - ', fg='black',command=lambda: press("-"), height=1, width=7)
	minus.grid(row=3, column=3)

	multiply = Button(root, text=' * ', fg='black',command=lambda: press("*"), height=1, width=7)
	multiply.grid(row=4, column=3)

	divide = Button(root, text=' / ', fg='black',command=lambda: press("/"), height=1, width=7)
	divide.grid(row=5, column=3)

	equal = Button(root, text=' = ', fg='black',command=equalpress, height=1, width=7)
	equal.grid(row=5, column=2)

	clear = Button(root, text='Clear', fg='black',command=clear, height=1, width=7)
	clear.grid(row=5, column='1')

	Decimal= Button(root, text='.', fg='black',command=lambda: press('.'), height=1, width=7)
	Decimal.grid(row=6, column=0)
	
	root.mainloop()


#Question 4

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


n = int(input('Please enter the number of elements in the list: '))
li = list(map(int, input().strip().split()))
quickSort(li, 0, n - 1)
print("Sorted array is: ", li)
print("\n\n")


#Question 5

n = int(input('Please enter the number of elements in the list: '))
li = list(map(int, input('Please enter the elements: ').strip().split()))
# Part 1
li.sort()
print("Sorted array is:", li)

# Part 2
flag = False
low = 0
high = n
count = 0
ind = -1
to_find = int(input('Please enter the number you are looking for: '))
while(low < high):
    mid = low + (high - low) // 2
    if(int(li[mid]) == to_find):
        flag = True
        ind = mid
        print("Value is at index:", mid)
        break
    elif li[mid] > to_find:
        high = mid - 1
    else:
        low = mid + 1
if flag == False:
    print("Error")

# Part 3
if(ind == -1):
    print("No element found\n")
else:
    i = mid
    j = mid
    count = 0
    for k in range(0, max(i, n - j)):
        if(i >= 0 and li[i] == to_find):
            count += 1
            i -= 1
        if(j < n and li[j] == to_find):
            count += 1
            j += 1
    print("Total number of occurances is:", count - 1)



