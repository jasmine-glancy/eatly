from flask import Flask, render_template

app = Flask(__name__)

# Home page

# Meal Recommendation Page/Ask Page
@app.route("/")
def home():
    return render_template("index.html")

# Community / Feed Page

# Request a Home-Cooked Meal (Optional)

# About / Contact (Optional)

