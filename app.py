from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/contact')
def contacts():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/thanks')
def thanks():
    name = request.args.get('name')
    email = request.args.get('email')
    props = {
        "name": name,
        "email": email
    }
    return render_template("thanks.html", data=props)

if __name__ == '__main__':
    app.run(debug=True)

