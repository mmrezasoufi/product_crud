from product import Product
from datetime import datetime
if __name__ == '__main__':
    phone_1 = Product('samsung phone', 'smart phone',
                    "Samsung, South Korean company that is one of the world's largest producers of electronic devices.",
                    'GALAXY A53 ','https://samsung.com', True, 'ADDS32E',
                    600.20,
                    950.59,
                    0,
                    False,
                    4,
                    datetime.now(),
                    datetime.now(),
                    1)
    
    phone_2 = Product('apple phone', 'smart phone',
                    "apple phone with ...",
                    'iphone 13 ','https://apple.com', True, 'ADDS32E',
                    600.20,
                    950.59,
                    0,
                    False,
                    4,
                    datetime.now(),
                    datetime.now(),
                    1)
    
    car = Product('bmw car', 'sedan car',
                    "BMW Serie 8 Gran Coupe,Curb weight: 2,070 kg , Engine: 4.4 L V8 ",
                    'BMW Serie 8 Gran Coupe ','https://bmw.com', True, 'SF23F',
                    77850,
                    79600,
                    0,
                    False,
                    3,
                    datetime.now(),
                    datetime.now(),
                    2)

    
    phone_1.create()
    print(phone_1.read())
    
    print('*'*10)
    
    car.create()
    car.list_all()
    
    print('*'*10)
    
    phone_1.delete()
    car.list_all()
    
    print('*'*10)
    
    phone_1.create()
    phone_1.update(phone_2)
    phone_2.list_all()
    
    print('*'*10)
    
    print(type(phone_1))
    print(isinstance(car, Product))
    