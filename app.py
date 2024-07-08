import psycopg2
from flask import Flask, url_for, redirect, render_template, request
from dotenv import load_dotenv
import os

load_dotenv()

db_url = "postgresql://root:GYzXqOTxsloftWiq8okOQ8nnQgxFSqL1@dpg-cq619iks1f4s73dqluk0-a.singapore-postgres.render.com/crud_app_db_otox"

db = psycopg2.connect(db_url)

app = Flask(__name__,template_folder='templat')

cursor = db.cursor()


@app.route("/")
def get_student_details():
    student_details_query = "SELECT * FROM student_detail"
    cursor.execute(student_details_query)
    student_data = cursor.fetchall()
    print("student_data-------------------->",student_data)
    return render_template("index.html", student_data=student_data)

# Add new student details
@app.route("/add_student_details", methods=["GET", "POST"])
def add_student_details():
    if request.method == 'POST':
        id = request.form.get("id")
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        email = request.form.get("email")
        password = request.form.get("password")
        add_data = "INSERT INTO student_detail (id,fname, lname, email, password) VALUES(%s, %s, %s, %s, %s)"
        values = (id,fname, lname, email, password)
        cursor.execute(add_data, values)
        db.commit()
        return redirect(url_for("get_student_details"))
    return render_template("add.html")

# Update student details
@app.route("/update_details/<int:id>", methods=["GET", "POST"])
def update_student_details(id):
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        email = request.form["email"]
        password = request.form["password"]

        
        update_query = "UPDATE student_detail SET fname=%s, lname=%s, email=%s, password=%s WHERE id=%s"
        values = (fname, lname, email, password, id)
        cursor.execute(update_query, values)
        db.commit()

        return redirect(url_for("get_student_details"))

    cursor.execute("SELECT * FROM student_detail WHERE id=%s", (id,))
    student = cursor.fetchone()


    return render_template("update.html", student=student)

# Delete student by id
@app.route("/delete_student/<int:id>")
def delete_student(id):
    delete_query = "DELETE FROM student_detail WHERE id=%s"
    cursor.execute(delete_query, (id,))
    db.commit()
    return redirect(url_for("get_student_details"))
