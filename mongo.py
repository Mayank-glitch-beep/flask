from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas connection (replace with your URI)
client = MongoClient("mongodb+srv://nathanimayank09_db_user:bHjVyNuu54Ph829U@cluster0.ygxgep5.mongodb.net/?appName=Cluster0")
db = client["student_db"]
collection = db["students"]

@app.route('/')
def form():
    return render_template('form.html')
 
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        grade = request.form['grade']

        data = {
            "name": name,
            "grade": grade
        }

        collection.insert_one(data)

        return redirect(url_for('success'))

    except Exception as e:
        return render_template('form.html', error=str(e))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)