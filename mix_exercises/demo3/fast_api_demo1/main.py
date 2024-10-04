from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class BookBase(BaseModel):
    title: str
    author: str


class Book(BookBase):
    id: int


books: list[Book] = [
    Book(id=1, title="1984", author="George Orwell"),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee"),
    Book(id=3, title="The Great Gatsby", author="F. Scott Fitzgerald"),
]
BOOK_ID_COUNTER = 1


@app.get("/books", response_model=list[Book])
def read_books():
    return books


@app.post("/books", response_model=Book, status_code=201)
def create_book(book: BookBase):
    global BOOK_ID_COUNTER
    new_book = Book(id=BOOK_ID_COUNTER, **book.dict())
    books.append(new_book)
    BOOK_ID_COUNTER += 1
    return new_book


@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int):
    book = next((b for b in books if b.id == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookBase):
    for idx, book in enumerate(books):
        if book.id == book_id:
            updated_book = Book(id=book_id, **book_update.dict())
            books[idx] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    global books
    books = [b for b in books if b.id != book_id]
