
class Product:
    
    def __init__(self, tittle, short_description, description, slug, permalink, IsAvailable, 
                 sku, price, regular_price, sale_price, manage_stock, stock_quantity, 
                 IsVisible, date_created_gmt, date_modified_gmt):
        self.tittle = tittle
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
    
    def create(self):
        pass
    
    def read(self):
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass


if __name__ == '__main__':
    pass
