from fastapi import FastAPI
import uvicorn
from app.books.books_router import router as books_router

app = FastAPI()
app.include_router(books_router)

if __name__ == '__main__':
  uvicorn.run('main:app', port=3001, reload=True)
  