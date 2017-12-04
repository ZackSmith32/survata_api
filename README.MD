# Survata API Take Home Assignment

Basic useful feature list:

 * Query for User id and Attribute
 * Query for count of exposures to a particuar survey
 * Flask Framework
 * SQLAlchemy ORM
 * SQLite relational database


Future improvements

 * Read CSV in chunks
 * Add more exception handling for query formatting
 * Querying with relative criteria (i.e. date > xyz)

How to run the server locally:

1. clone repo
2. `pip install -r requirements.txt`
3. `python run.py`
4. tested using chrome browser

User attribute query:

`localhost:5000/query/?id=[906050d3-20d9-4503-aba7-fbb863708474]&column=[operating_system]`
	> return ios

`localhost:5000/query/?id=[b3c48e9b-3be1-4351-8921-caeb73119df8]&column=[metro_area]`
	> return Null

User survey exposure count query:

`localhost:5000/query/?id=[68c5e638-a147-47ba-9f8a-eec5398c2152]&survey=[406497652]`
	> return 3

`localhost:5000/query/?id=[e806c51a-ada9-4ef5-a7b8-5d10d0bcacd1]&survey=[402938329]`
	> return 1