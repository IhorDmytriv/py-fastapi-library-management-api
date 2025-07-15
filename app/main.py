from typing import List

from fastapi import FastAPI, Depends, HTTPException
from fastapi.params import Query
from sqlalchemy.orm import Session

from crud import (
    get_all_authors,
    create_author,
    create_book,
    get_author_by_id,
    get_all_books
)
from db.database import get_db
from schemas import (
    AuthorListSchema,
    AuthorCreateSchema,
    BookListSchema,
    BookCreateSchema,
    AuthorRetrieveSchema
)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/authors/", response_model=AuthorListSchema)
def add_author(author: AuthorCreateSchema, db: Session = Depends(get_db)):
    return create_author(db, author)


@app.get("/authors/", response_model=List[AuthorListSchema])
def list_authors(db: Session = Depends(get_db)):
    authors = get_all_authors(db)
    if not authors:
        raise HTTPException(status_code=404, detail="Authors not found")
    return authors


@app.get("/authors/{author_id}", response_model=AuthorRetrieveSchema)
def retrieve_author(author_id: int, db: Session = Depends(get_db)):
    film = get_author_by_id(db, author_id)
    if not film:
        raise HTTPException(status_code=404, detail="Author not found")
    return film


@app.post("/books/", response_model=BookListSchema)
def add_book(book: BookCreateSchema, db: Session = Depends(get_db)):
    return create_book(db, book)


@app.get("/books/", response_model=List[BookListSchema])
def list_books(
        db: Session = Depends(get_db),
        author_id: int = Query(None)
):
    books = get_all_books(db, author_id)
    if not books:
        raise HTTPException(status_code=404, detail="Books not found")
    return books
