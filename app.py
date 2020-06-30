from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# flask app initialize
app = Flask(__name__)

# db config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///add_member.db'
db = SQLAlchemy(app)


# AddMember Model
class AddMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    message = db.Column(db.String(255))

    def __str__(self):
        return f'My name is {self.name}'


# Index Route
@app.route('/')
def index():
    members = AddMember.query.all()
    return render_template('index.html', members=members)


# Add Member Route
@app.route('/add-member/', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        # assigning form data.
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # assigning value to db and saving.
        members = AddMember(name=name, email=email, message=message)
        db.session.add(members)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('add-member.html')


# same file run
if __name__ == '__main__':
    app.run()
