class Book:
    def __init__(self,title,author,list_of_reviews):
        self.title=title
        self.author=author
        self.list_of_reviews=list_of_reviews
    
    def add_review(self,review):
        self.list_of_reviews.append(review)
        print(f"these are updated list of review:{self.list_of_reviews}")
    def count_rev(self):
        count=0
        for i in self.list_of_reviews:
            count+=1
        print(f"Number of review = {count}")
    def display_review(self):
        print("Reviews are :\n")
        for i in self.list_of_reviews:
            print(i)

b1=Book("Python","MJ",["hello","Verry good"])
b1.add_review("Awesome")
b1.count_rev()
b1.display_review()