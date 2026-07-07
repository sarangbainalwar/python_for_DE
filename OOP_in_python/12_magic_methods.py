# magic methods Dunder methods (double underscore), they are automatically called by many of pythons buil in operations they allow devs to define or customize the behaviour of objects

class book:
    def __init__(self,title,author,num_pages):
        self.title=title
        self.author=author
        self.num_pages=num_pages
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self,other):
        return self.title == other.title and self.author==other.author
    
    def __lt__(self,other):
        return self.num_pages < other.num_pages
    
    def __add__(self,other):
        return f"{(self.num_pages + other.num_pages)}"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        if key=="author":
            return self.author
    
book1=book("the hobbit","JJR",310)
book4=book("the hobbit","JJR",3100)
book2=book("LOTR","Snow",3100)
book3=book("Lanister","Hodor",1000)

print(book1)
print(book1==book4)
print(book3)
print(book2<book3)
print(book1+book4)
print("Lanister" in book3)
print(book1['author'])