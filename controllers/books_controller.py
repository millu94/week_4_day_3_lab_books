from flask import Flask, render_template, redirect, request
from flask import Blueprint
from repositories import book_repository
from repositories import author_repository
from models.book import Book

books_blueprint = Blueprint("books", __name__)

# declaring a route for the list of books
@books_blueprint.route("/books")
def books():
    books = author_repository.select_all()
    return render_template("books/index.html", all_books = books)
    