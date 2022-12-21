from product import Product

if __name__ == '__main__':
    test = Product(1,'phone', 'short_description','description',1,1,1,1,1,1,1,1,1,1,1,1)
    test.create()
    test.get_all_products()
    print(isinstance(test, Product))