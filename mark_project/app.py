from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        # When marks are submitted
        if request.form.get("logged") == "yes":

            name = request.form["student_name"]

            m1 = int(request.form["m1"])
            m2 = int(request.form["m2"])
            m3 = int(request.form["m3"])
            m4 = int(request.form["m4"])
            m5 = int(request.form["m5"])

            total = m1 + m2 + m3 + m4 + m5
            percentage = round(total / 5, 2)

            if percentage >= 90:
                grade = "A+"
                message = "🌟 Outstanding Performance!"
            elif percentage >= 75:
                grade = "A"
                message = "👏 Excellent Work!"
            elif percentage >= 60:
                grade = "B"
                message = "👍 Good Job!"
            elif percentage >= 50:
                grade = "C"
                message = "📘 Keep Improving!"
            else:
                grade = "Fail"
                message = "💪 Work Hard and Try Again!"

            status = "PASS" if percentage >= 50 else "FAIL"


            return render_template("index.html",
                                   result=True,
                                   name=name,
                                   m1=m1, m2=m2, m3=m3, m4=m4, m5=m5,
                                   total=total,
                                   percentage=percentage,
                                   average=percentage,
                                   grade=grade,
                                   status=status,
                                   message=message)

        # Login check
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "allen" and password == "2007":
            return render_template("index.html", show_marks=True)
        else:
            return render_template("index.html", error="Invalid Login ❌")

    return render_template("index.html")
    
@app.route("/report")
def report():
    return render_template("report.html")


if __name__ == "__main__":
    app.run(debug=True)