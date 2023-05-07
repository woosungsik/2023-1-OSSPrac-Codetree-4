from flask import Flask, redirect,render_template,request

app=Flask(__name__)
data = dict()

@app.route('/', methods=['GET','POST'])
def main():
    return render_template('main.html')

@app.route('/result', methods=['GET','POST'])
def result():
    if request.form.get("delete row"):
        result = list(data.values())
        result.sort(key = lambda x: x["StudentNumber"])
        for i in reversed(request.form.getlist('studentNumber')):
            del result[int(i)]

        return render_template('result.html', result =  result)

    if request.method == 'POST':
        Students = dict()
        Students['name'] = request.form.get('name')
        Students['StudentNumber'] = request.form.get('StudentNumber')
        Students['major'] = request.form.get('major')
        Students['email'] = request.form.get('email_id') + '@' + request.form.get('email_addr')
        Students['gender'] = request.form.get('gender')
        Students['ProgrammingLanguages'] = ", ".join(request.form.getlist('ProgrammingLanguages'))

        data[Students["StudentNumber"]] = Students
        
        result = list(data.values())
        result.sort(key = lambda x: x["StudentNumber"])
        
        return render_template('result.html', result =  result)
    
@app.route('/home')
def home():
   data.clear()
   
   return redirect('/')

if __name__=='__main__':
    app.run(debug=True)