# from flask import Flask, render_template, request, redirect, url_for
# # from book import Book
# import sqlite3
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# from sqlalchemy import Integer, String, Float

# class BooksCollection:
#     def __init__(self) -> None:
#         pass

#     def add_new_book(db, book) -> None:
#         db.session.add(book)
#         db.session.commit()

#     def get_books(db, self):
#         books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
#         return books