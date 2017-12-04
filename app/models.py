from app import db

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
    # Surveys = db.relationship('Exposure', backref='respondent', lazy=True)
    # Servey_ID = db.column(db.Integer, db.ForeignKey(Exposure.id))

    def __repr__(self):
        return '<Respondent %r>' % (self.Survata_Interview_ID)

class Exposure(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	Survey_ID = db.Column(db.String, nullable=False)
	Respondent_ID = db.column(db.Integer, db.ForeignKey('Respondent.id'))
	Resopndent = db.relationship(Respondent, backref='Surveys', 
		primaryjoin="Exposure.Respondent_ID == Respondent.id")

	def __repr__():
		print("<Exposure {}>".format(self.Exposure))

'''

class DomainRoot(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class DomainPath(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    root_id = db.Column(db.ForeignKey(DomainRoot.id))
    root = db.relationship(DomainRoot, backref='paths')
   '''




















