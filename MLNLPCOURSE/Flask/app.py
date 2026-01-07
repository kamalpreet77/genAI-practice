from flask import Flask

# Instance of flask class 
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Home Page"


if __name__=="__main__":
    app.run(debug=True)