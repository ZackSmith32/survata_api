# Survata API Take Home Assignment

Basic useful feature list:

 * Query for User id and Attribute
 * Query for count of exposures to a particuar survey
 * SQLite relational database


Future improvements

 * Read CSV in chunks
 * Add more exception handling for query formatting
 * Querying with relative criteria (i.e. date > xyz)

How to run the server locally:

1. clone repo
2. `pip install -r requirements.txt`
3. `python run.py`

User attribute query:

`localhost:5000/query/?id=[906050d3-20d9-4503-aba7-fbb863708474]&column=[operating_system]`

User survey exposure count query:

`localhost:5000/query/?id=[68c5e638-a147-47ba-9f8a-eec5398c2152]&survey=[406497652]`
