from helpers import hello
from bottle import route, run


@route("/")
def homepage():
    return hello()


run(host="0.0.0.0", port=8080, reloader=True)
