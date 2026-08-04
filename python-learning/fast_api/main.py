from fastapi import FastAPI
from models import Product

app=FastAPI()


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




@app.get("/products")
def get_all_product():     
    return products


@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id==id:
            return product
    return "Product not found"



@app.post("/product")
def add_product(product:Product):
    products.append(product)
    return product
    