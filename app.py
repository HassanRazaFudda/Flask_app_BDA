# pip install flask
# python -m venv venv
# pip list

from flask import Flask, render_template, request, url_for, redirect   # <- added redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(100), nullable=False)
        

@app.before_request
def creat_table():
    db.create_all()    
    

Students = [
    {
        'name': 'Ali',
        'id': '1',
        'grade': '50'
    }
]

@app.route('/')
def index():
    return render_template('show.html', data=Students)

@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        id = request.form.get('id')
        grade = request.form.get('grade')   # <- grade must match form name="grade"
        new_student = Student(
            name = name,
            grade = grade
        )
        db.session.add(new_student)
        db.session.commit()
        
        # Students.append({
        #     'name': name,
        #     'id': id,
        #     'grade': grade
        # })
        # return render_template('new-temp/index.html', data=Students)
        return redirect(url_for('index'))   # <- fixed redirect syntax
    else:
        return render_template('form.html')
    

@app.route('/profile/<id>')
def getStudent(id):
    result = None
    for s in Students:
        if s['id'] == id:
            result = s
            break;
        
    return render_template('profile.html', student= result)  

if __name__ == '__main__':
    app.run(debug=True)
