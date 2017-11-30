from app import app, db, models
from config import basedir
import os
import csv
from datetime import datetime

# if the data base has not been created, then populate database
# with "take_home.csv"
if not os.path.exists(os.path.join(basedir, 'app.db')):
	# try:
		print('populating database...')
		db.create_all()
		i = 1
		with open(os.path.join(basedir, 'take_home.csv')) as f:
			next(f)
			csv_file = csv.reader(f, dialect='excel')
			# del(csv_file[0])
			for line in csv_file:
				if i == 5:
					break
				# print(i, line)
				temp = models.Respondent()
				temp.Survata_Interview_ID = line[1]
				temp.Date = line[2]
				temp.Period = line[3]
				temp.Length_of_Interview = [4]
				temp.Country = line[5]
				temp.State = line[6]
				temp.Metro_Area = line[7]
				temp.Postal_Code = line[8]
				temp.Region = line[9]
				temp.Division = line[10]
				temp.City = line[11]
				temp.Gender = line[12]
				temp.Age = line[13]
				temp.Operating_System = line[14]
				temp.Web_Browser = line[15]
				i += 1
				db.session.add(temp)
			db.session.commit()



	# except Exception as e:
	# 	print('ERROR: populating database failed')
	# 	print(e)
	# 	exit()

app.run(debug=True)