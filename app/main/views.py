from flask import render_template,g,session,redirect,url_for
from . import main
from .. import db
from ..models import Student,Score
from sqlalchemy import func

@main.before_app_first_request
def bf_first_request():
    main.studentNum = db.session.query(func.count(Student.id)).scalar()

@main.route("/")
@main.route("/welcome")
def index():
    #g.courseNum=db.session.query(Score.courseName, func.count(Score.courseName)).group_by(Score.courseName).first()[1]
    g.studentNum=main.studentNum
    major=db.session.query(Student.majorName,func.count(Student.id).label("majorNum")).group_by(Student.majorName).all()
    g.majorNum=len(major)
    totalNum = 0
    # 计算各专业占百分比
    majors = []
    for classes in major:
        totalNum += classes.majorNum
        majors.append(list(classes))

    for classes in majors:
        classes[1] = (int(classes[1] / totalNum * 100))

    top20score = Student.query.order_by(Student.average.desc()).all()[:20]

    g.major = major
    g.majors=majors
    g.score = top20score
    course=db.session.query(Score.courseName,func.count(Score.id).label("courseNum")).group_by(Score.courseName).all()
    g.courseNum=len(course)
    g.course=course
    male = db.session.query(Student.id).filter_by(gender='男').count()
    female = db.session.query(Student.id).filter_by(gender='女').count()
    g.male = male
    g.female = female
    return render_template("index.html",studentNum=main.studentNum,g=g)

@main.route("/student",methods=["GET","POST"])
def students():
    return render_template("students.html",studentNum=main.studentNum)

@main.route('/<location>/<int:id>', methods=["GET","POST"])
def person(location, id):
    g.id = id
    info = Student.query.filter_by(id=id).all()[0]
    score = Score.query.filter_by(studentId=id).all()
    g.info = info
    g.score = score
    return render_template("person.html", studentNum=main.studentNum, g = g)

@main.route("/lesson",methods=["GET","POST"])
def lessons():

    return render_template("lessons.html",studentNum=main.studentNum)


@main.route("/totalRank",methods=["GET","POST"])
def totalRank():
    topscore = Student.query.order_by(Student.average.desc()).all()[:300]
    for stu in topscore:
        stu.average = round(stu.average, 2)
    g.score = topscore
    return render_template("totalRank.html", studentNum = main.studentNum, g = g)


@main.route("/specializedRank",methods=["GET","POST"])
def specializedRank():
    software_score = Student.query.filter_by(majorName = '软件工程').order_by(Student.average.desc()).all()[:20]
    for stu in software_score:
        stu.average = round(stu.average, 2)
    civil_score = Student.query.filter_by(majorName = '土木工程').order_by(Student.average.desc()).all()[:20]
    for stu in civil_score:
        stu.average = round(stu.average, 2)
    info_score = Student.query.filter_by(majorName = '信息管理与信息系统').order_by(Student.average.desc()).all()[:20]
    for stu in info_score:
        stu.average = round(stu.average, 2)
    e_bussiness_score = Student.query.filter_by(majorName = '电子商务').order_by(Student.average.desc()).all()[:20]
    for stu in e_bussiness_score:
        stu.average = round(stu.average, 2)
    e_bussiness_s_score = Student.query.filter_by(majorName = '电子商务（专）').order_by(Student.average.desc()).all()[:20]

    net_score = Student.query.filter_by(majorName = '网络工程').order_by(Student.average.desc()).all()[:17]
    for stu in net_score:
        stu.average = round(stu.average, 2)
    cs_score = Student.query.filter_by(majorName = '计算机科学与技术').order_by(Student.average.desc()).all()[:20]
    for stu in cs_score:
        stu.average = round(stu.average, 2)
    specializedScore = []
    specializedScore.append({'name': '软件工程', 'score': software_score})
    specializedScore.append({'name': '土木工程', 'score': civil_score})
    specializedScore.append({'name': '信息管理与信息系统', 'score': info_score})
    specializedScore.append({'name': '电子商务', 'score': e_bussiness_score})
    specializedScore.append({'name': '电子商务（专）', 'score': e_bussiness_s_score})
    specializedScore.append({'name': '网络工程', 'score': net_score})
    specializedScore.append({'name': '计算机科学与技术', 'score': cs_score})
    g.specializedScore = specializedScore
    return render_template("specializedRank.html", studentNum = main.studentNum, g = g)


def queryAvgTwo(key):
    studentid = "17110250102"
    result = db.session.query(Student.id, Student.gender, Student.departmentName, Student.majorName, Student.className,
                              Student.grade, Student.jidian, Student.average).filter(Student.id == studentid).first()
    jidianPM = db.session.query(result[0], func.count("*")).filter(Student.jidian >= result[6]).first()
    averagePM = db.session.query(result[0], func.count("*")).filter(Student.average >= result[7]).first()
    print(jidianPM, averagePM)
    queryAvgTwo("性别")
    result=db.session.query(Score.courseId,Score.courseName,func.avg(Score.mark).label("average")).group_by(Score.courseId).order_by(db.desc("average")).all()
    jidianPM=db.session.query(result[0],func.count("*")).filter(Student.jidian>=result[6]).first()
    averagePM=db.session.query(result[0],func.count("*")).filter(Student.average>=result[7]).first()
    print(jidianPM,averagePM)
    queryAvgTwo("性别")
    keyDict={
        "性别":Student.gender,
        "学院":Student.departmentName,
        "专业":Student.majorName,
        "班级":Student.className,
        "年级":Student.grade
    }
    result=db.session.query(keyDict[key],func.avg(Student.average)).filter(Student.id == Score.studentId).group_by(keyDict[key]).all()
    print(result)
