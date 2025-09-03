from enum import Enum 

class CoffeeType(Enum):
    AMERICANO = 0,
    ESPRESSO = 1,
    CAPPUCCINO = 2,

class Coffee:
    def __init__(self, price: float):
        self.__price= price

    def get_price(self) -> float:
        return self.__price
    
class CoffeeAmericano(Coffee):
    def __init__(self):
        super().__init__(3.5)


class CoffeeEspresso(Coffee):
    def __init__(self):
        super().__init__(17.5)


class CoffeeCappuccino(Coffee):
    def __init__(self):
        super().__init__(5.5)


def crate_coffee(coffee_type: CoffeeType) -> Coffee:
    
    factory_dict = {
        CoffeeType.AMERICANO: CoffeeAmericano,
        CoffeeType.ESPRESSO: CoffeeEspresso,
        CoffeeType.CAPPUCCINO: CoffeeCappuccino
    }
    return factory_dict[coffee_type]()

if __name__ =='__main__':
    for coffee in CoffeeType:
        my_coffee = crate_coffee(coffee)
        print(f'Coffee type: {coffee}, price: {my_coffee.get_price()}')