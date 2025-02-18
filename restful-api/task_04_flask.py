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
        return jsonify(
            data={
                "error": "User not found"
            },
            status=400
        )

    return jsonify(data)


@app.post("/add_user")
def add_user():
    data = request.json

    if isinstance(data, dict):
        if "username" not in data:
            return jsonify(
                data={"error": "Username is required"},
                status=400
            )

        USERS[data["username"]] = data

    return jsonify(
        data = {
            "message": "User added",
            "user": data,
        },
        status=201
    )


if __name__ == "__main__":
    app.run()
