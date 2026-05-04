from flask import Flask, render_template, request, redirect, url_for, flash
import yaml
from mail import mail, send_email
from dotenv import load_dotenv

load_dotenv()

import os
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev")
app.config.from_object("config")

mail.init_app(app)

def load_content():
    with open("content.yaml") as f:
        return yaml.safe_load(f)

# Home page
@app.route("/")
def home():
    content = load_content()
    return render_template("page.html", page=content["home"])

# Dynamic pages
@app.route("/<page_name>")
def page(page_name):
    content = load_content()
    page_data = content.get(page_name)

    if not page_data:
        return "Page not found", 404

    return render_template("page.html", page=page_data)

# Contact form submission
@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    subject = "New Contact Form Submission"

    body = f"""
    Name: {name}
    Email: {email}
    
    Message:
    {message}
    """
    try:
        send_email(app, app.config["CONTACT_EMAIL"], subject, body)
        flash("Form submitted successfully!")
    except Exception as e:
        print(e)
        flash("Error submitting form!")
    
    return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True)