"""Creating objects in OOP to calculate shipping costs of a book"""


class book:

    """A class that calculates the shipping cost of a book
    
    Properties:
        self._book_name = Str, title of the book
        self._book_description = Str, description of the book
        self._book_price = Float, must be a number
        self._book_weight = Int, weight of the book in grams
    
    Method:
        Calculates the cost of shipping the book depending on it's weight

    """

    def __init__(self):
        """Initialises the properties"""
        self._book_name = "booktitle"
        self._book_description = "book desciption"
        self._book_price = 0
        self._book_weight = 0
    
    
    @property
    def bookName(self):
        """_book_name getter"""
        return self._book_name
    
    @bookName.setter
    def bookName (self, newVal):
         """_book_name setter
           
           Args:
               newVal = New name of book
        
           Raises:
               ValueError : If the name of book is not a string"""
         
         if isinstance(newVal, str):
            self._book_name = newVal
            print("Book Name Updated")
         else:
            raise ValueError("Please eneter a valid book name")
    
    
    @property
    def bookDescript (self):
        """"_book_description getter"""
        return self._book_description
    
    @bookDescript.setter
    def bookDescript(self, newVal):
        """_book_description setter
           
           Args:
               newVal = New description of book
        
           Raises:
               ValueError : If the description of book is not a string"""
        
        if isinstance(newVal, str):
            self._book_description = newVal
            print("Book Description Updated")
        else:
            raise ValueError("Please eneter a valid book description")
        
    
    @property
    def bookPrice (self):
        """_book_price getter"""
        return self._book_price
    
    @bookPrice.setter
    def bookPrice(self, newVal):
        """_book_price setter
           
           Args:
               newVal = New price of book
        
           Raises:
               ValueError : If the price of book is not a float
               ValueError : If the price of book is not more than 0"""
               
        
        if isinstance(newVal, float):
            if newVal > 0:
                self._book_price = newVal
                print("Book Price Updated")
            else:
                raise ValueError("Price must be more than 0")
        else:
            raise ValueError("Please eneter a valid price, must be a number")
        
    
    @property
    def bookWeight (self):
        """_book_weight_ getter"""
        return self._book_weight
    
    @bookWeight.setter
    def bookWeight(self, newVal):
        """_book_price setter
           
           Args:
               newVal = New price of book
        
           Raises:
               ValueError : If the weight of book is not a int
               ValueError : If the weight of book is not more than 0"""
        
        if isinstance(newVal, int):
            if newVal > 0:
                self._book_weight = newVal
                print("Book Weight Updated")
            else:
                raise ValueError("Weight must be more than 0")
        else:
            raise ValueError("Please eneter a valid weight, must be a number")
    

    def calculateShipping (self):
        """calculates shipping cost based on weight"""
        if self._book_weight <= 1000:
            self._shipping_price = 5
        elif self._book_weight < 5000:
            self._shipping_price = 8
        else:
            self._shipping_price = 10
        
        print(f"The Shipping price for: {self._book_name} is: {self._shipping_price}")
    
        




class bookType (book):
    """A child class that calculates the shipping cost of a book
    
    Properties:
        self._book_name = Str, title of the book
        self._book_description = Str, description of the book
        self._book_price = Float, must be a number
        self._book_weight = Int, weight of the book in grams
        self._book_ISBN = Int, ISBN of the book
        self._book_hardback = Boolean, determines if book is hardback or paperback
    
    Method:
        Calculates the cost of shipping the book depending on whether hardback or paperback

    """
    def __init__(self):
        """Initialises the properties"""
        super().__init__()
        self._book_ISBN = 12345678
        self._book_hardback = True

    @property
    def bookISBN (self):
        """_book_ISBN getter"""
        return self._book_ISBN
    
    @bookISBN.setter
    def bookISBN(self, newVal):
        """_book_ISBN setter
           
           Args:
               newVal = New ISBN of book
        
           Raises:
               ValueError : If the ISBN of book is not a int"""
        
        if isinstance(newVal, int):
            self._book_ISBN = newVal
            print("Book ISBN Updated")
        else:
            raise ValueError("Please eneter a valid ISBN, must be a number")
        
    @property
    def bookHardback (self):
        """_book_hardback getter"""
        return self._book_hardback
    
    @bookHardback.setter
    def bookHardback(self, newVal):
        """_book_hardback setter
           
           Args:
               newVal = New value that states binding of book
        
           Raises:
               ValueError : If the binding of book is not a boolean"""
        
        if isinstance(newVal, bool):
            self._book_hardback = newVal
            print("Book Binding Updated")
        else:
            raise ValueError("Please eneter a valid book type, must be a Boolean")
    

    def calculateShipping (self):
        """Calculates shipping cost based on whether it's hardback or paperback"""
        if self._book_hardback is True:
            self._shipping_price = 4
        else:
            self._shipping_price = 3

        print(f"The Shipping price for book: {shipping_cost_weight.bookName} is: {self._shipping_price}")
        
        






shipping_cost_weight = book()
shipping_cost_weight.bookName = "LOTR"
shipping_cost_weight.bookDescript = "Fantasy fiction"
shipping_cost_weight.bookPrice = 1.99
shipping_cost_weight.bookWeight = 6000
shipping_cost_weight.calculateShipping()

shipping_cost_type = bookType()
shipping_cost_type.bookHardback = False
shipping_cost_type.bookISBN = 5678
shipping_cost_type.calculateShipping()
