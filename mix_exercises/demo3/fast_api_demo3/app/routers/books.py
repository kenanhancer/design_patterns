from fastapi import HTTPException, Depends, status
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from app.schemas.book import Book, BookBase

# Initialize the InferringRouter with metadata
router = InferringRouter(
    prefix="/books",
    tags=["books"],
    responses={
        status.HTTP_400_BAD_REQUEST: {"description": "Bad Request"},
        status.HTTP_404_NOT_FOUND: {"description": "Not Found"},
    },
)


# In-Memory Data Storage with Initial Data
initial_books: list[Book] = [
    Book(id=1, title="1984", author="George Orwell"),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee"),
    Book(id=3, title="The Great Gatsby", author="F. Scott Fitzgerald"),
    Book(id=4, title="The Catcher in the Rye", author="J.D. Salinger"),
]


class BookManager:
    def __init__(self, books: list[Book]):
        self.books: list[Book] = books
        self.book_id_counter = len(books) + 1  # Starts from the next available ID

    def get_all_books(self):
        return self.books

    def create_book(self, book_data: BookBase):
        new_book = Book(id=self.book_id_counter, **book_data.model_dump())
        self.books.append(new_book)
        self.book_id_counter += 1
        return new_book

    def get_book(self, book_id: int):
        return next((book for book in self.books if book.id == book_id), None)

    def update_book(self, book_id: int, book_update: BookBase):
        for idx, book in enumerate(self.books):
            if book.id == book_id:
                updated_book = Book(id=book_id, **book_update.model_dump())
                self.books[idx] = updated_book
                return updated_book
        return None

    def delete_book(self, book_id: int):
        original_length = len(self.books)
        self.books = [book for book in self.books if book.id != book_id]
        return len(self.books) < original_length  # Returns True if a book was deleted


book_manager = BookManager(initial_books)


@cbv(router)
class BookView:
    book_manager: BookManager = Depends(lambda: book_manager)

    @router.get(
        "/",
        response_model=list[Book],
        status_code=status.HTTP_200_OK,
        summary="Retrieve All Books",
        description="Fetch a list of all books in the system.",
        responses={200: {"description": "List of books retrieved successfully."}},
    )
    def get_books(self):
        return self.book_manager.get_all_books()  # pylint: disable=no-member

    @router.post(
        "/",
        response_model=Book,
        status_code=status.HTTP_201_CREATED,
        summary="Create a New Book",
        description="Add a new book to the collection.",
        responses={
            201: {"description": "Book created successfully."},
            400: {"description": "Invalid input data."},
        },
    )
    def create_book(self, new_book: BookBase):
        return self.book_manager.create_book(new_book)  # pylint: disable=no-member

    @router.get(
        "/{book_id}",
        response_model=Book,
        status_code=status.HTTP_200_OK,
        summary="Retrieve a Book by ID",
        description="Fetch details of a specific book using its ID.",
        responses={
            200: {"description": "Book details retrieved successfully."},
            404: {"description": "Book not found."},
        },
    )
    def get_book(self, book_id: int):
        book = self.book_manager.get_book(book_id)  # pylint: disable=no-member
        if book is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
            )
        return book

    @router.put(
        "/{book_id}",
        response_model=Book,
        status_code=status.HTTP_200_OK,
        summary="Update a Book",
        description="Modify details of an existing book using its ID.",
        responses={
            200: {"description": "Book updated successfully."},
            404: {"description": "Book not found."},
            400: {"description": "Invalid input data."},
        },
    )
    def update_book(self, book_id: int, book_update: BookBase):
        updated_book = self.book_manager.update_book(  # pylint: disable=no-member
            book_id, book_update
        )
        if updated_book is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
            )
        return updated_book

    @router.delete(
        "/{book_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete a Book",
        description="Remove a book from the collection by its ID.",
        responses={
            204: {"description": "Book deleted successfully."},
            404: {"description": "Book not found."},
        },
    )
    def delete_book(self, book_id: int):
        if not self.book_manager.delete_book(book_id):  # pylint: disable=no-member
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
            )
