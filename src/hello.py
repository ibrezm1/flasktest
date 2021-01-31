from flask import Flask
from waitress import serve
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route("/me")
def me_api():
    return {
        "username": "user.username",
        "theme": "user.theme",
       }
if __name__ == "__main__":
   #app.run() ##Replaced with below code to run it using waitress 
   serve(app, host='0.0.0.0', port=8002)
