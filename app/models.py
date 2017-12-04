from app import db

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.String, nullable=False)
    viewer = db.Column(db.ForeignKey('respondent.id'))

    def __repr__(self):
    	return self.survey_id

class Respondent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    survey = db.relationship(Survey, backref='resp')

    survata_interview_id = db.Column(db.String(), index=True)
    date = db.Column(db.String, nullable=False)
    period = db.Column(db.Integer, nullable=False)
    length_of_interview = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    metro_area = db.Column(db.String, nullable=True)
    postal_code = db.Column(db.Integer, nullable=True)
    region = db.Column(db.String, nullable=False)
    division = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=True)
    gender = db.Column(db.String, nullable=False)
    age = db.Column(db.String, nullable=False)
    operating_system = db.Column(db.String, nullable=False)
    web_browser = db.Column(db.String, nullable=False)

















