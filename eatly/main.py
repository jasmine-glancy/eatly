from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Meal Recommendation Page/Ask Page
@app.route("/ask_page")
def ask_page():
    return render_template("ask_page.html")

# Community / Feed Page

# Request a Home-Cooked Meal (Optional)

# About / Contact (Optional)


