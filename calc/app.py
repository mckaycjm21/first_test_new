from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_func():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)

@app.route("/sub")
def sub_func():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)

@app.route("/mult")
def mult_func(a, b):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult()

    return str(result)

@app.route("/div")
def div_func(a, b):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div()

    return str(result)


math_ops = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
    }

@app.route("/math/<math_op>")
def math(math_op):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = math_ops[math_op](a, b)

    return str(result)