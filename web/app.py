from flask import Flask, render_template, request, redirect, session
from logic.user_logic import UserLogic
import requests
import bcrypt

app = Flask(__name__)
app.secret_key = "ThisIsTheSecretKey"


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    data = {}
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        """validaciones de recaptha y base de datos"""
        data["secret"] = "6Lf2NzMbAAAAAO5pyzOSfVGWNLbWyskOofmduI3s"
        data["response"] = request.form["g-recaptcha-response"]
        response = requests.post(
            "https://www.google.com/recaptcha/api/siteverify", params=data
        )
        if response.status_code == 200:
            messageJson = response.json()
            if messageJson["success"]:
                """si el recaptcha es valido -  success"""
                logic = UserLogic()
                userName = request.form["username"]
                userEmail = request.form["useremail"]
                passwd = request.form["passwd"]
                confpasswd = request.form["confpasswd"]
                if passwd == confpasswd:
                    salt = bcrypt.gensalt(rounds=14)
                    strSalt = salt.decode("utf-8")
                    encPasswd = passwd.encode("utf-8")
                    hashPasswd = bcrypt.hashpw(encPasswd, salt)
                    strPasswd = hashPasswd.decode("utf-8")
                    rows = logic.insertUser(userName, userEmail, strPasswd, strSalt)
                    return redirect("login")
                else:
                    return redirect("register")
            else:
                return redirect("register")
        return f"posted register rows: {rows}"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        """ validacion del codigo de base de datos """
        logic = UserLogic()
        userEmail = request.form["email"]
        passwd = request.form["passwd"]
        userDict = logic.getUserByEmail(userEmail)
        salt = userDict["salt"].encode("utf-8")
        hashPasswd = bcrypt.hashpw(passwd.encode("utf-8"), salt)
        dbPasswd = userDict["password"].encode("utf-8")
        if hashPasswd == dbPasswd:
            """si pasa esta validacion entonces todos nuestros saltos de seguridad estan bien"""

            """ crear la sesion """
            session["login_user"] = userEmail
            session["loggedIn"] = True
            return redirect("dashboard")
        else:
            return redirect("login")
    else:
        return redirect("login")

    return redirect("login")


if __name__ == "__main__":
    app.run(debug=True)
