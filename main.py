from fastapi import FastAPI ,Request
from mock_data import products
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/home")
def house(): 
    return {"home":"sweet Home"}


@app.get("/contact")
def contact():
    return {"contact:you can connect us here"}


@app.get("/products")
def get_products():
    return products

# handling path parameters  

@app.get("/products/{id}")
def get_one_product(id:int):
     for product in products:
        if product["id"] == id:
            return product
     return {"error": "Product not found"}
 

#handling query parameter 

@app.get("/greet")
def greet_name(name:str):
    return{"message": f"hello {name}"}


#handling query parameter with large amount of params 
#we can do that using a request 

@app.get("/longGreet")
def greet_user(request:Request):
    name = request.query_params.get("name")
    age = request.query_params.get("age")
    city = request.query_params.get("city")
    return {"message": f"hello {name} from {city} who is {age} years old"}