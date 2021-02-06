from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/SignIn')
def SignIn():
    return render_template('signIn.html')


@app.route('/LogIn')
def LogIn():
    return render_template('logIn.html')

if __name__ == '__main__':
    app.run(debug=True)
