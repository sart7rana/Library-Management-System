'''importing date and time'''
import datetime

'''creating functions'''
'''To convert the text file into 1D list'''
def OneDlsit():
    file = open("Books.txt", "r")
    double_dlist = []
    single_dlist = []
    for line in file:
        line = line.replace("\n", "")
        double_dlist.append(line.split(","))
    for i in range(len(double_dlist)):
        for j in range(len(double_dlist[i])):
            single_dlist.append(double_dlist[i][j])
    return single_dlist

'''To display values of dictionary in a table format'''
def display(dlist):
    '''Column name'''
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nBook ID          Author           Book Name                 Price          Quantity\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    '''All the data of the list in the table'''
    print("  ", dlist[0], "         ", dlist[1], "      ", dlist[2], "              ", dlist[3], "             ", dlist[4])
    print("  ", dlist[5], "         ", dlist[6], "     ", dlist[7], "             ", dlist[8], "            ", dlist[9])
    print("  ", dlist[10], "         ", dlist[11], "     ", dlist[12], "               ", dlist[13], "            ", dlist[14])
    print("  ", dlist[15], "         ", dlist[16], "     ", dlist[17], "    ", dlist[18], "            ", dlist[19])
    print("  ", dlist[20], "         ", dlist[21], "     ", dlist[22], "                 ", dlist[23], "            ", dlist[24])
    print("  ", dlist[25], "         ", dlist[26], "     ", dlist[27], "             ", dlist[28], "            ", dlist[29])
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

'''for displaying available books'''
def availableBooks(dlist, quantity, bookID):
    '''Appending value'''
    quantity1 = dlist[4] 
    quantity2 = dlist[9]
    quantity3 = dlist[14]
    quantity4 = dlist[19]
    quantity5 = dlist[24]
    quantity6 = dlist[29]
    file = open("Books.txt", "w") #Open the books.txt file and write the following
    if bookID == 1:
        quantity1 = int(dlist[4])-1
        file.write("1,JK Rowling,Harry Potter,$5,"+str(quantity1)+"\n2,James Clear,Atomic Habits,$15,"+quantity2+"\n3,Peter Thiel,Zero to One,$20,"+quantity3 +
                   "\n4,Robert Iger,The ride of a lifetime,$15,"+quantity4+"\n5,Cal Newport,Deep Work,$10,"+quantity5+"\n6,Jim Collins,Good to Great,$10,"+quantity6+"")
    elif bookID == 2:
        quantity2 = int(dlist[9])-1
        file.write("1,JK Rowling,Harry Potter,$5,"+quantity1+"\n2,James Clear,Atomic Habits,$15,"+str(quantity2)+ "\n3,Peter Thiel,Zero to One,$20,"+quantity3 +
                   "\n4,Robert Iger,The ride of a lifetime,$15,"+quantity4+"\n5,Cal Newport,Deep Work,$10,"+quantity5+"\n6,Jim Collins,Good to Great,$10,"+quantity6+"")
    elif bookID == 3:
        quantity3 = int(dlist[14])-1
        file.write("1,JK Rowling,Harry Potter,$5,"+quantity1+"\n2,James Clear,Atomic Habits,$15,"+quantity2+"\n3,Peter Thiel,Zero to One,$20,"+str(quantity3) +
                   "\n4,Robert Iger,The ride of a lifetime,$15,"+quantity4+"\n5,Cal Newport,Deep Work,$10,"+quantity5+"\n6,Jim Collins,Good to Great,$10,"+quantity6+"")
    elif bookID == 4:
        quantity4 = int(dlist[19])-1
        file.write("1,JK Rowling,Harry Potter,$5,"+quantity1+"\n2,James Clear,Atomic Habits,$15,"+quantity2+"\n3,Peter Thiel,Zero to One,$20,"+quantity3 +
                   "\n4,Robert Iger,The ride of a lifetime,$15,"+str(quantity4)+"\n5,Cal Newport,Deep Work,$10,"+quantity5+"\n6,Jim Collins,Good to Great,$10,"+quantity6+"")
    elif bookID == 5:
        quantity5 = int(dlist[24])-1
        file.write("1,JK Rowling,Harry Potter,$5,"+quantity1+"\n2,James Clear,Atomic Habits,$15,"+quantity2+"\n3,Peter Thiel,Zero to One,$20,"+quantity3 +
                   "\n4,Robert Iger,The ride of a lifetime,$15,"+quantity4+"\n5,Cal Newport,Deep Work,$10,"+str(quantity5)+"\n6,Jim Collins,Good to Great,$10,"+quantity6+"")
    elif bookID == 6:
        quantity6 = int(dlist[29])-1
        file.write("1,JK Rowling,Harry Potter,$5,"+quantity1+"\n2,James Clear,Atomic Habits,$15,"+quantity2+"\n3,Peter Thiel,Zero to One,$20,"+quantity3 +
                   "\n4,Robert Iger,The ride of a lifetime,$15,"+quantity4+"\n5,Cal Newport,Deep Work,$10,"+quantity5+"\n6,Jim Collins,Good to Great,$10,"+str(quantity6)+"")
    file.close()
    RemainingQuantity = quantity - 1
    for i in range(len(dlist)):
        for j in range(len(dlist[i])):
            if bookID == 1:
                dlist[4] = str(RemainingQuantity)
            elif bookID == 2:
                dlist[9] = str(RemainingQuantity)
            elif bookID == 3:
                dlist[14] = str(RemainingQuantity)
            elif bookID == 4:
                dlist[19] = str(RemainingQuantity)
            elif bookID == 5:
                dlist[24] = str(RemainingQuantity)
            elif bookID == 6:
                dlist[29] = str(RemainingQuantity)

'''for displaying borrowBook'''
def borrowBook(dlist):
    bookPrice = 0 #initializing bookPrice to 0
    book_Name = "" #initializing book_Name to empty string
    fg = True
    valid = True
    n_valid = True
    while valid == True:
        '''Exception Handling'''
        try:
            bookID = int(input("Enter the BookID: "))
            break
        except:
            print("The bookID should be an integer between 1-6")
    while fg == True:
        if bookID == 1:
            quantity = int(dlist[4])
            if quantity > 0:
                displayAvailable()
                availableBooks(dlist, quantity, bookID)
                display(dlist)
                bookPrice = Price(dlist, bookID)
                book_Name = N_book(dlist, bookID)
                break
            else:
                while n_valid == True:
                    '''Exception Handling'''
                    try:
                        bookID = int(input("The book you want to borrow is out of stock, please enter another bookID if you want to borrow: "))
                        break
                    except:
                        print("ID should be a integer between 1-6")
        elif bookID == 2:
            quantity = int(dlist[9])
            if quantity > 0:
                displayAvailable()
                availableBooks(dlist, quantity, bookID)
                display(dlist)
                bookPrice = Price(dlist, bookID)
                book_Name = N_book(dlist, bookID)
                break
            else:
                while n_valid == True:
                    '''Exception Handling'''
                    try:
                        bookID = int(input("The book you want to borrow is out of stock, please enter another bookID if you want to borrow: "))
                        break
                    except:
                        print("ID should be a integer between 1-6")
        elif bookID == 3:
            quantity = int(dlist[14])
            if quantity > 0:
                displayAvailable()
                availableBooks(dlist, quantity, bookID)
                display(dlist)
                bookPrice = Price(dlist, bookID)
                book_Name = N_book(dlist, bookID)
                break
            else:
                while n_valid == True:
                    '''Exception Handling'''
                    try:
                        bookID = int(input("The book you want to borrow is out of stock, please enter another bookID if you want to borrow: "))
                        break
                    except:
                        print("ID should be a integer between 1-6") 
        elif bookID == 4:
            quantity = int(dlist[19])
            if quantity > 0:
                displayAvailable()
                availableBooks(dlist, quantity, bookID)
                display(dlist)
                bookPrice = Price(dlist, bookID)
                book_Name = N_book(dlist, bookID)
                break
            else:
                while n_valid == True:
                    '''Exception Handling'''
                    try:
                        bookID = int(input("The book you want to borrow is out of stock, please enter another bookID if you want to borrow: "))
                        break
                    except:
                        print("ID should be a integer between 1-6")
        elif bookID == 5:
            quantity = int(dlist[24])
            if quantity > 0:
                displayAvailable()
                availableBooks(dlist, quantity, bookID)
                display(dlist)
                bookPrice = Price(dlist, bookID)
                book_Name = N_book(dlist, bookID)
                break
            else:
                while n_valid == True:
                    '''Exception Handling'''
                    try:
                        bookID = int(input("The book you want to borrow is out of stock, please enter another bookID if you want to borrow: "))
                        break
                    except:
                        print("ID should be a integer between 1-6")
        elif bookID == 6:
            quantity = int(dlist[29])
            if quantity > 0:
                displayAvailable()
                availableBooks(dlist, quantity, bookID)
                display(dlist)
                bookPrice = Price(dlist, bookID)
                book_Name = N_book(dlist, bookID)
                break
            else:
                while n_valid == True:
                    '''Exception Handling'''
                    try:
                        bookID = int(input("The book you want to borrow is out of stock, please enter another bookID if you want to borrow: "))
                        break
                    except:
                        print("ID should be a integer between 1-6")
        else:   
            print("Error")
            break
    return bookPrice, book_Name

'''for seting price of the books of each book'''
def Price(dlist, bookID):
    if bookID == 1:
        price = dlist[3]
        price = price.replace("$", "")
    elif bookID == 2:
        price = dlist[8]
        price = price.replace("$", "")
    elif bookID == 3:
        price = dlist[13]
        price = price.replace("$", "")
    elif bookID == 4:
        price = dlist[18]
        price = price.replace("$", "")
    elif bookID == 5:
        price = dlist[23]
        price = price.replace("$", "")
    elif bookID == 6:
        price = dlist[28]
        price = price.replace("$", "")
    return price

'''for displaying Number of books'''
def N_book(dlist, bookID):
    book_Name = ""
    if bookID == 1:
        book_Name = dlist[2]
    elif bookID == 2:
        book_Name = dlist[7]
    elif bookID == 3:
        book_Name = dlist[12]
    elif bookID == 4:
        book_Name = dlist[17]
    elif bookID == 5:
        book_Name = dlist[22]
    elif bookID == 6:
        book_Name = dlist[27]
    return book_Name

'''when the user wants to continue borrow'''
def borrowContinuation(dlist, display, totalCost, bookName, name):
    fg = True
    book_Cost, book_Name = borrowBook(dlist) #call borrowBook
    totalCost += int(book_Cost) #set total cost to the total cost + book_Cost 
    bookName += book_Name+"\n" #set bookName to the bookName + book_Name
    while fg == True:
        Yes_No = input("If you want to borrow another book type 'Y' else type 'N':")
        if Yes_No == "Y":
            book_Cost, book_Name = borrowBook(dlist)
            totalCost += int(book_Cost)
            bookName += book_Name+"\n"
        elif Yes_No == "N":
            print("Thankyou for borrowing books from us.")
            break
        else:
            print("Invalid Input")
    return totalCost, bookName

'''to develop borrow bill with a unique name'''
def Bill(Cost, bookName, name):
    dateNtime = datetime.datetime.now()
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    microsecond = str(datetime.datetime.now().microsecond)
    file = open("Borrow_"+name+".txt", "w")
    file.write("Name of the Customer: "+name+"\n")
    file.write("The Date and Time when borrowed is: "+str(dateNtime)+"\n")
    file.write("The name of the borrowed book is: "+bookName+"\n")
    file.write("The total Cost is: $"+str(Cost)+"\n")
    file.close()

'''When the quantity of the book is left on the records'''
def displayAvailable():
    print("The book is available")
