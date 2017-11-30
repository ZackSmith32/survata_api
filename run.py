from app import app, db, models
from config import basedir
import os

# does the import of basedir from config work?


if not os.path.exists(os.path.join(basedir, 'app.db')):
	try:
		print('populating database...')
		with open(basedir + 'take_home.csv') as f:
			for line in f.readline(10):
				line.strip().split(',')
				print(line)



		db.create_all()
	except Exception as e:
		print('ERROR: populating database failed')
		print(e)

app.run(debug=True)