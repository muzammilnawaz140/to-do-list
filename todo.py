from flask import Flask, render_template, request, redirect
import pandas as pd
import os

app = Flask(__name__)
file_path = "db.csv"

def database():
    global file_path
    if os.path.exists(file_path):
        db = pd.read_csv(file_path) 
    else: 
        db = pd.DataFrame(columns=["Task", "Status"])
    return db





@app.route("/", methods=["GET", "POST"])
def index():
    search = request.args.get('search')
    db = database()
    if search:
        db = db[db['Task'].str.contains(search, case=False, na=False )]

    return render_template("index.html",todo_list = db.to_dict(orient="records"),search = search)

@app.route("/savetodo",methods=["POST"])
def savetodo():
    global file_path
    db = database()
    task = request.form.get('task')
    if not ((db['Task'] == task) & (db['Status'] == 'Pending')).any():
        new_row = pd.DataFrame([{"Task":task,"Status":"Pending"}])
        db = pd.concat([db, new_row],ignore_index=True)
        db.to_csv(file_path, index=False)
    return redirect("/")

@app.route("/remove/<int:row_no>")
def remove(row_no):
    global file_path
    db = database()
    if 0 <= row_no < len(db):
        db = db.drop(row_no).reset_index( drop = True )
        db.to_csv(file_path,index=False)


    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
