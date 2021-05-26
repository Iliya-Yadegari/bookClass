class Book:
    def __init__(self,ISBN_13,BookTitle,author_s,publisher,publishedYear,subject,bookID):
        self.ISBN_13 = ISBN_13
        self.BookTitle = BookTitle
        self.author_s = author_s
        self.publisher = publisher
        self.publishedYear = publishedYear
        self.subject = subject
        self.bookID = bookID
        
    def info(self):
        
        print(f'The ISBN-13 is {self.ISBN_13}, the book title is {self.BookTitle}, the author(s) is/are {self.author_s}, the publisher is {self.publisher}, the subject is {self.subject}, the book ID is {self.bookID}.')
      

harryPotter = Book('ISBN-13','Harry Potter',['J.K Rowling'],'Puffin','2000','Magic and fiction','34259')

harryPotter.info()