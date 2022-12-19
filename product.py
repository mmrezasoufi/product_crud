
class Product:
    _products_list = list()

    def __init__(self, id, title, short_description, description, slug, permalink, IsAvailable, 
                 sku, price, regular_price, sale_price, manage_stock, stock_quantity, 
                 IsVisible, date_created_gmt, date_modified_gmt):
        self._id = id
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
        
        
    def __repr__(self):
        return f"Product('{self._id}','{self.title}','{self.description}')"
    
    def create(self):
        self._products_list.append(self)
        
    def read(self):
        pass
    
    def update(self, new_product):
        for i in range(len(self._products_list)):
            if self._products_list[i] == self :
                self._products_list[i] = new_product
                break
                
    def delete(self):
        self._products_list.remove(self)

    def get_all_products(self):
        for product in self._products_list :
            print(product)
            
        