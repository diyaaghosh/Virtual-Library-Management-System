class library:
    def __init__(self,books_list):
        
        self.books_list=books_list
    def add_book(self):
          self.addbook=""
    def info(self):
        self.show_number=len(self.books_list)
        
        print("Books Number : ",self.show_number)
        
        print("Books List : ",end="\n")
        cnt=0
        for i in self.books_list:
            cnt+=1
            print(cnt,". ",i)
        
       
    def onlynumber(self):
           self.show_number=len(self.books_list)  
           return self.show_number      
           
print(":::::::: Welcome to Virtual Library ::::::::::\n")   
books=["Harry Poter","Sherlok Homes","The Eyes Have It","Comedy of Errors","Macbeth"]
number=len(books)
a=library(books)     
initial_no=a.onlynumber()
print("Press 1 : Show Current Status of the Library \nPress 2 : Show Current No of Books \nPress 3 : Add Some New Books and Show the Final Number and Status of Books Also Check if There Is Any Mismatch\n")
choice=int(input("Enter Any Button (1-3) : "))

if(choice==1):
    print(a.info())
    
elif(choice==2):
   print("Current Number of Books : ",a.onlynumber())
elif(choice==3):
    a.info()    
   
    
    moves=int(input("Enter Number of Books You want to add in the Library : "))
    i=0

    while(i<moves):  
      a.add_book=input("Enter Name of New Added Book : ")
      books.append(a.add_book)
      i+=1
      initial_no+=1
  
 
    print("Final Status : ",end="\n")
    a.info()
    print("As Final Number of Books is also  ", initial_no)
    final_no=len(books)
    if(initial_no==final_no):
       print("Therefore , Number of the Final Books is verified ")
    else :
       rest=abs(initial_no-final_no)
       print("Some Mismatch occured w.r.t ",rest,"number of books")         
else:
    print("You Pressed Wrong Button")      
