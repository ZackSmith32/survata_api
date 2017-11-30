from app import db

class Respondent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Survata_Interview_ID = db.Column(db.String(64), index=True, unique=True)
    Date = db.Column(db.DateTime, nullable=False)
    Period = db.Column(db.Integer, nullable=False)
    Length_of_Interview = db.Column(db.Integer, nullable=False)
    Country = db.Column(db.String(2), nullable=False)
    State = db.Column(db.String, nullable=False)
    Metro_Area = db.Column(db.String, nullable=True)
    Postal_Code = db.Column(db.Integer, nullable=True)
    Region = db.Column(db.String, nullable=False)
    Division = db.Column(db.String, nullable=False)
    City = db.Column(db.String, nullable=True)
    Gender = db.Column(db.String, nullable=False)
    Age = db.Column(db.String, nullable=False)
    Operating_System = db.Column(db.String, nullable=False)
    Web_Browser =  db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<User %r>' % (self.Survata_Interview_ID)