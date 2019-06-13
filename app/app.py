from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def hello():
    name = "Hello"
    return render_template('index.html', name=name)

if __name__ == "__main__":
    app.run()
