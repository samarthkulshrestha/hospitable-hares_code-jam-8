from flask import Flask

app = Flask(__name__)

from api import auth  # noqa: E402 F401
