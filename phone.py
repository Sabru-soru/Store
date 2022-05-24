from item import Item

class Phone(Item): #s tem podeduje te metode, to je child class
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0): #s super function potegneš tudi prejšnje
        #Call to super function to have access to all attributes
        super().__init__(
            name, price, quantity
        )

        #print(f"I am created: {name}")
        #run validations to the received arguments
        assert broken_phones >= 0, f"broken_phones {broken_phones} is not greater or equal than zero!"
        #assign to self object
        self.broken_phones = broken_phones