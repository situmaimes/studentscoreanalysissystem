from flask import render_template,session,redirect,url_for
from . import main
from .. import db
from ..models import Student,Score
from sqlalchemy import func
@main.route("/welcome")
def hello():
    return "hello"

@main.route("/student",methods=["GET","POST"])
def studentAnalysis():
    studentid = "17110250102"
    result=db.session.query(Student.id,Student.gender,Student.departmentName,Student.majorName,Student.className,Student.grade,Student.jidian,Student.average).filter(Student.id==studentid).first()
    jidianPM=db.session.query(result[0],func.count("*")).filter(Student.jidian>=result[6]).first()
    averagePM=db.session.query(result[0],func.count("*")).filter(Student.average>=result[7]).first()
    print(jidianPM,averagePM)
    queryAvgTwo("性别")


@main.route("/course",methods=["GET","POST"])
def courseAnalysis():
    result=db.session.query(Score.courseId,Score.courseName,func.avg(Score.mark).label("average")).group_by(Score.courseId).order_by(db.desc("average")).all()
    jidianPM=db.session.query(result[0],func.count("*")).filter(Student.jidian>=result[6]).first()
    averagePM=db.session.query(result[0],func.count("*")).filter(Student.average>=result[7]).first()
    print(jidianPM,averagePM)
    queryAvgTwo("性别")

def queryAvgTwo(key):
    keyDict={
        "性别":Student.gender,
        "学院":Student.departmentName,
        "专业":Student.majorName,
        "班级":Student.className,
        "年级":Student.grade
    }
    result=db.session.query(keyDict[key],func.avg(Student.average)).filter(Student.id == Score.studentId).group_by(keyDict[key]).all()
    print(result)


