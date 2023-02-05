class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print("You have issued "+bookName+". Please keep it safe and return it within 30 days.")
            self.books.remove(bookName)
        else:
            print("Sorry, this book has already been to someone else. Please wait until the book is returned.")

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":
   centralLibrary = Library(['Algorithms', 'CPP', 'Python', 'DSA', 'Basics of c language', 'Java'])
   student = Student()

   while True:
       welcomeMsg = '''=====Welcome To Central Library=====
       Please choose an option...
       1. List of all the books
       2. Request a book
       3. Return a book
       4. Exit the library
       '''

       print(welcomeMsg)

       a = int(input("Enter a choice: "))

       if a == 1:
           centralLibrary.displayAvailableBooks()
       elif a == 2:
           centralLibrary.borrowBook(student.requestBook())
       elif a == 3:
           centralLibrary.returnBook(student.returnBook())
       elif a == 4:
           print("Thanks for choosing Central Library! Have a great day ahead!")
           exit()
       else:
           print("Invalid choice")



