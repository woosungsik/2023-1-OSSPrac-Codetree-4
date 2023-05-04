from flask import Flask, redirect,render_template,request

app=Flask(__name__)
@app.route('/', methods=['GET','POST'])
def main():
    return render_template('main.html')

@app.route('/result', methods=['GET','POST'])
def result():
    return render_template('result.html')

if __name__=='__main__':
    app.run()