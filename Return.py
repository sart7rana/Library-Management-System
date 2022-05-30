'''importing date and time'''
import datetime

'''ccreating function'''
'''To convert the text file imtp 1D list'''
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
    

'''for displaying available books after returning'''
def addBooks(dlist, quantity, bookID):
    '''Appending value'''
    quantity1 = dlist[4]
    quantity2 = dlist[9]
    quantity3 = dlist[14]
    quantity4 = dlist[19]
    quantity5 = dlist[24]
    quantity6 = dlist[29]
    file = open("Books.txt", "w") #Open the books.txt file and write the following
    if bookID == 1:
        quantity1 = int(dlist[4])+1
        file.write("1,JK Rowling,Harry Potter,$5,"+str(quantity1)+"\n2,James Clear,Atomic Habits,$15,"+quantity2+"\n3,Peter Thiel,Zero to One,$20,"+quantity3 +
                   "\n4,Robert Iger,The ride of a lifetime,$15,"+quantity4+"\n5,Cal Newport,Deep Work,$10,"+quantity5+"\n6,Jim Collins,Good to Great,$10,"+quantity6+"")
    elif bookID == 2:
        quantity2 = int(dlist[9])+1
        file.write("1,JK Rowling,Harry Potter,$5,"+quantity1+"\n2,James Clear,Atomic Habits,$15,"+str(quantity2)+ "\n3,Peter Thiel,Zero to One,$20,"+quantity3 +
                   "\n4,Robert Iger,The ride of a lifetime,$15,"+quantity4+"\n5,Cal Newport,Deep Work,$10,"+quantity5+"\n6,Jim Collins,Good to Great,$10,"+quantity6+"")
    elif bookID == 3:
        quantity3 = int(dlist[14])+1
        file.write("1,JK Rowling,Harry Potter,$5,"+quantity1+"\n2,James Clear,Atomic Habits,$15,"+quantity2+"\n3,Peter Thiel,Zero to One,$20,"+str(quantity3) +
                   "\n4,Robert Iger,The ride of a lifetime,$15,"+quantity4+"\n5,Cal Newport,Deep Work,$10,"+quantity5+"\n6,Jim Collins,Good to Great,$10,"+quantity6+"")
    elif bookID == 4:
        quantity4 = int(dlist[19])+1
        file.write("1,JK Rowling,Harry Potter,$5,"+quantity1+"\n2,James Clear,Atomic Habits,$15,"+quantity2+"\n3,Peter Thiel,Zero to One,$20,"+quantity3 +
                   "\n4,Robert Iger,The ride of a lifetime,$15,"+str(quantity4)+"\n5,Cal Newport,Deep Work,$10,"+quantity5+"\n6,Jim Collins,Good to Great,$10,"+quantity6+"")
    elif bookID == 5:
        quantity5 = int(dlist[24])+1
        file.write("1,JK Rowling,Harry Potter,$5,"+quantity1+"\n2,James Clear,Atomic Habits,$15,"+quantity2+"\n3,Peter Thiel,Zero to One,$20,"+quantity3 +
                   "\n4,Robert Iger,The ride of a lifetime,$15,"+quantity4+"\n5,Cal Newport,Deep Work,$10,"+str(quantity5)+"\n6,Jim Collins,Good to Great,$10,"+quantity6+"")
    elif bookID == 6:
        quantity6 = int(dlist[29])+1
        file.write("1,JK Rowling,Harry Potter,$5,"+quantity1+"\n2,James Clear,Atomic Habits,$15,"+quantity2+"\n3,Peter Thiel,Zero to One,$20,"+quantity3 +
                   "\n4,Robert Iger,The ride of a lifetime,$15,"+quantity4+"\n5,Cal Newport,Deep Work,$10,"+quantity5+"\n6,Jim Collins,Good to Great,$10,"+str(quantity6)+"")
    file.close()
    RemainingQuantity = quantity + 1
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

'''for displaying returnBook'''
def returnBook(dlist, name, display):
    fg = True
    valid = True
    n_valid = True
    while valid == True:
        '''Exception Handling'''
        try:
            bookID = int(input("Enter BookID: "))
            break
        except:
            print("The bookID should be an integer between 1-6")
    while valid == True:
        '''Exception Handling'''
        try:
            noOfDays = int(input("Enter for how many days you have borrowed the book: "))
            break
        except:
            print("Enter an integer")
    bookFine(noOfDays, name, dlist, bookID)
    while fg == True:
        if bookID == 1:
            quantity = int(dlist[4])
            addBooks(dlist, quantity, bookID)
            display(dlist)
            break
        elif bookID == 2:
            quantity = int(dlist[9])
            addBooks(dlist, quantity, bookID)
            display(dlist)
            break
        elif bookID == 3:
            quantity = int(dlist[14])
            addBooks(dlist, quantity, bookID)
            display(dlist)
            break
        elif bookID == 4:
            quantity = int(dlist[19])
            addBooks(dlist, quantity, bookID)
            display(dlist)
            break
        elif bookID == 5:
            quantity = int(dlist[24])
            addBooks(dlist, quantity, bookID)
            display(dlist)
            break
        elif bookID == 6:
            quantity = int(dlist[29])
            addBooks(dlist, quantity, bookID)
            display(dlist)
            break
        else:
            print("Error")
            break

'''for Number of books'''
def N_book(dlist, bookID):
    book_Name = "" #initialize book_Name to empty string
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


'''function for bookFine'''
def bookFine(noOfDays, name, dlist, bookID):
    if int(noOfDays) > 10:
        fineBill(name, dlist, bookID, noOfDays) #when noOfDays > 10, display fineBill
    else:
        noFineBill(name, dlist, bookID) #when noOfDays < 10, display noFineBill

'''to develop return bill with a unique name when there is fine'''
def fineBill(name, dlist, bookID, noOfDays):
    nameofbook = N_book(dlist, bookID)
    fineAmount = (int(noOfDays) - 10) * 1
    dateNtime = datetime.datetime.now()
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    microsecond = str(datetime.datetime.now().microsecond)
    file = open("Return_"+name+".txt", "w")
    file.write("Name of the Customer: "+name+"\n")
    file.write("The Date and Time when returned is: "+str(dateNtime)+"\n")
    file.write("The name of the returned book is: "+nameofbook+"\n")
    file.write("The Fine amount is: $"+str(fineAmount)+"\n")
    file.close()
    print("You have charged with a fine of 1$ per day.")

'''to develop return bill with a unique name when there is no fine'''
def noFineBill(name, dlist, bookID):
    nameofbook = N_book(dlist, bookID)
    dateNtime = datetime.datetime.now()
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    microsecond = str(datetime.datetime.now().microsecond)
    file = open("Return_"+name+".txt", "w")
    file.write("Name of the Customer: "+name+"\n")
    file.write("The Date and Time when returned is: "+str(dateNtime)+"\n")
    file.write("The name of the returned book is: "+nameofbook+"\n")
    file.write("You returned the book on time, so there is no fine.")
    file.close()
