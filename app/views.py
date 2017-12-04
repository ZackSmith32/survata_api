from app import app, db, models
from flask import request


def strip_split(s):
	return(s.strip('[').strip(']').lower())

@app.route('/', methods=['GET'])
def index():
	return "USAGE: /query/?ID:[id-number-here]&column=[column_name]"

@app.route('/query/', methods=['GET'])
def id_query():

	if request.args.get('id') is not None:
		respondent = strip_split(request.args.get('id'))
		res_obj = models.Respondent.query.filter_by( \
			survata_interview_id=respondent).first()
		if res_obj is None:
			return "The ID you specified does not match \
						any records in the database"		
	else:
		return "id improperly entered"
	
	if request.args.get('column') is not None:
		column = strip_split(request.args.get('column'))
		try:
			res = res_obj.__dict__[column]
			if res == '':
				return "Null"
		except (KeyError, TypeError):
			return "The column you specified does not exist"
	
	if request.args.get('survey') is not None:
		print('survey')
		survey = strip_split(request.args.get('survey'))
		try:
			res = 0
			for surv in res_obj.survey:
				if str(surv) == survey:
					res += 1
		except (KeyError, TypeError):
			return "Invalid survey parameter"
		
	return(str(res))

















