from product import Product

if __name__ == '__main__':
    test = Product(1,'phone', 'short_description','description',1,1,1,1,1,1,1,1,1,1,1,1)
    test1 = Product(2,'car', 'short_description','description',1,1,1,1,1,1,1,1,1,1,1,1)
    test2 = Product(3,'home', 'short_description','description',1,1,1,1,1,1,1,1,1,1,1,1)
    
    test.create()
    test1.create()
    test.get_all_products()
    print('#'*10)
    
    print(test.update(test2))
    print('#'*10)
    test.get_all_products()
    print('#'*10)
    
    test2.delete()
    test.get_all_products()
    print('#'*10)
    
    
    
    print(isinstance(test, Product))
    