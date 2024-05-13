#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def stuff(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<parameter>')
def morestuff(parameter):
    count = ''
    for i in range(0, int(parameter)):
        count += f'{i}\n'
    return f'{count}'

@app.route('/math/<first_num>/<operation>/<sec_num>')
def mathstuff(first_num, operation, sec_num):
    if operation == "+":
        return str(int(first_num) + int(sec_num))
    elif operation == "-":
        return str(int(first_num) - int(sec_num))
    elif operation == "*":
        return str(int(first_num) * int(sec_num))
    elif operation == "div":
        return str(int(first_num) / int(sec_num))
    elif operation == "%":
        return str(int(first_num) % int(sec_num))
