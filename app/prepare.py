from .models import Student,Score
from . import db
import xlrd
fileName="StudentAndScore.xls"
def processDB():
    db.create_all()
    data = xlrd.open_workbook(fileName)
    table = data.sheet_by_name("学生成绩信息")
    for i in range(1, table.nrows):
        values = table.row_values(i)
        one = Score(id=int(values[0]), studentId=values[1].strip(), courseId=values[2].strip(),
                    courseName=values[3].strip(),
                    classId=int(values[4]), termId=int(values[5]), termName=values[6], year=values[7],
                    yearterm=int(values[8]),
                    credit=values[9], courseDe=values[10], mark=values[11])
        db.session.add(one)
    table = data.sheet_by_name("学生信息")
    for i in range(1,table.nrows):
        values=table.row_values(i)
        one=Student(id=values[0],gender=values[1],departmentId=values[2],departmentName=values[3],
                    majorId=values[4],majorName=values[5],classId=values[6],className=values[7],grade=values[8])
        db.session.add(one)
    db.session.commit()


    for i in range(1,table.nrows):
        studentId = table.row_values(i)[0]
        student=db.session.query(Student).filter_by(id=studentId).first()
        student.jidian,student.average,student.youxiu,student.bujige=get(student.id)
    db.session.commit()






def get(studentId):
    scoreResult = db.session.query(Score.credit, Score.mark).filter(
        Score.studentId == studentId).all()
    if scoreResult==[]:
        return (None,None,None,None)
    scoreList=[]
    jidianList=[]
    credit=[]
    youxiu=0
    bujige=0
    for i in scoreResult:
        if i[1]>=90:
            youxiu+=1
        if i[1]<60:
            bujige+=1
        scoreList.append(i[1])
        credit.append(i[0])
        jidianList.append(jiDian(i[1])*xishu(i[0])*i[0])
    return (sum(jidianList)/sum(credit),sum(scoreList)/len(scoreList),youxiu/len(scoreList),bujige/len(scoreList))










def jiDian(mark):
    if 90<=mark<=100:
        return 4.0
    elif 85<=mark<=89:
        return 3.7
    elif 82<=mark<=84:
        return 3.3
    elif 78<=mark<=81:
        return 3.0
    elif 75<=mark<=77:
        return 2.7
    elif 72<=mark<=74:
        return 2.3
    elif 68<=mark<=71:
        return 2.0
    elif 66<=mark<=67:
        return 1.7
    elif 64<=mark<=65:
        return 1.3
    elif 60<=mark<=63:
        return 1.0
    else:
        return 0





def xishu(credit):
    if credit>=4:
        return 1.2
    else:
        return 1.0
