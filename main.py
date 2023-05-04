from flask import Flask, redirect, render_templates, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return('Hello World! \n CodeTree 입니다.')

if __name__ == '__main__':
    app.run()