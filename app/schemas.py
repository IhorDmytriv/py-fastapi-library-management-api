from datetime import datetime

from pydantic import BaseModel

# Author Schemas
class AuthorBaseSchema(BaseModel):
    name: str
    bio: str


class AuthorCreateSchema(AuthorBaseSchema):
    pass


class AuthorListSchema(AuthorBaseSchema):
    id: int

    class Config:
        orm_mode = True

# Book Schemas
class BookBaseSchema(BaseModel):
    title: str
    summary: str
    publication_date: datetime
    author = AuthorListSchema

class BookCreateSchema(BookBaseSchema):
    pass

class BookListSchema(BookBaseSchema):
    id: int

    class Config:
        orm_mode = True
