from . import db

class Student(db.Model):
    __tablename__="students"
    id=db.Column(db.String(16),primary_key=True)
    gender=db.Column(db.String(2))
    departmentId=db.Column(db.String(4))
    departmentName=db.Column(db.String(64))
    majorId=db.Column(db.String(8))
    majorName=db.Column(db.String(64))
    classId=db.Column(db.String(16))
    className=db.Column(db.String(64))
    grade=db.Column(db.String(8))
    scores=db.relationship("Score",lazy='dynamic')
    average=db.Column(db.Float)
    jidian = db.Column(db.Float)
    youxiu = db.Column(db.Float)
    bujige = db.Column(db.Float)

    def __repr__(self):
        return "<Student %r %r %r %r %r %r %r %r >"%\
               (self.id,self.gender,self.departmentId,self.majorName,self.className,self.grade,self.average,self.jidian)

class Score(db.Model):
    __tablename__="scores"
    id = db.Column(db.Integer, primary_key=True)
    studentId=db.Column(db.String(16),db.ForeignKey("students.id"))
    courseId=db.Column(db.String(16))
    courseName=db.Column(db.String(64))
    classId=db.Column(db.Integer)
    termId=db.Column(db.Integer)
    termName=db.Column(db.String(64))
    year=db.Column(db.String(8))
    yearterm=db.Column(db.Integer)
    credit=db.Column(db.Float)
    courseDe=db.Column(db.String(4))
    mark=db.Column(db.Float)

    def __repr__(self):
        return '<Score %r %r %r %r %r %r >' % (self.studentId,self.courseName,self.credit,self.termName,self.courseDe,self.mark)



