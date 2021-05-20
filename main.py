from flask import Flask, request, Response
import re

app = Flask("CRUD_punishman")

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(port='5000', debug=True)