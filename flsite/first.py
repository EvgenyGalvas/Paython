from flask import Flask

app = Flask(__name__)

@app.route("/index")
def index():
    return 'index'


@app.route("/about")
def about():
    return 'about'

if __name__ =='__main__':
    app.run(debug=True)