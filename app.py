from flask import Flask, render_template

app = Flask(__name__)

def calculate_result(name, marks):
    total_marks = sum(marks)
    percentage = total_marks / len(marks)

    if percentage >= 75:
        division = "1st Division with Distinction"
    elif percentage >= 60:
        division = "1st Division"
    elif percentage >= 45:
        division = "2nd Division"
    else:
        division = "Fail"

    return {
        "name": name,
        "total": total_marks,
        "percentage": round(percentage, 2),
        "division": division
    }


@app.route("/")
def home():
    students = [
        ("Student 1", [80, 75, 70]),
        ("Student 2", [65, 60, 58]),
        ("Student 3", [85, 90, 88])
    ]

    results = []
    for student in students:
        results.append(calculate_result(student[0], student[1]))

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)
