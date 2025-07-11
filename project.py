class Book:
    def __init__(self,name,userID,book,bookID,price):
        self.name = name
        self.userID = userID
        self.book = book
        self.bookID = bookID
        self.price = price
        self.books = [[book, bookID,price]]
        self.count = 1

    def get_userDB(self):
        return [self.name, self.userID, self.books, self.count]
    

    def show_users(self):
        listed = self.get_userDB()
        print(listed)


class Library(Book):
    def __init__(self):
        self.libraryDB = []
        self.dic = {
            'HINDI': {
                'bookQty' : 5,
                'bookID' : 11
            },
            'ENGLISH':{
                'bookQty' : 5,
                'bookID' : 12
            },"MATHS":{
                'bookQty' : 5,
                'bookID' : 13
            },
              "CA":{
                'bookQty' : 5,
                'bookID' : 14
              }, 
              "COMPUTER":{
                'bookQty' : 5,
                'bookID' : 15
              },
              "GK" : {
                'bookQty' : 5,
                'bookID' : 16
              }}

    def all_books(self):
        for i in self.dic:
            print(f"{i} : {self.dic[i]}")

    def find_user(self,userID):
        for i in self.libraryDB:
            if i.userID == userID:
                return i
        return None

    def add_user(self,name,userID,book,bookID,price):
        find = self.find_user(userID)
        if find:
            if self.dic[book]["bookQty"] != 0 and self.dic[book]['bookID'] == bookID:
                self.dic[book]["bookQty"] = self.dic[book]["bookQty"]-1
                print(self.dic[book]["bookQty"])
                print("User Add Sucesfully")
                find.count +=1
                find.books.append([book,bookID,price])

            else:
                print("This book is not availableeee")

        else:
            obj = Book(name,userID,book,bookID,price)
            value = self.dic.get(book)
            if value and self.dic[book]["bookQty"] != 0 and self.dic[book]['bookID'] == bookID:
                self.dic[book]['bookQty'] = self.dic[book]['bookQty']-1
                print("User Add Sucesfully")
                self.libraryDB.append(obj)
            else:
                print("This book is not available")

    def deposite_book(self,userID,bookID,book):
        find = self.find_user(userID)
        if find:
            for i in find.books:
                if i[1] == bookID and i[0] == book:
                    ind = find.books.index(i)
                    find.books.pop(ind)
                    self.dic[book]['bookQty'] += 1


                    length = len(find.books)
                    if length == 0:
                        # print(length)
                        self.libraryDB.remove(find)

                    print("Book Submit Sucessfully ")
                else:
                    print("Invalid Book ID or Book Name")

        else:
            print("User Not Found")    


    def show_all_user(self):
        for i in self.libraryDB:
            i.show_users()

obj1= Library()

while True:
    print("\n Library Menu ")
    print("Press 1 for Show All Books ")
    print("Press 2 for Issue A Book")
    print("Press 3 for Return A Book")
    print("Press 4 for Show All Users")
    print(" Press 5 for Exit")
    ch = input("Enter Your Choice ")

    if ch == "1":
        obj1.all_books()

    elif ch == "2":
        print("Please Fill All the Details")
        try:

            name = input("Enter Your Name ")
            id = int(input("Enter your Aadhar No "))
            book = input("Enter book name in CAPS ")
            bookId = int(input("Enter book ID "))
            bookRs = int(input("Enter book Price "))
            obj1.add_user(name, id, book.upper(), bookId,bookRs)
        except ValueError:
            print("Invalid Input Please Enter correct Details")

    elif ch == "3":
        try:
            id = int(input("Enter your Aadhar No "))
            bookId = int(input("Enter book ID "))
            book = input("Enter book Name ")
            obj1.deposite_book(id,bookId, book.upper())
        except ValueError:
            print("Please Enter Correct Input")

    elif ch == "4":
        obj1.show_all_user()

    elif ch == "5":
        break

    else:
        print("Invalid Choice. Try Again")