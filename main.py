from product import Product

if __name__ == '__main__':
    test1 = Product(1,'phone', 'short_description','description',1,1,1,1,1,1,1,1,1,1,1,1)
    test2 = Product(2,'car', 'short_description','description',1,1,1,1,1,1,1,1,1,1,1,1)
    test3 = Product(3,'home', 'short_description','description',1,1,1,1,1,1,1,1,1,1,1,1)
    
    
    test1.add()
    test2.add()
    test3.add()
    test1.get_all_products()
    # print('#'*10)
    
    # print(test1.update(test3))
    # print('#'*10)
    # test1.get_all_products()
    # print('#'*10)
    
    
    # test3.delete()
    # test1.get_all_products()
    # print('#'*10)
    
    print(isinstance(test1, Product))
    