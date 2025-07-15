from sqlalchemy.orm import Session

from db import models
from schemas import BookCreateSchema, AuthorCreateSchema


# Author
def create_author(db: Session, author: AuthorCreateSchema) -> models.DBAuthor:
    db_author = models.DBAuthor(
        name=author.name,
        bio=author.bio
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)

    return db_author


def get_all_authors(db: Session):
    return db.query(models.DBAuthor).all()


def get_author_by_id(db: Session, author_id: int):
    return (
        db
        .query(models.DBAuthor)
        .filter(models.DBAuthor.id == author_id)
        .one_or_none()
    )


# Book
def get_all_books(db: Session, author_id: int):
    books = db.query(models.DBBook)
    if author_id:
        books = books.filter_by(author_id=author_id)
    return books.all()


def create_book(db: Session, book: BookCreateSchema) -> models.DBBook:
    db_book = models.DBBook(
        title=book.title,
        summary=book.summary,
        publication_date=book.publication_date,
        author_id=book.author_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book
