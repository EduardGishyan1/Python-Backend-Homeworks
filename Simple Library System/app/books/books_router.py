from fastapi import HTTPException,APIRouter
from fastapi.responses import JSONResponse
from bson import ObjectId
from app.models.books_model import Books
from typing import List
from config import settings
from app.db.db_connection import books_collection

MONGO_URI = settings.MONGO_URI
DATABASE = settings.DATABASE
COLLECTION = settings.COLLECTION

router = APIRouter(prefix = "/books")

@router.get('/', response_class=JSONResponse)
async def getBooks():
  book_cursor = books_collection.find()
  books = await book_cursor.to_list()
  for book in books:
    book["_id"] = str(book["_id"])
  return books

@router.get("/{id}")
async def get_book_by_id(id):
  book_cursor = books_collection.find({"_id":ObjectId(id)})
  books = await book_cursor.to_list()
  for book in books:
    book["_id"] = str(book["_id"])
  return books

@router.post("/")
async def add_book(books:List[Books]):
  try:
    book_ids = {}
    count = 1
    
    for book in books:
      book_for_insert = book.model_dump()
      book_for_insert["status"] = book.status.value
      result = await books_collection.insert_one(book_for_insert)
      book_ids[f"book {count}"] = str(result.inserted_id)
      count += 1
      
    return {f"book(s) successfully added, id(s)": book_ids}
  
  except Exception as e:
    raise HTTPException(status_code = 500,detail = str(e))
  
@router.put("/{id}")
async def update_book(book_id: str,book: Books):
  book_update = book.dict(exclude_unset = True)
  
  if book_update.get("status"):
    book_update["status"] = book_update["status"].value
  
  existing_book = books_collection.find_one({"_id": ObjectId(book_id)})
  
  if not existing_book:
    raise HTTPException(status_code = 404, detail = "Book not found")
  
  result = books_collection.update_one({"_id":ObjectId(book_id)},{"$set":book_update})
  
  if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Book not found or no changes made")

  return {"message": f"Book {book_id} successfully updated"}

@router.delete("/{book_id}")
async def delete_book(book_id:str):
  try:
      result = await books_collection.delete_one({"_id": ObjectId(book_id)})
        
      if result.deleted_count == 0:
          raise HTTPException(status_code=404, detail="Book not found")
        
      return {"message": f"Book {book_id} successfully deleted"}

  except Exception as e:
      raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    