from flask import Flask,render_template, request
import find_sal
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/model',methods=['POST'])
def mod():
    return render_template('model.html')

@app.route('/output',methods=['POST'])
def output():
    if request.method == 'POST':
        age = request.form['age']
        workclass = request.form['workclass']
        education = request.form['Education']
        race = request.form['race']
        sex = request.form['sex']
        hpw = request.form['hpw']
        country = request.form['country']
        result = find_sal.find_saly(age,workclass,education,race,sex,hpw,country)
    if result == 0:
        resp = "Not Wealthy"
    else:
        resp = "Wealthy"
    return resp

if __name__ == '__main__':
    app.run(debug=True)
