from flask import Flask, render_template, request, redirect

app = Flask(__name__)

USERNAME = "allen"
PASSWORD = "2007"

student_data = {}

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and password == PASSWORD:
            return redirect('/home')

    return render_template("login.html")


@app.route('/home', methods=['GET','POST'])
def home():
    global student_data

    if request.method == 'POST':
        name = request.form['student_name']
        m1 = int(request.form['m1'])
        m2 = int(request.form['m2'])
        m3 = int(request.form['m3'])
        m4 = int(request.form['m4'])
        m5 = int(request.form['m5'])

        total = m1 + m2 + m3 + m4 + m5
        percentage = round(total / 5, 2)

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "Fail"

        status = "PASS" if percentage >= 50 else "FAIL"

        # Save student
        file = open("students.txt", "a")
        file.write(name + "," + str(total) + "," + str(percentage) + "," + grade + "," + status + "\n")
        file.close()

        student_data = {
            "name": name,
            "m1": m1,
            "m2": m2,
            "m3": m3,
            "m4": m4,
            "m5": m5,
            "total": total,
            "percentage": percentage,
            "average": percentage,
            "grade": grade,
            "status": status
        }

        return render_template("result.html", **student_data)

    return render_template("index.html")


@app.route('/resultcard')
def resultcard():
    return render_template("result_card.html", **student_data)


@app.route('/report')
def report():
    return render_template("report.html")


@app.route('/students')
def students():
    data = []
    file = open("students.txt", "r")
    for line in file:
        data.append(line.strip().split(","))
    file.close()

    return render_template("students.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)