"""
flask
Question-16:
Sharing of content 
@app.route("/updatefortoday", methods=['GET','POST']) # http://localhost:5000/updatefortoday
@app.route("/share", methods=['GET'])                # http://localhost:5000/share
@app.route("/clearnotepadtxt", methods=['GET'])      # http://localhost:5000/clearnotepadtxt
"""

from flask import render_template, request, Flask
import os
import json

app = Flask(__name__)

# Load entries from JSON file on startup
entries = []
try:
    with open("data.json", "r") as f:
        entries = json.load(f)
except FileNotFoundError:
    entries = []

@app.route("/updatefortoday", methods=['GET', 'POST'])  # http://localhost:5000/updatefortoday
def updatefortoday():
    global entries
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        city = request.form.get('city')
        gender = request.form.get('gender')
        
        new_entry = dict(name=name, age=age, city=city, gender=gender)
        entries.append(new_entry)

        # Save updated entries to file
        with open("data.json", "w") as f:
            json.dump(entries, f)

        return "Data Submitted"

    # GET method - show the form
    return """
    <html>
    <head>
        <title>Updates for Today</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
            }
            .container {
                width: 400px;
                margin: 50px auto;
                padding: 30px;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
            }
            h2 {
                text-align: center;
                margin-bottom: 20px;
                color: #333;
            }
            label {
                font-weight: bold;
                display: block;
                margin-bottom: 5px;
                color: #555;
            }
            input[type="text"], input[type="number"], select {
                width: 100%;
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 5px;
                box-sizing: border-box;
            }
            input[type="submit"] {
                width: 100%;
                padding: 10px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            input[type="submit"]:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Updates for Today</h2>
            <form action="/updatefortoday" method="post">
                <label>Name:</label>
                <input type="text" name="name" required>

                <label>Age:</label>
                <input type="number" name="age" required>

                <label>City:</label>
                <input type="text" name="city" required>

                <label>Gender:</label>
                <select name="gender" required>
                    <option value="">--Select--</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="Other">Other</option>
                </select>

                <input type="submit" value="Submit">
            </form>
        </div>
    </body>
    </html>
    """

@app.route("/share", methods=['GET'])
def share():
    return render_template("share.html", entries=entries)

@app.route("/clearnotepadtxt", methods=['GET'])  # http://localhost:5000/clearnotepadtxt
def clearnotepadtxt():
    entries.clear()
    with open("data.json", "w") as f:
        json.dump(entries, f)
    return "<h3>All entries have been cleared!</h3><a href='/updatefortoday'>Go Back</a>"

if __name__ == '__main__':
    app.run(debug=True)
