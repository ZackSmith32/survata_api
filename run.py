from app import app, db, models
from config import basedir
import os
import csv
from datetime import datetime

# Load data into database if it hasn't been created yet
'''
if not os.path.exists(os.path.join(basedir, 'app.db')):
	try:
		print('populating database...')
		db.create_all()
		i = 1
		with open(os.path.join(basedir, 'take_home.csv')) as f:
			next(f)
			csv_file = csv.reader(f, dialect='excel')
			for line in csv_file:
				# if i == 10:
				# 	break
				print(i)
				temp = models.Respondent()
				temp.Survata_Interview_ID = line[1]
				# temp.Date = datetime.strptime(line[2], '%Y-%m-%d %H:%M:%S.%f')
				temp.Date = line[2]
				temp.Period = int(line[3])
				temp.Length_of_Interview = int(line[4])
				temp.Country = line[5]
				temp.State = line[6]
				temp.Metro_Area = line[7]
				if line[8]:
					temp.Postal_Code = int(line[8])
				else:
					temp.Postal_Code = None
				temp.Region = line[9]
				temp.Division = line[10]
				temp.City = line[11]
				temp.Gender = line[12]
				temp.Age = line[13]
				temp.Operating_System = line[14]
				temp.Web_Browser = line[15]
				i += 1
				db.session.add(temp)
				raw_exp_list = line[16].split('|')
				for raw_exp in raw_exp_list:
					exp_list = raw_exp.split(':')[-1].split(',')
					for exp in exp_list:
						print(exp)
						# new_exp = models.Exposure(
						# 			Survey_ID=exp,
						# 			Resopndent=temp)
			db.session.commit()
			print('out of loop')

	except Exception as e:
		print('ERROR: populating database failed')
		print(e)
		exit()
'''
db.create_all()
temp = models.Respondent()
temp.Surveys = [models.Exposure(), models.Exposure()]
app.run(debug=True)
































