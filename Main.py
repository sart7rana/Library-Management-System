import Borrow #importing Borrow.py 
import Return #importing Return.py

'''Initializing dlist in borrow 1D list'''
dlist = Borrow.OneDlsit()
'''CallingDisplay function'''
Borrow.display(dlist)

'''Main Function'''
bookName = "" #initializing bookName to empty string
totalCost = 0 #initializing totalCost to 0
inputNumber = 0 #initializing inoutNumber to 0
valid = True
while inputNumber != 3: #when inputNumber is not equal to 3
    print("Enter 1 to borrow a book")
    print("Enter 2 to return a book")
    print("Enter 3 to exit")
    while valid == True:
        '''Exception Handling'''
        try:
            inputNumber = int(input("Enter number: 1,2,3 : "))
            break
        except:
            print("The given value is not an integer")
            break
    if inputNumber == 1: #when inoutNumber equals to 1
        name = input("Enter the costumer name: ")
        Cost, bookName = Borrow.borrowContinuation(dlist, Borrow.display, totalCost, bookName, name)
        Borrow.Bill(Cost, bookName, name)

    elif inputNumber == 2: #when inoutNumber equals to 2
        name = input("Enter the costumer name: ")
        Return.returnBook(dlist, name, Return.display)
        
    elif inputNumber == 3: #when inoutNumber equals to 3
        print("You have exit the program")
        
    else:
        print("You can only enter values from 1-3.")
