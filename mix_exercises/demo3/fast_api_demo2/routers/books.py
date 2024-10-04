from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


# Initialize the InferringRouter with metadata
router = APIRouter(
    prefix="/books", tags=["books"], responses={404: {"description": "Not Found"}}
)

# Pydantic Schemas
class BookBase(BaseModel):
    title: str
    author: str


class Book(BookBase):
    id: int


class BookManager:
    def __init__(self):
        # In-Memory Data Storage with Initial Data
        self.books: list[Book] = [
            Book(id=1, title="1984", author="George Orwell"),
            Book(id=2, title="To Kill a Mockingbird", author="Harper Lee"),
            Book(id=3, title="The Great Gatsby", author="F. Scott Fitzgerald"),
        ]
        self.book_id_counter = 4  # Starts from the next available ID

    def get_all_books(self):
        return self.books

    def create_book(self, book_data: BookBase):
        new_book = Book(id=self.book_id_counter, **book_data.dict())
        self.books.append(new_book)
        self.book_id_counter += 1
        return new_book

    def get_book(self, book_id: int):
        return next((book for book in self.books if book.id == book_id), None)

    def update_book(self, book_id: int, book_update: BookBase):
        for idx, book in enumerate(self.books):
            if book.id == book_id:
                updated_book = Book(id=book_id, **book_update.dict())
                self.books[idx] = updated_book
                return updated_book
        return None

    def delete_book(self, book_id: int):
        original_length = len(self.books)
        self.books = [book for book in self.books if book.id != book_id]
        return len(self.books) < original_length  # Returns True if a book was deleted


book_manager = BookManager()


@router.get("/", response_model=list[Book])
def read_books():
    return book_manager.get_all_books()


@router.post("/", response_model=Book, status_code=201)
def create_book(book: BookBase):
    return book_manager.create_book(book)


@router.get("/{book_id}", response_model=Book)
def read_book(book_id: int):
    book = book_manager.get_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookBase):
    updated_book = book_manager.update_book(book_id, book_update)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book


@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int):
    deleted = book_manager.delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
