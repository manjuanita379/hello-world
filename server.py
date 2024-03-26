from flask import Flask

PORT = 8000
MESSAGE = "Hello, world!\n"

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("hello world")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="54.151.2.1", port=8000)
