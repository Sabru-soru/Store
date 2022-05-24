import csv
class Item:
    pay_rate = 0.8 #after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #print(f"I am created: {name}")
        #run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal than zero!"

        #assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self,increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property   #property decorator = read-only attribute; 
    def name(self):
        return self.__name

    @name.setter #lahko spreminjamo vrednosti
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name=value

    def calculate_total_price(self):  #temu se reče method in ne function
        return self.__price * self.quantity


    @classmethod
    def instantiate_from_csv(cls): #tole moramo dati v class method
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod #classmetode najprej pošljejo class, staticmetode pa so kot navadne funkcije        
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e= 5.0, 10.0
        if isinstance(num, float):
            # counts out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self): #da je lepši zapis print(Item.all)
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"     

    
    #Abstraction - tukaj smo zdaj naredili privatne metode
    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello, we have {self.name}
    """

    def __send(self):
        pass

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()