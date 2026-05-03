from flask import Flask, render_template, redirect, url_for, request
from flask_login import (
    LoginManager, UserMixin,
    login_user, login_required,
    logout_user, current_user
)
import sqlite3
#from AlphaBot import AlphaBot

app = Flask(__name__)
app.secret_key = "ChiaveSegreta"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
DB="db.db"

#a = AlphaBot()
def crea_db():
    db = sqlite3.connect(DB)
    cur = db.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS login (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)

    cur.execute("""
    INSERT OR IGNORE INTO login (username, password) VALUES 
    ('user1', 'pass1'),
    ('user2', 'pass2')            
    """)
    db.commit()

def carica_users_from_db(): 
    db = sqlite3.connect(DB) 
    cur = db.cursor() 
    cur.execute("SELECT username, password FROM login") 
    rows = cur.fetchall() 
    db.close() 
    users = {} 
    for username, password in rows: 
        users[username] = {"password": password} 
    return users

crea_db() 
USERS = carica_users_from_db()

class User(UserMixin): 
    def __init__(self, username): 
        self.id = username 

@login_manager.user_loader 
def load_user(user_id): 
    if user_id in USERS: return User(user_id) 
    return None 

@app.route("/", methods=["GET", "POST"]) 
@app.route("/login", methods=["GET", "POST"]) 
def login(): 
    if request.method == "POST": 
        username = request.form["username"] 
        password = request.form["password"] 
        if username in USERS and USERS[username]["password"] == password: 
            login_user(User(username)) 
            return redirect(url_for("movimento")) 
    return render_template("index.html") 

@app.route("/logout") 
@login_required 
def logout(): 
    return render_template("index.html")

@app.route("/movimento", methods=["POST", "GET"])
@login_required
def movimento():
    movimento = request.form.get("mov")
    if movimento == "avanti":
        #a.forward()
        print("a")
    elif movimento == "indietro":
        #a.backward()
        print("i")
    elif movimento == "sinistra":
        #a.left()
        
        print("s")
    elif movimento == "destra":
        #a.right()
        print("d")
    elif movimento == "stop":
        #a.stop()
        print("st")

    return render_template("movimento.html")


if __name__ == "__main__":
    app.run(debug=True)