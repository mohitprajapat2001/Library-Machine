from sql_query import *
def ShowBook():
    return db_query("SELECT Name,Author FROM books WHERE istrue = 'true';")
def ShowLendbook(user):
    return db_query(f"SELECT * FROM guest WHERE user = '{user}';")
def loopShow(temp):
    for i in temp:
        print(i)

class LibraryMain:
    def __init__(self, user, ):
        self.user = user
        print(user)
    def display_Books(self):
        temp = ShowBook()
        loopShow(temp)
        mydb.commit()
    def add_Book(self, bookname, author):
        db_query(f"insert into books values('{bookname}','{author}','true');")
        mydb.commit()
    def lend_book(self, booklend):
        db_query(f"INSERT INTO guest VALUES('{self.user}','{booklend}','Lended');")
        db_query(f"UPDATE books SET istrue ='false' WHERE Name = '{booklend}';")
        temp = ShowLendbook(self.user)
        loopShow(temp)
        mydb.commit()
    def userreturn(self):
        temp = db_query(f"SELECT * FROM guest WHERE user = '{self.user}'")
        loopShow(temp)
        bookreturn = input("\nWhich Book to Return ")
        db_query(f"UPDATE guest SET status = 'Returned' WHERE book = '{bookreturn}';")
        db_query(f"UPDATE books SET istrue ='true' WHERE Name = '{bookreturn}';")
        print(f"{self.user} Returned {bookreturn}")
        mydb.commit()

def main():
    library_obj = LibraryMain(user)
    option = int(input(f"Welcome {user} Choose Option"
                       "\n1. Available Book"
                       "\n2. Add Book"
                       "\n3. Lend Book"
                       "\n4. Return Book: "))
    if option == 1:
        library_obj.display_Books()
    elif option == 2:
        bookname = input("\nEnter Book Name :")
        author = input("\nEnter Author Name :")
        library_obj.add_Book(bookname, author)
    elif option == 3:
        library_obj.display_Books()
        booklend = input("\nEnter Book For Lend :")
        library_obj.lend_book(booklend)
    elif option == 4:
        library_obj.userreturn()
        print("Available books:")
        library_obj.display_Books()

user = input("Welcome User: ")
while True:
    main()
    mydb.commit()
    tmp = input("Press Enter to Explore More Otherwise Enter 'EXIT' ;-)")
    if tmp == "EXIT" or tmp == "exit":
        break