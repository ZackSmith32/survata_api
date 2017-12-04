from app import app, db, models
from config import basedir
import os
import csv
from datetime import datetime

# Load data from csv into database if it hasn't been created yet
if not os.path.exists(os.path.join(basedir, 'app.db')):
	try:
		print('populating database...')
		db.create_all()
		i = 1
		with open(os.path.join(basedir, 'take_home.csv')) as f:
			next(f)
			csv_file = csv.reader(f, dialect='excel')
			for line in csv_file:
				temp = models.Respondent()
				temp.survata_interview_id = line[1]
				temp.date = line[2]
				temp.period = int(line[3])
				temp.length_of_interview = int(line[4])
				temp.country = line[5]
				temp.state = line[6]
				temp.metro_area = line[7]
				if line[8]:
					temp.postal_code = int(line[8])
				else:
					temp.postal_code = None
				temp.region = line[9]
				temp.division = line[10]
				temp.city = line[11]
				temp.gender = line[12]
				temp.age = line[13]
				temp.operating_system = line[14]
				temp.web_browser = line[15]
				i += 1
				db.session.add(temp)
				raw_exp_list = line[16].split('|')
				for raw_exp in raw_exp_list:
					exp_list = raw_exp.split(':')[-1].split(',')
					for exp in exp_list:
						new_exp = models.Survey(
									survey_id=exp.strip(),
									resp=temp)
						db.session.add(new_exp)

			db.session.commit()
			print('database created')

	except Exception as e:
		print('ERROR: populating database failed')
		print(e)
		exit()


app.run(debug=False)
































