from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "abdelrahman amr\nID:2023040129"

@app.get("/hello")
def hello():
    return "Hello World"

@app.get("/users")
def users():
    return "A list of users!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
