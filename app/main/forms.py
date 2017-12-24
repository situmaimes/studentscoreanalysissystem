from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import DataRequired


class StudentForm(FlaskForm):
    studentId = StringField('StudentId', validators=[DataRequired()])
    submit = SubmitField('Submit')
class NormalForm(FlaskForm):
    string = StringField('String', validators=[DataRequired()])
    submit = SubmitField('Submit')
class CourseForm(FlaskForm):
    courseName = StringField('CourseName', validators=[DataRequired()])
    submit = SubmitField('Submit')
class Score(FlaskForm):
    info = SelectField('info', choices=[
        ('student', '个人'),
        ('major', '专业'),
        ("grade","年级"),
        ("class",'班级'),
        ("gender","性别"),
        ('department', '学院'),
        ('course', '课程'),("courseDe","课程性质")
    ])
    search = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CompareForm(FlaskForm):
    Name1 = StringField('Name1', validators=[DataRequired()])
    Name2 = StringField('Name2', validators=[DataRequired()])
    submit = SubmitField('Submit')



