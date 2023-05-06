from flask import Flask, redirect,render_template,request

app=Flask(__name__)
@app.route('/', methods=['GET','POST'])
def main():
    return render_template('main.html')

@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == 'POST':
        result = dict()
        result['Name'] = request.form.get('name')
        result['StudentNumber'] = request.form.get('StudentNumber')
        result['Major'] = request.form.get('major')
        result['Email'] = request.form.get('email_id') + '@' + request.form.get('email_addr')
        result['Gender'] = request.form.get('gender')
        result['ProgrammingLanguages'] = request.form.getlist('ProgrammingLanguages')
        return render_template('result.html', result = result)

if __name__=='__main__':
    app.run(debug=True)