from bottle import route, run

@route('/')
def index():
    return "<b>Hello</b>"


run(host='0.0.0.0', port=8080)

