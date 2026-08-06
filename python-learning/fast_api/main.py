from fastapi import FastAPI
from models import Product

from database import session, engine
import database_models

app=FastAPI()

database_models.Base.metadata.create_all(bind=engine)


@app.get("/")
def greet(): 
    return "Welcome to Tausif space!"


products = [
    Product(id=1, name="Phone", description="This is very good phone", price=18880.0, quantity=2),
    Product(id=2, name="Laptop", description="High performance gaming laptop", price=62000.0, quantity=10),
    Product(id=3, name="Wireless Headphones", description="Noise-cancelling over-ear headphones", price=4500.0, quantity=15),
    Product(id=4, name="Smart Watch", description="Fitness tracker with AMOLED display", price=2999.0, quantity=8),
    Product(id=5, name="Mechanical Keyboard", description="RGB backlit mechanical keyboard", price=3500.0, quantity=5),
]


def init_db():
    db=session()
    
    count=db.query(database_models.Product).count()
     
    if count==0: 
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        
        db.commit()    


init_db()



# get api 
@app.get("/products")
def get_all_product(): 
    # db=session()
    # db.query() 
    return products


@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id==id:
            return product
    return "Product not found"


# post api 
@app.post("/product")
def add_product(product:Product):
    products.append(product)
    return product
    
    
    
# update api    
@app.put("/product") 
def update_product(id:int, product:Product):
    for i in range(len(products)):
        if products[i].id==id:
            products[i]==product
            return {"message": "Product updated successfully", "data": products[i]}
          
    return "No product found"        



# delete api 
@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i] 
            return {"message": "Product deleted successfully", "data": products}
            
    return {"message": "No product found"}    