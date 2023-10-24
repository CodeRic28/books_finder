from flask import Flask, request, render_template, jsonify
import subprocess
import json
from main import info

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    book_title = data.get("title")
    if book_title:
        book_info = info(book_title)
        book_info = book_info
        return jsonify(book_info)
    return jsonify({"error": "Please enter a book title"})


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
