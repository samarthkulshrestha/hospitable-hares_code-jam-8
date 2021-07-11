from api import app
import secrets

@app.route("/join")
def join():
    return secrets.token_hex(64)

