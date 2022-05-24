from item import Item

class Keyboard(Item): #s tem podeduje te metode, to je child class
    pay_rate=0.7
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0): #s super function potegneš tudi prejšnje
        super().__init__(
            name, price, quantity
        )