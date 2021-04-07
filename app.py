from flask import Flask, render_template

# creating an app instance
app = Flask(__name__)

# use a decorator (@) to define the route for our webpage
@app.route("/")  # setting up a default page
def index():
    return "Welcome to my page!"

@app.route("/welcome/")
def welcome():
    return f"Welcome on board c:"

@app.route("/home/")
def home():
    return render_template("index.html")

# create two more pages and add the functionality for email and password
@app.route("/email/")
def get_email():
    return render_template("get_email.html")

@app.route("/page_2/")
def page_2():
    return render_template("page_2.html")

if __name__ == "__main__":
    app.run(debug=True)