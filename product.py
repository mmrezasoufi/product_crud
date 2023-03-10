
class Product:
    _products_list = list()

    def __init__(self, title:str, short_description:str, description:str, slug:int, permalink:str, IsAvailable:bool, 
                 sku:str, price:int, regular_price:int, sale_price:int, manage_stock:bool, stock_quantity:int, 
                 IsVisible:bool, date_created_gmt, date_modified_gmt):
        self.title = title
        self.short_description = short_description
        self.description = description
        self.slug = slug
        self.permalink = permalink
        self.IsAvailable = IsAvailable
        self.sku = sku
        self.price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.manage_stock = manage_stock
        self.stock_quantity = stock_quantity
        self.IsVisible = IsVisible
        self.date_created_gmt = date_created_gmt
        self.date_modified_gmt =  date_modified_gmt
        
        self.IsExisted = False
        
        
    def __repr__(self):
        return f"Product('{self.title}','{self.description}')"
    
    def create(self):
        if not(self.IsExisted):
            self._products_list.append(self)
            self.IsExisted = True
            return self.__repr__()
        
        
        
    def read(self):
        return self.__repr__()
    
    def update(self, new_product):
        if new_product.IsExisted:
            new_product.delete()
        temp = self.IsExisted
        for i in range(len(self._products_list)):
            if self._products_list[i] == self :
                self._products_list[i] = new_product
                self = new_product
                if not(temp):
                    self.create()
                return self._products_list[i].__repr__()
                
    def delete(self):
        if self.IsExisted:
            self._products_list.remove(self)
            self.IsExisted = False
        else:
            print(f"This product does not exist in the list")
        

    def list_all(self):
        for product in self._products_list :
            print(product)
            
        