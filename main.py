from flask import Flask, redirect,render_template,request

app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def main():
    return render_template('main.html')

@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == 'POST':
        Students = {}
        result['Name'] = request.form.get('name')
        result['StudentNumber'] = request.form.get('StudentNumber')
        result['Major'] = request.form.get('major')
        result['Email'] = request.form.get('email_id') + '@' + request.form.get('email_addr')
        result['Gender'] = request.form.get('gender')
        result['ProgrammingLanguages'] = ", ".join(request.form.getlist('ProgrammingLanguages'))
    
        Students[StudentNumber] = {
            'name': name,
            'major': major,
            'email': email_id + '@' + email_addr,
            'gender': gender,
            'ProgrammingLanguages': ProgrammingLanguages
        }
        
        sorted_students = sorted(students.items(), reverse = True)
        return render_template('result.html', Students =  sorted_students)
    
if __name__=='__main__':
    app.run(debug=True)