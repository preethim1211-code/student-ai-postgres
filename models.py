from extensions import db
from datetime import datetime


class Student(db.Model):
    __tablename__ = 'students'

    id         = db.Column(db.Integer,     primary_key=True)
    roll_no    = db.Column(db.String(20),  unique=True, nullable=False)
    full_name  = db.Column(db.String(100), nullable=False)
    email      = db.Column(db.String(150), unique=True)
    gender     = db.Column(db.String(10))
    department = db.Column(db.String(50),  default='BCA')
    semester   = db.Column(db.Integer,     default=1)
    created_at = db.Column(db.DateTime,    default=datetime.utcnow)

    records     = db.relationship('AcademicRecord', backref='student', lazy=True, cascade='all,delete')
    attendance  = db.relationship('Attendance',     backref='student', lazy=True, cascade='all,delete')
    predictions = db.relationship('Prediction',     backref='student', lazy=True, cascade='all,delete')

    def to_dict(self):
        return {
            'id':         self.id,
            'roll_no':    self.roll_no,
            'full_name':  self.full_name,
            'email':      self.email      or '',
            'gender':     self.gender     or '',
            'department': self.department or 'BCA',
            'semester':   self.semester,
            'created_at': self.created_at.isoformat()
        }


class AcademicRecord(db.Model):
    __tablename__ = 'academic_records'

    id             = db.Column(db.Integer,     primary_key=True)
    student_id     = db.Column(db.Integer,     db.ForeignKey('students.id'))
    semester       = db.Column(db.Integer)
    subject        = db.Column(db.String(100))
    internal_marks = db.Column(db.Float,  default=0)
    external_marks = db.Column(db.Float,  default=0)
    total          = db.Column(db.Float,  default=0)
    grade          = db.Column(db.String(5), default='F')

    def to_dict(self):
        return {
            'id':             self.id,
            'student_id':     self.student_id,
            'semester':       self.semester,
            'subject':        self.subject,
            'internal_marks': self.internal_marks,
            'external_marks': self.external_marks,
            'total':          self.total,
            'grade':          self.grade
        }


class Attendance(db.Model):
    __tablename__ = 'attendance'

    id            = db.Column(db.Integer, primary_key=True)
    student_id    = db.Column(db.Integer, db.ForeignKey('students.id'))
    subject       = db.Column(db.String(100))
    total_classes = db.Column(db.Integer, default=0)
    attended      = db.Column(db.Integer, default=0)
    percentage    = db.Column(db.Float,   default=0)

    def to_dict(self):
        return {
            'id':            self.id,
            'student_id':    self.student_id,
            'subject':       self.subject,
            'total_classes': self.total_classes,
            'attended':      self.attended,
            'percentage':    self.percentage
        }


class Prediction(db.Model):
    __tablename__ = 'predictions'

    id              = db.Column(db.Integer,  primary_key=True)
    student_id      = db.Column(db.Integer,  db.ForeignKey('students.id'))
    predicted_grade = db.Column(db.String(5))
    risk_level      = db.Column(db.String(10))
    confidence      = db.Column(db.Float,    default=0)
    suggestions     = db.Column(db.Text)
    predicted_at    = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id':              self.id,
            'student_id':      self.student_id,
            'predicted_grade': self.predicted_grade,
            'risk_level':      self.risk_level,
            'confidence':      self.confidence,
            'suggestions':     self.suggestions,
            'predicted_at':    self.predicted_at.isoformat()
        }


class ChatSession(db.Model):
    __tablename__ = 'chat_sessions'

    id         = db.Column(db.Integer,  primary_key=True)
    student_id = db.Column(db.Integer,  db.ForeignKey('students.id'), nullable=True)
    message    = db.Column(db.Text)
    response   = db.Column(db.Text)
    intent     = db.Column(db.String(50))
    timestamp  = db.Column(db.DateTime, default=datetime.utcnow)
