from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username=="Eric" and password=="1234":
            return "Yup, you found my password"
        else:
            return render_template("index.html")
    return render_template("index.html")

app.run(debug=True)
