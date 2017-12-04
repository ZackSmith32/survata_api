from app import db
'''

class Exposure(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	Survey_ID = db.Column(db.String, nullable=False)
	Respondent_ID = db.column(db.Integer, db.ForeignKey('respondent.id'))
	# Resopndent = db.relationship(Respondent, backref='Surveys', 
	# 	primaryjoin="Exposure.Respondent_ID == Respondent.id")

	def __repr__():
		print("<Exposure {}>".format(self.Exposure))

class Respondent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Survata_Interview_ID = db.Column(db.String(), index=True)
    Date = db.Column(db.String, nullable=False)
    Period = db.Column(db.Integer, nullable=False)
    Length_of_Interview = db.Column(db.Integer, nullable=False)
    Country = db.Column(db.String, nullable=False)
    State = db.Column(db.String, nullable=False)
    Metro_Area = db.Column(db.String, nullable=True)
    Postal_Code = db.Column(db.Integer, nullable=True)
    Region = db.Column(db.String, nullable=False)
    Division = db.Column(db.String, nullable=False)
    City = db.Column(db.String, nullable=True)
    Gender = db.Column(db.String, nullable=False)
    Age = db.Column(db.String, nullable=False)
    Operating_System = db.Column(db.String, nullable=False)
    Web_Browser = db.Column(db.String, nullable=False)
    Surveys = db.relationship('Exposure', backref='resp', lazy='dynamic',
    	primaryjoin="Respondent.id==Exposure.Respondent_ID")
    # Servey_ID = db.column(db.Integer, db.ForeignKey(Exposure.id))

    def __repr__(self):
        return '<Respondent %r>' % (self.Survata_Interview_ID)


'''

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.String, nullable=False)
    viewer = db.Column(db.ForeignKey('respondent.id'))

    def __repr__(self):
    	return self.survey_id

class Respondent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # survey_ids = db.Column(db.ForeignKey(Survey.id))
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

















