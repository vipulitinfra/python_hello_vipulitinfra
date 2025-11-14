from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from vipulitinfra!"
 @app.route('/home')
 def home():
    return "Hello from vipulitinfra1111111111!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
