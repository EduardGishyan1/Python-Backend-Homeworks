from fastapi import FastAPI
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
import uvicorn
from bson import ObjectId

DATABASE ='library'
COLLECTION= 'books'
mongo_uri = 'mongodb://localhost:27017'

app = FastAPI()

client = AsyncIOMotorClient(mongo_uri)

db = client[DATABASE]
books_collection = db[COLLECTION]


@app.get('/books', response_class=JSONResponse)
async def getBooks():

  book_cursor = books_collection.find()
  books = await book_cursor.to_list()
  for book in books:
    book["_id"] = str(book["_id"])
  return books

@app.get("/books/{id}")
async def get_book_by_id(id):
    
  book_cursor = books_collection.find({"_id":ObjectId(id)})
  books = await book_cursor.to_list()
  for book in books:
    book["_id"] = str(book["_id"])
  return books

if __name__ == '__main__':
  uvicorn.run('main:app', port=3005, reload=True)