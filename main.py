from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/contact")
# def contact():
#     return render_template("contact.html")

@app.route("/contact", methods=["POST","GET"])
def receive_data():
    if request.method == "GET":
        return render_template("contact.html", h1_value="Contact Me")
    else:
        username = request.form["username"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        print(f"{username}\n{phone}\n{email}\n{message}")
        return render_template("contact.html", h1_value="Successfully Sent Your Message!")

if __name__ == "__main__":
    app.run(debug=True)
