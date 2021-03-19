"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    rows = hackbright.get_grades_by_github(github)

    print("{} is the GitHub account for {} {}".format(github, first, last))

    return render_template("student_info.html", first=first, last=last, github=github, rows=rows)


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/new-student-form")
def new_student_form():
    """New Student Form."""
    return render_template("new_student_form.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""
    first_name = request.form.get('first_name',"")
    last_name = request.form.get('last_name',"")
    github = request.form.get('github',"")

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("student_add.html",github=github)

@app.route("/project", methods=['GET'])
def get_project():
    """List information about a project."""

    title = request.args.get('title',"")
    row = hackbright.get_project_by_title(title)

    return render_template("project_info.html", row=row)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")

