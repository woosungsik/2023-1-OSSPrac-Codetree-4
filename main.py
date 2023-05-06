from flask import Flask, redirect,render_template,request

app=Flask(__name__)
data = dict()

@app.route('/', methods=['GET','POST'])
def main():
    return render_template('main.html')

@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == 'POST':
        Students = dict()
        Students["name"] = request.form.get('name')
        Students["StudentNumber"] = int(request.form.get('StudentNumber'))
        Students["major"] = request.form.get('major')
        Students["email"] = request.form.get('email_id') + '@' + request.form.get('email_addr')
        Students["gender"] = request.form.getlist('gender')
        Students["ProgrammingLanguages"] = ", ".join(request.form.getlist('ProgrammingLanguages'))
    
        data[Students["StudentNumber"]] = Students
        result = [data[key] for key in sorted(data)]
        return render_template('result.html', result =  result)
    
if __name__=='__main__':
    app.run(debug=True)