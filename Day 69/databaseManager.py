from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from dotenv import dotenv_values
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import dotenv_values

config = dotenv_values(".env")

class DataBaseManager:
    def __init__(self, app) -> None:
        class Base(DeclarativeBase):
            pass
        app.config['SQLALCHEMY_DATABASE_URI'] = config["DB_URI"]
        self.db = SQLAlchemy(model_class=Base)
        self.db.init_app(app)

        
        class BlogPost(self.db.Model):
            __tablename__ = "blog_posts"
            id: Mapped[int] = mapped_column(Integer, primary_key=True)
            title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
            subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
            date: Mapped[str] = mapped_column(String(250), nullable=False)
            body: Mapped[str] = mapped_column(Text, nullable=False)
            img_url: Mapped[str] = mapped_column(String(250), nullable=False)
            user_id: Mapped[int] = mapped_column(Integer, self.db.ForeignKey('users.id'), nullable=False)

            author = self.db.relationship("User", back_populates="posts")
            comments = self.db.relationship("Comment", back_populates="post")


        class User(self.db.Model, UserMixin):
            __tablename__ = "users"
            id: Mapped[int] = mapped_column(Integer, primary_key=True)
            name: Mapped[str] = mapped_column(String(250), nullable=False)
            email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
            password: Mapped[str] = mapped_column(String(250), nullable=False)

            comments = self.db.relationship("Comment", back_populates="author")
            posts = self.db.relationship("BlogPost", back_populates="author")

        
        class Comment(self.db.Model, UserMixin):
            __tablename__ = "comments"
            id: Mapped[int] = mapped_column(Integer, primary_key=True)
            text: Mapped[str] = mapped_column(Text, nullable=False)
            user_id: Mapped[int] = mapped_column(Integer, self.db.ForeignKey('users.id'), nullable=False)
            post_id: Mapped[int] = mapped_column(Integer, self.db.ForeignKey('blog_posts.id'), nullable=False)

            author = self.db.relationship("User", back_populates="comments")
            post = self.db.relationship("BlogPost", back_populates="comments")


        self.User = User
        self.BlogPost = BlogPost
        self.Comment = Comment

        with app.app_context():
            self.db.create_all()