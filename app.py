from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from setup_database import create_database  # Importing the setup_db function

# Initialize the Flask application
app = Flask(__name__, static_url_path='/static')

#app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:pass@localhost/feedback_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define your SQLAlchemy models here...

# Run the setup_db function to create the database and tables
# Run the create_database function to create the database
create_database()

# Define your Flask routes and other application logic here...


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    try:
        feedback_text = request.form['feedback']
        new_feedback = Feedback(text=feedback_text)
        db.session.add(new_feedback)
        db.session.commit()
        return redirect('/thank_you')
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

if __name__ == "__main__":
    app.run(debug=True)