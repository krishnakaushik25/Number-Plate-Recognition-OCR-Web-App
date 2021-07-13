from flask import Flask,render_template

# webserver gateway interface
app = Flask(__name__)




@app.route('/')
def index():
    return "Hello World!! I am working"
@app.route('/home')
def home():
    return render_template('test.html')

if __name__ =="__main__":
    app.run()