from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from datetime import datetime
from flask import jsonify  # Import jsonify for handling JSON responses

app = Flask(__name__, static_folder='assets')
app.config["MONGO_URI"] = "mongodb+srv://zarific:!SecreT!@zarific.qqtjtp3.mongodb.net/zarificdb"
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Get the current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

        # Store the data in MongoDB along with the timestamp
        mongo.db.contacts.insert_one({
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
            'timestamp': current_time
        })

        # Return a JSON response indicating success
        return jsonify({"status": "success", "message": "Thank you! Your submission has been received!"})
    else:
        # Return a JSON response indicating failure
        return jsonify({"status": "error", "message": "Message was not sent"})



@app.route('/audio1')
def audio1():
    return render_template("audio1.html")

@app.route('/audio2')
def audio2():
    return render_template("audio2.html")

@app.route('/audio3')
def audio3():
    return render_template("audio3.html")

@app.route('/podcast1')
def podcast1():
    return render_template("podcast1.html")

@app.route('/podcast2')
def podcast2():
    return render_template("podcast2.html")

@app.route('/podcast3')
def podcast3():
    return render_template("podcast3.html")

@app.route('/music1')
def music1():
    return render_template("music1.html")

@app.route('/music2')
def music2():
    return render_template("music2.html")

@app.route('/music3')
def music3():
    return render_template("music3.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)