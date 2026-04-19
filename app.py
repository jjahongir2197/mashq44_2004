from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    result = ""

    if request.method == "POST":

        number = int(request.form.get("number"))

        if number % 2 == 0:
            result = "Juft son"
        else:
            result = "Toq son"

    return render_template("index.html", result=result)

app.run(debug=True)
