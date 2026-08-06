from fastapi import FastAPI, Depends
from models import Product
from sqlalchemy.orm import Session

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
    Product(id=6, name="Mouse", description="Wired mouse for daily use", price=500.0, quantity=50),
]


def get_db():
    db=session()
    try:
        yield db
        
    finally:    
        db.close()



def init_db():
    db=session()
    
    count=db.query(database_models.Product).count()
    print("this is count: ", count)
     
    if count==0: 
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        
        db.commit()    


init_db()



# get api 
@app.get("/products")
def get_all_product(db:Session=Depends(get_db)): 
    
    db_products=db.query(database_models.Product).all()
    return db_products


@app.get("/product/{id}")
def get_product_by_id(id:int, db:Session=Depends(get_db)):

    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    
    if db_product:
        return db_product
    
    return "Product not found"


# post api 
@app.post("/product")
def add_product(product:Product, db:Session=Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product
    
    
    
# update api    
@app.put("/product") 
def update_product(id:int, product:Product, db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
          
    if db_product:   
        db_product.name= product.name
        db_product.description=product.description
        db_product.price=product.price
        db_product.quantity=product.quantity
        db.commit()
        return {"message":"Product Updated"}
    else:
        return "No product found"        



# delete api 
@app.delete("/product")
def delete_product(id: int, db:Session=Depends(get_db)):
   db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
   
   if db_product:
       db.delete(db_product)
       db.commit() 
       
   else:         
       return {"message": "No product found"}    