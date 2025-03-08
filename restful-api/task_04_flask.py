#!/usr/bin/python3
"""
This is a module docstring
"""
from flask import Flask, request, jsonify


USERS = {}

app = Flask(__name__)


@app.get("/")
def home():
    return "Welcome to the Flask API!"


@app.get("/status")
def status():
    return "OK"


@app.get("/data")
def data():
    return jsonify(list(USERS.keys()))


@app.get("/users/<username>")
def get_username(username: str):
    data = USERS.get(username, None)

    if data is None:
        return { "error": "User not found" }, 404

    return jsonify(data)


@app.post("/add_user")
def add_user():
    data = request.get_json()

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    USERS[data["username"]] = data
    
    res = {
        "message": "User added",
        "user": data,
    }

    return jsonify(res), 201


if __name__ == "__main__":
    app.run()
