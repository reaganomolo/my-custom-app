from flask import Flask  # type: ignore[import]

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route("/how-are-you")
def hello():
    return "I am good, how about you?"

if __name__ == "__main__":
    # Bind to all interfaces so Docker can expose it
    app.run(host="0.0.0.0", port=8080)