class Book:
    def __init__(self,bName,bAuthor,bPublishYear):
        self.bName = bName
        self.bAuthor = bAuthor
        self.bPublishYear = bPublishYear

    def __len__(self):
        return len(self.bName)
    
    def __str__(self):
        return f"The book '{self.bName}' was written by '{self.bAuthor}' and was published in the year {self.bPublishYear}"
    

book1 = Book("Harry Potter","J K Rowling", 2002)
print(f"Length of the book title is {len(book1)}")
print(book1)
        