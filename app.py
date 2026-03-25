from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/sobre")
def sobre():
    return "Página sobre"

@app.route("/usuario/<int:id>")
def usuario(id):
    return {
        "usuario":"id"
    }


with app.test_request_context():
    print(url_for('home'))
    print(url_for('sobre'))
    print(url_for('home', next='/'))
    print(url_for('usuario', id=1))

if __name__ == "__main__":
    app.run(debug=True)