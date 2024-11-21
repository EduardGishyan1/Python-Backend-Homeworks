from fastapi import FastAPI,HTTPException
import uvicorn

app = FastAPI()
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]
products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Smartphone", "price": 500}
]

@app.get("/users")
def get_all_users() -> list:
    return users

@app.get("/products")
def get_all_products() -> list:
    return products


@app.get("/users/{id}")
def get_user_by_id(id:int):
    for user in users:
        if user["id"] == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.get("/products/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product["id"] == id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/users/{id}")
def delete_user(id:int):
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/products/{id}")
def delete_product(id:int):
    for product in products:
        if product["id"] == id:
            products.remove(product)
            return {"message": "Product deleted successfully"}
    raise HTTPException(status_code=404, detail="Product not found")
                        

@app.post("/users")
def add_user(user:dict):
    new_id = max([user["id"] for user in users] , default=0) + 1
    user["id"] = new_id
    users.append(user)
    return user


@app.post("/products")
def add_product(product:dict):
    new_id = max([product["id"] for product in products] , default=0) + 1
    product['id'] = new_id
    products.append(product)
    return product

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=5000,reload=True)
