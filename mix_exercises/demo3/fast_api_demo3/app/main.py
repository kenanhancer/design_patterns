from fastapi import FastAPI
from app.routers import books
from app.routers import users


app = FastAPI()

app.include_router(books.router)
app.include_router(users.router)
