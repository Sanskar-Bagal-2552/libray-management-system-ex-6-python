class libray:
    def __init__(self):
        self.notebooks=0
        self.books=[]
    def addbooks(self,books):
        self.books.append(books)
        self.nobooks=len(self.books)
    def showinfo(self):
        print(f'the libray has {self.nobooks} the books are ')
        for books in self.books:
            print(books)
l1=libray()
l1.addbooks("atomic habits")
l1.addbooks("The 7 Habits of Highly Effective People")
l1.addbooks("Think and Grow Rich")
l1.addbooks("The Power of Now")
l1.addbooks("Can't Hurt Me")
l1.showinfo()
